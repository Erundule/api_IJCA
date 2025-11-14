#  API do Restaurante (`api-ijca`)

API simples para gerenciar o cardápio (menu) de um restaurante, construída com FastAPI e Poetry.

Este projeto demonstra uma estrutura de API limpa, separando a lógica de rotas, a lógica de dados e a configuração da aplicação.

## 📋 Descrição do Projeto

Esta API fornece endpoints para listar, buscar, adicionar e remover itens de um cardápio. Em vez de um banco de dados real, ela utiliza uma lista em memória (`menu`) como uma simulação de banco de dados, tornando-a ideal para fins de aprendizado e prototipagem rápida.

## 🛠️ Tecnologias Utilizadas

* **Python 3.14+**
* **[FastAPI](https://fastapi.tiangolo.com/)**: O framework web para construir a API.
* **[Uvicorn](https://www.uvicorn.org/)**: O servidor ASGI para rodar a aplicação.
* **[Poetry](https://python-poetry.org/)**: Para gerenciamento de dependências e do ambiente virtual.

## ⚙️ Instalação e Configuração

Para rodar este projeto localmente, siga os passos abaixo.

**Pré-requisitos:**
* Python (versão >=3.14, conforme `pyproject.toml`)
* [Poetry](https://python-poetry.org/docs/#installation) instalado globalmente.

**Passos:**

1.  **Clone o repositório:**
    ```bash
    git clone <URL-DO-SEU-REPOSITORIO>
    cd api_IJCA-4b76de6b5424323c403dbad7311e1426a51265d1 
    ```
    *(Substitua o nome da pasta se necessário)*

2.  **Instale as dependências:**
   Instale o poetry com
    ```bash
    pip install poetry
    ```
    O Poetry criará um ambiente virtual (`.venv`) e instalará o `fastapi` e `uvicorn` definidos no `pyproject.toml`.
    ```bash
    poetry install
    ```

## 🔥 Executando o Servidor

Existem duas formas de rodar o servidor:

**1. (Recomendado) Usando `poetry run`:**
Este comando executa o Uvicorn dentro do ambiente virtual gerenciado pelo Poetry.

```bash
# A partir da pasta raiz do projeto
poetry run uvicorn main:app --reload --app-dir src
