document.addEventListener('DOMContentLoaded', () => { carregarProdutos(); });

async function carregarProdutos() {
    try {
        const response = await fetch('/api/produtos');
        const produtos = await response.json();
        const container = document.getElementById('produtos-container');
        
        produtos.forEach(produto => {
            const card = document.createElement('div');
            card.className = 'card';
            card.innerHTML = `
                <h3>${produto.nome}</h3>
                <p>${produto.descricao}</p>
                <div class="preco">R$ ${parseFloat(produto.preco).toFixed(2).replace('.', ',')}</div>
                <button onclick="adicionarCarrinho('${produto.nome}')">Adicionar ao Carrinho</button>
            `;
            container.appendChild(card);
        });
    } catch (error) { console.error('Erro:', error); }
}

let itensCarrinho = 0;
function adicionarCarrinho(nome) {
    itensCarrinho++;
    document.getElementById('cart-count').innerText = itensCarrinho;
    alert(`"${nome}" adicionado ao carrinho!`);
}

// Lógica para finalizar a simulação de compra
document.querySelector('.carrinho-btn').addEventListener('click', function(event) {
    event.preventDefault(); // Evita que a página recarregue ou pule para o topo
    let quantidade = document.getElementById('cart-count').innerText;
    
    if (quantidade === '0') {
        alert("Seu carrinho está vazio! Adicione nossos cupcakes saudáveis antes de fechar o pedido.");
    } else {
        alert("Você tem " + quantidade + " cupcake(s) no carrinho!\n\n🎉 Simulação de compra finalizada com sucesso!\nMuito obrigado por testar o nosso sistema.");
    }
});
