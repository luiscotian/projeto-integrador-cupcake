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