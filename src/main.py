from fastapi import FastAPI

# 2. Cria a aplicação principal
app = FastAPI(
    title="API do Restaurante",
    description="API para gerenciar o cardápio do restaurante.",
    version="0.1.0"
)

# 4. Define um endpoint raiz para verificar se a API está funcionando
@app.get("/")
def hello_world_root():
    """
    Endpoint raiz da aplicação.
    """
    return {"status": "Online", "message": "Bem-vindo à API do Restaurante!"}