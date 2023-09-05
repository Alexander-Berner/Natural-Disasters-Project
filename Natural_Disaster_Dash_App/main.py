# To run web app, open:
# http://127.0.0.1:8050/

from dash_app.app import app
from dash_app.tabs.tab import make_tab_layout


if __name__ == '__main__':
    app.layout = make_tab_layout()
    app.run_server(debug=True)
