produtos=0
contador=0
nome=str(input('Informe seu nome:'))
print('Seja bem vindo(a), a sua lista de compras eletronica, {}!'.format(nome))
listafim=[]
valores=[]
resposta='Ss'
while True:
    produtos=str(input('Produto:')).upper()
    valor=float(input('Valor:'))
    if produtos =='SAIR':
        break
    contador += 1
    listafim.append(produtos)
    valores.append(valor)
print('compras: \n {}'.format(listafim))
print('valores: \n {}'.format(valores))
print('Sua lista possui {} produtos'.format(contador))
print('Até a proxima!')

