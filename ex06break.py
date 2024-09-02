soma = cont = 0

while True:
    num = input('Digite um número inteiro (ou digite X para parar): ')
    if num in str('Xx'):
        break
    else:
        soma += int(num)
        cont += 1
print(f'Você digitou {cont} números e a soma foi {soma}')