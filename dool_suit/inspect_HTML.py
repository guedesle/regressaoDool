from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)

class Test_HtmlInspector(BaseCase):
    def test_html_inspector(self):
        self.open("https://dool.egba.ba.gov.br/ver-html/19768/#e:19768")
        self.inspect_html()
        
        
        
       