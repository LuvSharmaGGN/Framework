import pytest
from pages.technologies import technologies

@pytest.mark.smoke
def test_eCommerce_Development_tab(page):
    technologies_tab_obj=technologies(page)
    technologies_tab_obj.eCommerce_Development_clicking()
    
@pytest.mark.smoke
def test_Mobile_Development_tab(page):
    technologies_tab_obj=technologies(page)
    technologies_tab_obj.Mobile_Development_clicking()

@pytest.mark.smoke
def test_Artificial_Intelligence_tab(page):
    technologies_tab_obj=technologies(page)
    technologies_tab_obj.Artificial_Intelligence_clicking()
