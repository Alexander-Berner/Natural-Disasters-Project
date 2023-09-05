from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from dash_app.tabs.tab import make_tab_layout
from dash_app.app import app

def test_lin001_h3_text_equals(dash_duo):
    """
    GIVEN the app is running
    WHEN the tab is switched
    THEN the H3 heading element should be the title of the switched tab
    """
    app.layout = make_tab_layout()
    dash_duo.start_server(app)

    # Get tab
    tab = dash_duo.driver.find_element_by_id('tab-line')

    # Click on tab
    dash_duo.driver.execute_script('arguments[0].click();', tab)

    # Get page title
    dash_duo.wait_for_element("h3", timeout=4)
    h3_text = dash_duo.find_element("h3").text

    # Test if page title is correct
    assert h3_text == 'Number of Events per Year'