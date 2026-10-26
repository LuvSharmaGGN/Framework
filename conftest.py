from datetime import datetime
import os
from pathlib import Path
import re
import shutil

import pytest
from playwright.sync_api import sync_playwright
import pytest_html
from config import base_url


@pytest.fixture(scope="session")
def recordings_dir():
    run_id = datetime.now().strftime("%Y%m%d_%H%M%S_%f")
    recordings_path = Path("recordings")
    recordings_path.mkdir(exist_ok=True)

    for previous_run in recordings_path.iterdir():
        if previous_run.is_dir() and re.fullmatch(
            r"\d{8}_\d{6}_\d{6}", previous_run.name
        ):
            shutil.rmtree(previous_run)

    path = recordings_path / run_id
    path.mkdir(parents=True, exist_ok=False)
    return path


@pytest.fixture
def page(request, recordings_dir):
    p = sync_playwright().start()
    browser = None
    context = None
    video = None
    video_name = re.sub(r"[^A-Za-z0-9._-]+", "_", request.node.nodeid)
    video_path = recordings_dir / f"{video_name}.webm"

    try:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(
            ignore_https_errors=True,
            record_video_dir=str(recordings_dir),
        )
        page = context.new_page()
        video = page.video

        page.goto(base_url)
        page.wait_for_load_state("load")

        yield page
    finally:
        try:
            if context is not None:
                context.close()
            if video is not None:
                video.save_as(str(video_path))
                Path(video.path()).unlink()
        finally:
            try:
                if browser is not None:
                    browser.close()
            finally:
                p.stop()


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    extra = []

    if report.when == "call":
        recordings_dir = item.funcargs.get("recordings_dir")
        html_path = item.config.getoption("htmlpath")
        if recordings_dir is not None and html_path:
            video_name = re.sub(r"[^A-Za-z0-9._-]+", "_", item.nodeid)
            video_path = Path(recordings_dir) / f"{video_name}.webm"
            report_path = Path(html_path).resolve()
            video_url = os.path.relpath(
                video_path.resolve(), start=report_path.parent
            ).replace(os.sep, "/")
            video_html = (
                '<video controls preload="metadata" width="480">'
                f'<source src="{video_url}" type="video/webm">'
                "Your browser does not support HTML video."
                "</video>"
            )
            extra.append(pytest_html.extras.html(video_html))

        if report.failed:
            page = item.funcargs.get("page")

            if page:
                screenshots_dir = Path("screenshots")
                screenshots_dir.mkdir(exist_ok=True)

                file_name = screenshots_dir / f"{item.name}.png"

                page.screenshot(path=str(file_name))

                extra.append(pytest_html.extras.image(str(file_name)))

        if extra:
            report.extras = getattr(report, "extras", []) + extra