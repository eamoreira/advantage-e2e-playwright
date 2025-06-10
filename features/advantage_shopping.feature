
Funcionalidade: E-commerce Advantage Online Shopping
  Como um cliente do e-commerce Advantage Online Shopping
  Eu quero realizar compras online de forma segura e eficiente
  Para poder adquirir produtos eletrônicos facilmente

  Contexto:
    Dado que acesso o site "https://www.advantageonlineshopping.com/#/"
 
  Cenário: Cadastro de novo usuário com dados válidos
    Quando acesso a área de usuário
    E seleciono a opção "CREATE NEW ACCOUNT"
    E preencho o formulário de cadastro com as seguintes informações:
      | campo               | valor                    |
      | username            | user{dinamico}           |
      | email               | test{dinamico}@test.com  |
      | password            | {senha_valida}           |
      | confirm_password    | {senha_valida}           |
    E aceito os termos e condições
    E clico em "REGISTER"
    Então meu cadastro é concluído com sucesso
    E sou automaticamente logado no sistema

  Cenário: Tentativa de cadastro com username muito longo
    Quando acesso a área de usuário 
    E seleciono a opção "CREATE NEW ACCOUNT"
    E informo no campo de usuário "usuariocommaisde15caracteres"
    E preencho os demais campos com informações válidas
    Então uma mensagem de erro no campo do usuário é exibida informando o limite de caracteres

  Cenário: Acesso bem-sucedido com credenciais válidas
    Dado que possuo um usuário já cadastrado no sistema
    E estou na tela de login
    Quando informo minhas credenciais de acesso:
      | campo     | valor          |
      | username  | {user_valido}  |
      | password  | {senha_valida} |
    E clico em "SIGN IN"
    Então sou logado com sucesso
    E meu nome de usuário é exibido no menu principal

  Cenário: Tentativa de login com credenciais inválidas
    Quando acesso a área de usuário
    E informo as seguintes credenciais inválidas:
      | campo     | valor              |
      | username  | usuario_inexistente|
      | password  | senha_incorreta    |
    E clico em "SIGN IN"
    Então uma mensagem de erro de autenticação é exibida
    E devo permanecer na tela de login

  Cenário: Saída (Logout) bem-sucedida do sistema
    Dado que estou logado no Advantage Online Shopping
    Quando clico no ícone do meu perfil
    E seleciono a opção "Sign out"
    Então devo ser deslogado do sistema com sucesso
    E a tela é redirecionada para a home page
 
  Cenário: Exploração de produtos por categoria
    Quando navego até a categoria "Tablets"
    Então os produtos pertencentes à categoria Tablets são exibidos
    E visualizo produtos como "HP Elite x2", "HP Pro" e "Samsung Galaxy"

  Cenário: Verificação dos detalhes de um produto específico
   Dado que estou navegando na categoria "Tablets"
    Quando clico no produto "HP Pro Tablet"
    Então os detalhes completos do produto são exibidos
    E o preço "$479.00" é apresentado
    E o botão "ADD TO CART" está visível

  Cenário: Adicionar produto ao carrinho
   Dado que estou na página de detalhes do produto "HP Pro Tablet"
    Quando  clico no botão "ADD TO CART"
    Então o produto deve ser adicionado ao carrinho
    E o botão "CHECKOUT ($479.00)" é exibido

  Cenário: Redirecionamento para login ao iniciar checkout deslogado
    Dado que meu carrinho contém um produto
    E não estou logado no sistema
    Quando clico em "CHECKOUT"
    Então sou direcionado para a página de login
    E após realizar o login, o processo de checkout continuar

  Cenário: Início do processo de checkout com usuário logado
    Dado que estou logado no Advantage Online Shopping
    E tenho o produto "HP Pro Tablet" no meu carrinho
    Quando clico em "CHECKOUT ($479.00)"
    Então devo ser direcionado para a página de pagamento
    E o resumo do pedido é exibido
    E o produto "HP Pro Tablet" listado no resumo

  Cenário: Conclusão de compra utilizando SafePay
    Dado que estou na página de pagamento do checkout
    E tenho um produto no carrinho
    Quando clico em "NEXT" para prosseguir
    E informo os dados de pagamento do SafePay:
      | campo              | valor      |
      | safepay_username   | test02     |
      | safepay_password   | Ab12       |
    E clico em "PAY NOW"
    Então a confirmação do pagamento é exibida
    E a mensagem "Thank you for buying with" é apresentada
    E recebo um número de pedido para rastreamento

  Cenário: Falha no pagamento com dados inválidos do SafePay
    Dado que estou na página de pagamento do checkout
    Quando clico em "NEXT" para prosseguir
    E preencho dados inválidos do SafePay
      | campo              | valor         |
      | safepay_username   | usuario_erro  |
      | safepay_password   | senha_erro    |
    E clico em "PAY NOW"
    Então uma mensagem de erro é exibida
    E o pagamento não é finalizado

  Cenário: Fluxo completo de compra - do cadastro ao pagamento
    Quando realizo o cadastro de um novo usuário
    E navego até a categoria "Tablets"
    E seleciono o produto "HP Pro Tablet"
    E adiciono o produto ao carrinho de compras
    E inicio o processo de checkout
    E preencho os dados de pagamento do SafePay
    E confirmo a compra
    Então a confirmação do pedido é exibida
    E a mensagem de agradecimento é apresentada
    E recebo um número de pedido válido

  Cenário: Realização de compra com usuário já cadastrado
    Dado que possuo um usuário já cadastrado
    Quando realizo o login no sistema
    Quando realizo o login no sistema
    E seleciono o produto "HP Pro Tablet"
    E adiciono-o ao carrinho
    E concluo o processo de compra
    Então a compra é finalizada com sucesso

  Cenário: Adicionar múltiplos produtos ao carrinho
    Dado que estou logado no Advantage Online Shopping
    Quando adiciono o produto "HP Pro Tablet" ao carrinho
    E navego para outra categoria de produtos
    E adiciono um segundo produto ao carrinho
    Então ambos os produtos são exibidos no carrinho
    E o valor total da compra é calculado corretamente

  Cenário: Buscar produto por nome
    Quando utilizo a barra de busca do site
    E digito "HP Pro"
    E clico em buscar
    Então produtos relacionados a "HP Pro" são exibidos
    E consigo selecionar um dos produtos exibidos nos resultados

  Cenário: Acesso e visualização das informações do perfil
    Dado que estou logado no sistema
    Quando acesso a seção do meu perfil de usuário
    Então minhas informações pessoais são exibidas
    E posso editar meus dados cadastrais

  Esquema do Cenário:  Validação de campos obrigatórios durante o cadastro
    Quando tento realizar o cadastro deixando o campo "" vazio
    Então uma mensagem de erro específica para o campo "" é exibida
    E o cadastro não é concluído

    Exemplos:
      | campo             |
      | username          |
      | email             |
      | password          |
      | confirm_password  |

  Cenário: Navegação em dispositivo móvel
    Dado que estou usando um dispositivo móvel
    Quando navego pelas diferentes seções e páginas
    Então a interface deve se adaptar ao tamanho da tela
    E todas as funcionalidades devem estar acessíveis e utilizáveis

  Cenário: Requisitos de segurança para senhas no cadastro
    Quando tento me cadastrar usando uma senha considerada fraca:
      | senha    | criterio_faltante           |
      | 123      | muito curta                 |
      | abcd     | sem números e maiúsculas    |
      | ABCD     | sem números e minúsculas    |
      | 1234     | sem letras                  |
    Então uma mensagem de erro sobre a força da senha é exibida
    E o cadastro é impedido até que uma senha válida seja fornecida
