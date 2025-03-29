from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)

class HtmlInspectorTests(BaseCase):
    def test_html_inspector(self):
        self.open("https://dool.egba.ba.gov.br/")
        self.inspect_html()