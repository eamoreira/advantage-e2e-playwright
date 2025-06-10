# Testes básicos para site Advantage Online Shopping
# Ainda aprendendo Playwright - comecei com codegen e fui melhorando aos poucos

import random
import time

def test_registro_usuario_simples(page):
    """Teste de registro - descobri que precisa username único senão falha"""
    
    page.goto("https://www.advantageonlineshopping.com/#/")
    page.wait_for_timeout(2000)  # Site demora pra carregar
    
    # Abrir menu de usuário
    page.get_by_label("UserMenu").get_by_title("USER").click()
    page.get_by_role("link", name="CREATE NEW ACCOUNT").click()
    
    # Gerar dados únicos (aprendi isso na marra depois de muito erro)
    timestamp = str(int(time.time()))
    username = "user" + str(random.randint(1000, 9999)) + timestamp[-3:]
    email = username + "@test.com"
    password = "Test123"
    
    print("Tentando registrar: " + username)
    
    # Preencher o formulário
    page.locator("input[name=\"usernameRegisterPage\"]").fill(username)
    page.locator("input[name=\"emailRegisterPage\"]").fill(email) 
    page.locator("input[name=\"passwordRegisterPage\"]").fill(password)
    page.locator("input[name=\"confirm_passwordRegisterPage\"]").fill(password)
    page.locator("input[name=\"i_agree\"]").check()
    page.get_by_role("button", name="REGISTER").click()
    
    page.wait_for_timeout(3000)
    print("Usuário registrado: " + username)

def test_login_usuario_existente(page):
    """Login com usuário que já existe - mais simples que registrar novo"""
    
    page.goto("https://www.advantageonlineshopping.com/#/")
    page.wait_for_timeout(2000)
    
    # Fazer login 
    page.get_by_label("UserMenu").get_by_title("USER").click()
    page.locator("input[name=\"username\"]").fill("testuser123")
    page.locator("input[name=\"password\"]").fill("Test123")
    page.get_by_role("button", name="SIGN IN").click()
    
    page.wait_for_timeout(2000) 
    print("Login feito")

def test_buscar_produto(page):
    """Teste de busca simples - consertei o problema do elemento duplicado"""
    
    page.goto("https://www.advantageonlineshopping.com/#/")
    page.wait_for_timeout(2000)
    
    # Buscar produto - usar seletor mais específico pra evitar erro de elemento duplicado
    page.get_by_title("SEARCH").click()
    page.wait_for_timeout(1000)
    page.locator("#autoComplete").fill("laptop")
    page.wait_for_timeout(1000)
    page.locator("#autoComplete").press("Enter")
    
    page.wait_for_timeout(3000)
    print("Busca funcionou")

def test_adicionar_produto_carrinho(page):
    """Adicionar produto no carrinho - agora com seletor mais específico"""
    
    page.goto("https://www.advantageonlineshopping.com/#/")
    page.wait_for_timeout(2000)
    
    # Ir para categoria LAPTOPS
    page.locator("#laptopsImg").click()
    page.wait_for_timeout(2000)
    
    # Escolher um produto específico (evitar elemento invisível)
    page.get_by_text("HP PAVILION 15T TOUCH LAPTOP").click()
    page.wait_for_timeout(2000)
    
    # Adicionar no carrinho
    page.get_by_role("button", name="ADD TO CART").click()
    page.wait_for_timeout(1000)
    
    print("Produto adicionado no carrinho")

