# Crie um programa que leia a idade e o sexo de várias pessoas.
# A cada pessoa cadastrada, o programa deverá perguntar se o
# usuário quer ou não continuar. No final, mostre:
# A) quantas pessoas têm mais de 18 anos
# B) quantos homens foram cadastrados
# C) quantas mulheres têm menos de 20 anos

maioresIdade = 0
quantHomens = 0
mulheresMenos20 = 0

while True:
    # inputs
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    # requisitos
    # a
    if idade >= 18:
        maioresIdade += 1

    # c
    if sexo == 'M':
        quantHomens += 1

    # c
    if sexo == 'F' and idade < 20:
        mulheresMenos20 += 1

    # continuar
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if resp in 'Nn':
        break

# saída de dados
print(f'Total de pessoas maiores de 18 anos: {maioresIdade}')
print(f'Total de homens: {quantHomens}')
print(f'Total de mulheres menores de 20 anos: {mulheresMenos20}')