#  arquivo: adicionar.py
def adicionar(estoque, produto):
    # evita duplicidade no estoque
    if produto not in estoque:
        estoque.append(produto) #insere
    return estoque

# teste repido do modulo
if  __name__=="__main__":
    print (adicionar(["mouse"], "teclado"))