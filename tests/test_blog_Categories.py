import pytest
from pages.blog_Categories import blog

@pytest.mark.smoke
def test_blog_catergories_tab(page):
    blog_obj=blog(page)
    blog_obj.blog_catergories_clicking()