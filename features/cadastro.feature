Feature: Cadastro de Produto
  Como um administrador
  Eu quero cadastrar novos produtos
  Para que possam ser exibidos no site

  Scenario: Adicionar um novo produto
    Given que estou na página do Instituto Joga Junto
    When apertar o botão para adicionar produto
    And inserir as informações e clicar no botão de enviar novo produto
    Then o produto é cadastrado com sucesso
