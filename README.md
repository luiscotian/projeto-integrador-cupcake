# Cupcake Gourmet Valentim - Aplicação Full Stack (PIT II)

> Projeto Integrador Transdisciplinar em Engenharia de Software II

Aplicação completa desenvolvida para a gestão e comercialização de cupcakes artesanais saudáveis (adoçados naturalmente). O projeto adota uma arquitetura em camadas (**MVC**) baseada em uma API RESTful, integrando um banco de dados relacional **SQLite**, uma API de back-end em **Python (Flask)** e uma interface de usuário web moderna e responsiva utilizando **HTML, CSS e JavaScript**.

---

## Tecnologias Utilizadas

* **Linguagem Principal:** Python 3.14
* **Back-end (API REST):** Flask
* **Banco de Dados:** SQLite
* **Front-end (UI):** HTML5, CSS3, JavaScript
* **Hospedagem:** PythonAnywhere
* **Ambiente de Desenvolvimento:** VS Code

---

## Arquitetura do Sistema (MVC)

A aplicação segue o padrão de arquitetura **Model-View-Controller**:

* **Model (`app.py` / `loja_cupcakes.db`):** Gestão da persistência dos dados de produtos (cupcakes) utilizando SQLite.
* **Controller (`app.py`):** Servidor Flask que expõe os endpoints HTTP/REST, contendo a lógica de negócio e serializando os dados em formato JSON.
* **View (`templates/index.html` e `static/`):** Interface web desenvolvida com HTML/CSS, responsável por consumir a API REST via JavaScript e entregar uma experiência reativa ao usuário final.

---

## Endpoints da API REST

A API disponibiliza os seguintes caminhos para consumo:

| Método | Rota | Descrição |
| :--- | :--- | :--- |
| `GET` | `/` | Renderiza a página principal do cardápio |
| `GET` | `/api/produtos` | Retorna a lista de todos os cupcakes cadastrados em formato JSON |

---

## Estrutura do Repositório

```text
projeto-integrador-cupcake/
├── static/
│   ├── script.js             # Lógica de consumo da API e interação do carrinho
│   └── style.css             # Estilização da interface
├── templates/
│   └── index.html            # Estrutura da interface do usuário
├── app.py                    # Back-end / API Flask (Controller/Model)
├── .gitignore                # Arquivos ignorados pelo Git (venv/, *.db)
└── README.md                 # Documentação principal
