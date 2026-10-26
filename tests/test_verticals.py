import pytest

from pages.verticals import verticals

@pytest.mark.smoke
def test_verticals_trading(page):
    vertical_tab_obj=verticals(page)
    vertical_tab_obj.trading_options_clicking()

@pytest.mark.smoke
def test_verticals_Retails_Ecommerce(page):
    vertical_tab_obj=verticals(page)
    vertical_tab_obj.Retail_Ecommerce_options_Clicking()

@pytest.mark.smoke
def test_verticals_Healthcare(page):
    vertical_tab_obj=verticals(page)
    vertical_tab_obj.Healthcare_options_clicking()

@pytest.mark.smoke
def test_verticals_Fintech(page):
    vertical_tab_obj=verticals(page)
    vertical_tab_obj.Fintech_options_clicking()

@pytest.mark.smoke
def test_verticals_Custom(page):
    vertical_tab_obj=verticals(page)
    vertical_tab_obj.Custom_options_clicking()