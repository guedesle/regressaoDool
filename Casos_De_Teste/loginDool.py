import os
import pytest
from seleniumbase import SB, BaseCase

class LoginDoolTest(BaseCase):
    def test_login_to_dool(self):
        # Obtém as credenciais a partir das variáveis de ambiente ou usa valores padrão para teste
        username = os.environ.get("DOOL_USERNAME", "meu_usuario")
        password = os.environ.get("DOOL_PASSWORD", "minha_senha")
        
        # Abre a página de login
        self.open("http://dool.egba.ba.gov.br")
        
        # Preenche os campos de login
        self.type("input[name='username']", username)
        self.type("input[name='password']", password)
        
        # Clica no botão de envio
        self.click("button[type='submit']")
        
        # Verifica se o login foi bem-sucedido
        # Substitua 'div.welcome' pelo seletor que confirma o sucesso do login na sua aplicação
        self.assert_element("div.welcome")
        
        # Log de confirmação (opcional)
        self.log("Login realizado com sucesso!")

# Permite a execução do teste via pytest
if __name__ == '__main__':
    pytest.main(["-v", __file__])
