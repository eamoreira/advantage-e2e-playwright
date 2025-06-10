Funcionalidade: Navegação e Produtos
  Como um cliente do e-commerce
  Eu quero navegar pelos produtos
  Para encontrar e selecionar itens para compra

  Contexto:
    Dado que acesso o site "https://www.advantageonlineshopping.com/#/"

  Cenário: Navegação bem-sucedida pela categoria Tablets
    Quando clico na categoria "Tablets"
    Então os produtos pertencentes a essa categoria são exibidos
    E consigo visualizar o produto "HP Pro Tablet" entre eles

  Cenário: Visualização detalhada de um produto específico
    Dado que estou na categoria "Tablets"
    Quando clico no produto "HP Pro Tablet"
    Então os detalhes completos do produto são exibidos
    E o preço "$479.00" é apresentado
    E o botão "ADD TO CART" está visível e funcional

  Cenário: Adicionar um produto ao carrinho de compras
    Dado que estou visualizando a página do produto "HP Pro Tablet"
    Quando clico no botão "ADD TO CART"
    Então o produto é adicionado ao meu carrinho de compras
    E a opção "CHECKOUT ($479.00)" é exibida, refletindo o valor do item

  Cenário:Busca de produto por nome
    Quando utilizo a função de busca do site
    E digito "HP Pro"
    E confirmo a busca
    Então os resultados relacionados a "HP Pro" são apresentados
    E consigo selecionar um produto específico entre os resultados exibidos
