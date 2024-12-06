Parabens! por jogar junto 
aqui está 3 exemplos de como automatizar a a loja jogajunto.
fique avontade para criar de sua maneira.
estude os metodos utilizados e use sua criatividade.


Lista de pacotes necessários:
selenium

Biblioteca principal para automação de navegadores.

Copiar código:
pip install selenium
webdriver-manager

Gerenciador de WebDriver para facilitar o download do driver correto.

Copiar código:
pip install webdriver-manager
requests

Biblioteca para realizar requisições HTTP, usada para baixar imagens no código.

Copiar código:
pip install requests
behave

Ferramenta para desenvolvimento de testes utilizando o BDD (Behavior Driven Development).

Copiar código
pip install behave
pytest (opcional)

Caso você queira executar testes fora do contexto do Behave, pode ser útil.

Copiar código:
pip install pytest

chromedriver-autoinstaller (opcional, alternativa ao webdriver-manager)

Se preferir, pode usar este pacote para instalar o ChromeDriver.

Copiar código:
pip install chromedriver-autoinstaller

Comando consolidado para instalar tudo de uma vez:

Copiar código:
pip install selenium webdriver-manager requests behave

Requisitos do sistema:
Google Chrome:

Certifique-se de ter o Google Chrome instalado.
Atualize para a versão mais recente, se necessário.
Python:

Utilize o Python 3.7 ou superior.
Ambiente virtual (recomendado):

Crie um ambiente virtual para isolar as dependências:
Copiar código:

python -m venv venv
source venv/bin/activate  

# No Windows, use: venv\Scripts\activate

pip install selenium webdriver-manager requests behave

Com todos os pacotes instalados e o navegador configurado, você estará pronto para executar o código.