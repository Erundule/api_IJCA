from fastapi import APIRouter, HTTPException
# Importamos os dados e as funções de busca do nosso módulo de dados
from api_ijca.dados import menu, find_produto_by_id, find_produto_by_name, add_produto, remove_produto

# 1. Criamos um roteador
router = APIRouter(
    prefix="/menu",  # Adiciona /menu na frente de todas as rotas
    tags=["Menu"]    # Agrupa na documentação /docs
)

# 2. Definimos as rotas usando o @router

@router.get("/")
def get_menu():
    """
    Retorna o cardápio (menu) completo.
    (O path final será /menu/)
    """
    return menu

@router.get("/{item_id}")
def get_menu_item(item_id: int):
    """
    Retorna um item específico pelo ID.
    (O path final será /menu/{item_id})
    """
    item = find_produto_by_id(item_id)
    if item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item

@router.get("/nome/{item_name}")
def get_menu_item_by_name(item_name: str):
    """
    Retorna um item específico pelo nome.
    (O path final será /menu/nome/{item_name})
    """
    item = find_produto_by_name(item_name)
    if item is None:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return item

@router.post("/")
def add_menu_item(item: dict):
    """
    Adiciona um novo item ao cardápio.
    (O path final será /menu/)
    """
    
    try:
        if find_produto_by_id(item['id']) is not None:
            raise HTTPException(status_code=400, detail="Algum item com esse ID já existe") 
        else:
            result = add_produto(item)
            return result
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    

@router.delete("/{item_id}")
def delete_menu_item(item_id: int):
    """
    Remove um item do cardápio pelo ID.
    (O path final será /menu/{item_id})
    """
    success = remove_produto(item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item não encontrado")
    return {"message": "Item removido com sucesso"}
    
