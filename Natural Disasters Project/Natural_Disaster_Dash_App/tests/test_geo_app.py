from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from dash_app.tabs.tab import make_tab_layout
from dash_app.app import app


def test_geo001_h1_text_equals(dash_duo):
    """
    GIVEN the app is running
    WHEN the home page is available
    THEN the H1 heading element should include the text 'INTERNATIONAL GEOGRAPHIC' (not case sensitive)
    """
    app.layout = make_tab_layout()
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=4)
    h1_text = dash_duo.find_element("h1").text
    assert h1_text.casefold() == 'INTERNATIONAL GEOGRAPHIC'.casefold()