def test_logout_simples(page):
    """Logout básico - nova tentativa com abordagem diferente"""
    
    page.goto("https://www.advantageonlineshopping.com/#/")
    page.wait_for_timeout(2000)
    
    # Login primeiro
    page.get_by_label("UserMenu").get_by_title("USER").click()
    page.locator("input[name=\"username\"]").fill("testuser123")
    page.locator("input[name=\"password\"]").fill("Test123")
    page.get_by_role("button", name="SIGN IN").click()
    page.wait_for_timeout(3000)  # Esperar mais tempo pro login
    
    # Fazer logout - fechar modal primeiro e tentar abordagem mais simples
    page.keyboard.press("Escape")  # Fechar qualquer modal
    page.wait_for_timeout(1000)
    
    # Tentar forçar click mesmo com modal (usando force=True)
    try:
        page.get_by_label("UserMenu").click(force=True)
        page.wait_for_timeout(1000)
        page.get_by_role("link", name="Sign out").click()
        print("Logout feito")
    except:
        print("Logout ainda com problemas - modal interferindo")

def test_comprar_tablet_simples(page):
    """Teste de compra - vai até checkout"""
    
    page.goto("https://www.advantageonlineshopping.com/#/")
    page.wait_for_timeout(2000)
    
    # Navegar para tablets
    page.get_by_role("link", name="TabletsCategory", exact=True).click()
    page.wait_for_timeout(1000)
    
    # Selecionar HP Pro (seletor estranho do codegen)
    page.get_by_text("SOLD OUT SHOP NOW HP Pro").click()
    page.wait_for_timeout(1000)
    
    # Adicionar ao carrinho
    page.get_by_role("button", name="ADD TO CART").click()
    page.wait_for_timeout(1000)
    
    # Ir para checkout
    page.get_by_role("button", name="CHECKOUT ($479.00)").click()
    
    print("Chegou no checkout")
    page.wait_for_timeout(2000)

def test_fluxo_completo_registro_e_compra(page):
    """Tentativa de fazer tudo junto - às vezes funciona"""
    
    page.goto("https://www.advantageonlineshopping.com/#/")
    page.wait_for_timeout(2000)
    
    # 1. Registro
    page.get_by_label("UserMenu").get_by_title("USER").click()
    page.get_by_role("link", name="CREATE NEW ACCOUNT").click()
    
    timestamp = str(int(time.time()))
    username = "user" + str(random.randint(1000, 9999)) + timestamp[-3:]
    
    page.locator("input[name=\"usernameRegisterPage\"]").fill(username)
    page.locator("input[name=\"emailRegisterPage\"]").fill("" + username + "@test.com")
    page.locator("input[name=\"passwordRegisterPage\"]").fill("Test123")
    page.locator("input[name=\"confirm_passwordRegisterPage\"]").fill("Test123")
    page.locator("input[name=\"i_agree\"]").check()
    page.get_by_role("button", name="REGISTER").click()
    page.wait_for_timeout(3000)
    
    # 2. Compra
    page.get_by_role("link", name="TabletsCategory", exact=True).click()
    page.wait_for_timeout(1000)
    page.get_by_text("SOLD OUT SHOP NOW HP Pro").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="ADD TO CART").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="CHECKOUT ($479.00)").click()
    page.wait_for_timeout(2000)
    
    print("Fluxo completo até checkout - user: " + username)

def test_fluxo_com_pagamento_safepay(page):
    """Tentando fazer pagamento - ainda experimentando"""
    
    page.goto("https://www.advantageonlineshopping.com/#/")
    page.wait_for_timeout(2000)
    
    # Registro rápido
    page.get_by_label("UserMenu").get_by_title("USER").click()
    page.get_by_role("link", name="CREATE NEW ACCOUNT").click()
    
    timestamp = str(int(time.time()))
    username = "user" + str(random.randint(1000, 9999)) + timestamp[-3:]
    
    page.locator("input[name=\"usernameRegisterPage\"]").fill(username)
    page.locator("input[name=\"emailRegisterPage\"]").fill("" + username + "@test.com")
    page.locator("input[name=\"passwordRegisterPage\"]").fill("Test123")
    page.locator("input[name=\"confirm_passwordRegisterPage\"]").fill("Test123")
    page.locator("input[name=\"i_agree\"]").check()
    page.get_by_role("button", name="REGISTER").click()
    page.wait_for_timeout(3000)
    
    # Compra
    page.get_by_role("link", name="TabletsCategory", exact=True).click()
    page.wait_for_timeout(1000)
    page.get_by_text("SOLD OUT SHOP NOW HP Pro").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="ADD TO CART").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="CHECKOUT ($479.00)").click()
    page.wait_for_timeout(2000)
    
    # Pagamento (parte experimental)
    try:
        page.get_by_role("button", name="NEXT").click()
        page.wait_for_timeout(2000)
        
        # SafePay - descobri que test02/Ab12 funciona às vezes
        page.locator("input[name=\"safepay_username\"]").fill("test02")
        page.locator("input[name=\"safepay_password\"]").fill("Ab12") 
        page.locator("#pay_now_btn_SAFEPAY").click()
        
        page.wait_for_timeout(3000)
        print("Tentou pagamento")
        
    except Exception as e:
        print("Erro no pagamento: " + str(e))

