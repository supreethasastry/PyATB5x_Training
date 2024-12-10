from browserPackage.OpenBrowser import start_browser
from browserPackage.CloseBrowser import stop_browser
start_browser()
print("Without Case started")
stop_browser()

def TestCase():
    start_browser()
    print("Test Case started")
    stop_browser()

TestCase()