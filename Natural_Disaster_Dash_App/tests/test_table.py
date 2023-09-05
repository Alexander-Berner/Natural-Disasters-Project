from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from dash_app.tabs.tab import make_tab_layout
from dash_app.app import app


def test_tab001_dropdown_default(dash_duo):
    """
    GIVEN the app is running
    WHEN the tab is switched to tab-table
    THEN the drop down list should default to meteor
    """
    app.layout = make_tab_layout()
    dash_duo.start_server(app)

    # Get tab
    tab = dash_duo.driver.find_element_by_id('tab-table')

    # Click on tab
    dash_duo.driver.execute_script('arguments[0].click();', tab)

    # Get drop down text
    drop_down = dash_duo.find_element('#table-selector').text

    # Test if page title is correct
    assert 'Meteor datatable' in drop_down