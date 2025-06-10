
Funcionalidade: Autenticação de Usuários
  Como um usuário do e-commerce
  Eu quero me registrar e fazer login de forma segura
  Para acessar todas as funcionalidades do site

  Contexto:
    Dado que acesso o site "https://www.advantageonlineshopping.com/#/"

  Cenário: Cadastro bem-sucedido com dados válidos
    Quando preencho o formulário de cadastro com dados válidos
    E finalizo o processo de registro
    Então sou automaticamente logado no sistema
    E o menu de usuário logado é exibido

  Esquema do Cenário: Validação de campos durante o cadastro
    Quando tento me registrar informando "<campo>" com o valor inválido 
    Então uma mensagem de erro específica é exibida para o campo ""
    E o cadastro não é concluído
    Exemplos:
      | campo     | valor                          |
      | username  | usuariocommaisde15caracteres   |
      | email     | email_sem_arroba.com           |
      | password  | 123                            |

  Cenário: Login bem-sucedido com credenciais válidas
    Dado que possuo um usuário já cadastrado
    Quando informo minhas credenciais válidas na tela de login
    E clico para entrar
    Então sou logado com sucesso
    E o meu nome de usuário é exibido no menu principal

  Cenário: Saída (Logout) bem-sucedida do sistema
    Dado que estou logado no Advantage Online Shopping
    Quando clico na opção de "Sign out" (sair)
    Então sou deslogado do sistema
    E a tela de login é exibida novamente
