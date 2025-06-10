
Funcionalidade: Fluxo de Compras E2E
  Como um cliente do e-commerce
  Eu quero realizar compras completas
  Para adquirir produtos do início ao fim

  Contexto:
    Dado que acesso o site "https://www.advantageonlineshopping.com/#/"

  Cenário: Compra completa - Cadastro ao pagamento
    Quando me registro como um novo usuário no sistema
    E navego até a categoria de produtos "Tablets"
    E seleciono o item "HP Pro Tablet"
    E adiciono o produto ao carrinho de compras
    E prossigo para o processo de checkout
    E preencho todos os dados de pagamento utilizando SafePay
    E confirmo a finalização da compra
    Então uma confirmação de pagamento com a mensagem "Thank you for buying" é exibida
    E um número de pedido válido é fornecido

  Cenário: Realização de compra com usuário já existente
    Dado que possuo um usuário previamente registrado
    Quando realizo o login no sistema
    E completo todo o processo de compra de um produto
    Então a compra é finalizada com sucesso

  Cenário: Conclusão do pedido utilizando SafePay
    Dado que tenho um produto adicionado ao carrinho
    E estou na página de finalização do pedido (checkout)
    Quando preencho os dados de pagamento do SafePay:
      | campo              | valor  |
      | safepay_username   | test02 |
      | safepay_password   | Ab12   |
    E clico no botão "PAY NOW"
    Então a confirmação do pagamento é exibida
    E uma mensagem de agradecimento pela compra é apresentada
