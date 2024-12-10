from browserPackage.OpenBrowser import start_browser
from browserPackage.CloseBrowser import stop_browser
class TestCase:
    def TC1(self):
        start_browser()
        print("Testcase started")
        stop_browser()

obj=TestCase()
obj.TC1()