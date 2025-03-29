from seleniumbase import BaseCase
BaseCase.main(__name__, __file__)

class Test_acessarVersaoHTML(BaseCase):
    def test_acessarHome(self):
        self.open("http://dool.egba.ba.gov.br")
        self.assert_element("#imagemCapa")
        self.click("#downloadHTML")
        self.assert_element("#modal-acessolivre")
        self.click("#modal-acessolivre")
        self.click("#tree > li:nth-child(1) > div")
        
        try:
            self.click("#tree > li.collapsable > ul > li:nth-child(1) > div")
            self.click("#tree > li.collapsable > ul > li.collapsable > ul > li > span > a")
            self.assert_element_visible('body > div > table > tbody')
        
        
        except:
            self.click("#tree > li.collapsable > ul > li.collapsable > ul > li > span > a")
 