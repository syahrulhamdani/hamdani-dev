import os


LOGO_FILENAME = os.getenv("LOGO_FILENAME", "")
APP_NAME = os.getenv("APP_NAME", "App")
PAGES_CONFIG = {
    "home": {
        "page_title": "Syahrul B Hamdani",
        "page_icon": "🚀",
        "layout": "wide",
        "initial_sidebar_state": "collapsed",
    },
    "resume": {
        "page_title": "Resume",
        "page_icon": "📜",
        "initial_sidebar_state": "collapsed",
    },
    "dashboard": {
        "page_title": "YouTube Trending Dashboard",
        "page_icon": "🎥",
        "initial_sidebar_state": "collapsed",
    }
}
