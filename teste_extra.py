final_arquivo = False
string_vazia = ''
lista=[]
total=0

meu_arquivo = open('itens_pedido.txt', 'r')

while not final_arquivo: 
    linha = meu_arquivo.readline().rstrip()   
    if linha == string_vazia:
        final_arquivo = True        
    else:
        info_ex1 = linha.split(':')
        qtd = info_ex1[0]
        preco = info_ex1[1]
        produto = info_ex1[2]
        teste=int(qtd)*int(preco)
        total+=teste
        print("Produto:",produto," - Subtotal: R$ ",teste)


print("Total do pedido: R$ ",total)

meu_arquivo.close()
