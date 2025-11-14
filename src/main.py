from fastapi import FastAPI
# 1. Importa o roteador que criamos
from api_ijca.routes import router

# 2. Cria a aplicação principal
app = FastAPI(
    title="API do Restaurante",
    description="API para gerenciar o cardápio do restaurante.",
    version="0.1.0"
)

# 3. Inclui o roteador do menu no aplicativo principal
app.include_router(router)


# 4. Define um endpoint raiz para verificar se a API está funcionando
@app.get("/")
def hello_world_root():
    """
    Endpoint raiz da aplicação.
    """
    return {"status": "Online", "message": "Bem-vindo à API do Restaurante!"}