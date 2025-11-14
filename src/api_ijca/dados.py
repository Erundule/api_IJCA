
#arquivo que contém os dados do menu que vão ser usados na API
#nesse caso, estamos usando uma lista de dicionários para simular um banco de dados simples

menu = [
    {   'id': 1,
        'nome': 'café',
        'preco': 2.5
     },
    {
        'id': 2,
        'nome': 'torta',
        'preco': 10
    },
    {
        'id': 3,
        'nome': 'chá',
        'preco': 3.2
    },
    {
        'id': 4,
        'nome': 'croissant',
        'preco': 5.79
    }
]



# --- Lógica de Acesso aos Dados ---


def find_produto_by_id(item_id: int):
    """
    Busca um item no "banco de dados" pelo ID.
    """
    for item in menu:
        if item['id'] == item_id:
            return item
    return None

def find_produto_by_name(item_name: str):
    """
    Busca um item no "banco de dados" pelo Nome.
    """
    for item in menu:
        if item['nome'].lower() == item_name.lower():
            return item
    return None

def add_produto(item: dict):
    """
    Adiciona um novo item ao "banco de dados".
    """
    menu.append(item)
    return item

def remove_produto(item_id: int):
    """
    Remove um item do "banco de dados" pelo ID.
    """
    for index, item in enumerate(menu):
        if item['id'] == item_id:
            del menu[index]
            return True
    return False