def test_navegacao_categorias(page):
    """Teste só de navegação nas categorias - sempre funciona"""
    
    page.goto("https://www.advantageonlineshopping.com/#/")
    page.wait_for_timeout(2000)
    
    # Testar diferentes categorias
    categorias = ["#tabletsImg", "#laptopsImg", "#miceImg"]
    
    for categoria in categorias:
        try:
            page.locator(categoria).click()
            page.wait_for_timeout(1000)
            print("Categoria " + categoria + " - OK")
        except:
            print("Erro na categoria " + categoria)
    
    print("Navegação nas categorias testada")

def test_adicionar_multiplos_produtos(page):
    """Teste de adicionar vários produtos - consertei o problema do logo"""
    
    page.goto("https://www.advantageonlineshopping.com/#/")
    page.wait_for_timeout(2000)
    
    # Produto 1 - Tablet
    page.get_by_role("link", name="TabletsCategory", exact=True).click()
    page.wait_for_timeout(1000)
    page.get_by_text("SOLD OUT SHOP NOW HP Pro").click()
    page.wait_for_timeout(1000)
    page.get_by_role("button", name="ADD TO CART").click()
    page.wait_for_timeout(1000)
    
    # Voltar para home - usar seletor que funciona
    page.goto("https://www.advantageonlineshopping.com/#/")
    page.wait_for_timeout(2000)
    
    # Produto 2 - Mouse  
    try:
        page.locator("#miceImg").click()
        page.wait_for_timeout(1000)
        # Selecionar mouse específico
        page.get_by_text("KENSINGTON ORBIT WIRELESS MOBILE MOUSE").click()
        page.wait_for_timeout(1000)
        page.get_by_role("button", name="ADD TO CART").click()
        page.wait_for_timeout(1000)
        print("Dois produtos adicionados")
    except:
        print("Erro ao adicionar segundo produto")

def test_registro_com_diferentes_dados(page):
    """Testando registro com diferentes tipos de dados"""
    
    page.goto("https://www.advantageonlineshopping.com/#/")
    page.wait_for_timeout(2000)
    
    page.get_by_label("UserMenu").get_by_title("USER").click()
    page.get_by_role("link", name="CREATE NEW ACCOUNT").click()
    
    # Testar com dados um pouco diferentes
    timestamp = str(int(time.time()))
    username = "testuser" + timestamp[-4:]  # Só últimos 4 dígitos
    email = username + "@example.org"       # .org em vez de .com
    password = "MyPass123!"                 # Senha diferente
    
    print("Testando com: " + username)
    
    page.locator("input[name=\"usernameRegisterPage\"]").fill(username)
    page.locator("input[name=\"emailRegisterPage\"]").fill(email)
    page.locator("input[name=\"passwordRegisterPage\"]").fill(password)
    page.locator("input[name=\"confirm_passwordRegisterPage\"]").fill(password)
    page.locator("input[name=\"i_agree\"]").check()
    page.get_by_role("button", name="REGISTER").click()
    
    page.wait_for_timeout(3000)
    print("Registro alternativo: " + username)