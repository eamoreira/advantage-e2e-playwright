# E2E Tests - Advantage Online Shopping

Automação de testes para o site de demonstração [Advantage Online Shopping](https://www.advantageonlineshopping.com)

## 🚀 Como executar

```bash
# Instalar dependências
pip install -r requirements.txt
playwright install

# Executar todos os testes
pytest tests/ -v

# Executar teste específico
pytest tests/test_order_flow.py::test_registro_usuario_simples -v
```

## 🧪 Funcionalidades testadas

- ✅ Registro de usuário
- ✅ Login/Logout
- ✅ Busca de produtos
- ✅ Adicionar ao carrinho
- ✅ Checkout
- ✅ Pagamento SafePay
- ✅ Navegação por categorias

## 📄 Testes BDD (Gherkin)

Os cenários de teste também estão descritos em arquivos `.feature` utilizando a sintaxe Gherkin, facilitando a documentação e entendimento dos fluxos de negócio:

- `features/advantage_shopping.feature`
- `features/autenticacao.feature`
- `features/fluxo_compras.feature`
- `features/navegacao_produtos.feature`

Esses arquivos detalham os requisitos e comportamentos esperados do sistema de forma legível para todos os envolvidos no projeto.

## 🐞 Bug Reports

Relatórios de bugs encontrados durante a automação são documentados na pasta `bug report/`, como por exemplo:

- `bug report/Erro ao Tentar Login com Facebook.md`: detalha o erro 403 ao tentar login via Facebook, incluindo passos para reprodução, resultado atual, esperado, evidências e recomendações de correção.

## 📊 Status atual

**11/11 testes passando (100% sucesso)**

## 📁 Estrutura do projeto

```
tests/
  test_order_flow.py     # Testes principais
features/
  *.feature             # Cenários em Gherkin (documentação)
bug report/
  *.md                  # Relatórios de bugs
conftest.py             # Configuração Playwright
pytest.ini              # Configuração pytest
requirements.txt        # Dependências
```

## 🔧 Configuração

O projeto usa:
- **Playwright** para automação web
- **pytest** como test runner
- **Python 3.13+**

Testes executam no Chrome em modo headless por padrão.

## 🛠️ Ferramentas e Suporte

- Utilizou-se a ferramenta `playwright codegen` para gravar e gerar scripts de automação de forma rápida.
- O desenvolvimento contou com suporte do ChatGPT e consulta à [documentação oficial do Playwright](https://playwright.dev/python/).


> ⚠️ **Nota:** O site de demonstração utilizado para os testes é relativamente lento, o que pode dificultar a criação da automação. Em alguns casos, foi necessário adicionar delays ou aguardar elementos específicos para garantir o funcionamento estável dos testes. Além disso, em alguns momentos pode ocorrer timeout devido à lentidão do site.


## Melhorias futuras (opcional)
- [ ] Converter projeto para POM (Page Object Models)
- [ ] Tirar prints automáticos em falhas
- [ ] Execução em múltiplos browsers
- [ ] Relatórios HTML mais detalhados
- [ ] Integração CI/CD (pipeline)