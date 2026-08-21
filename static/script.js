document.addEventListener("DOMContentLoaded", () => {
    const produtosContainer = document.getElementById("produtos-container");
    const cartCount = document.getElementById("cart-count");
    let carrinhoTotal = 0;

    // Busca os produtos da API do Flask
    fetch('/api/produtos')
        .then(response => response.json())
        .then(produtos => {
            produtosContainer.innerHTML = "";
            produtos.forEach(produto => {
                const card = document.createElement("div");
                card.className = "card";
                
                card.innerHTML = `
                    <img src="/static/${produto.imagem_url}" alt="${produto.nome}" class="card-img">
                    <h3>${produto.nome}</h3>
                    <p>${produto.descricao}</p>
                    <div class="preco">R$ ${produto.preco.toFixed(2).replace('.', ',')}</div>
                    <button onclick="adicionarCarrinho()">Comprar</button>
                `;
                produtosContainer.appendChild(card);
            });
        })
        .catch(error => console.error("Erro ao carregar produtos:", error));

    // Função de simulação de clique no carrinho
    window.adicionarCarrinho = function() {
        carrinhoTotal++;
        cartCount.innerText = carrinhoTotal;
    };

    // Lógica do botão do carrinho no topo
    const carrinhoBtn = document.querySelector('.carrinho-btn');
    if (carrinhoBtn) {
        carrinhoBtn.addEventListener('click', function(event) {
            event.preventDefault();
            if (carrinhoTotal === 0) {
                alert("Seu carrinho está vazio! Adicione nossos cupcakes saudáveis antes de fechar o pedido.");
            } else {
                alert("Você tem " + carrinhoTotal + " cupcake(s) no carrinho!\n\n🎉 Simulação de compra finalizada com sucesso!\nMuito obrigado por testar o nosso sistema.");
                carrinhoTotal = 0;
                cartCount.innerText = carrinhoTotal;
            }
        });
    }
});