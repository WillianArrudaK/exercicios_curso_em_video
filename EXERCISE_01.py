# exercise 001

print("hello world")


# exercise 002

nome = input("qual o seu nome? ")
print("E um prazer te conhecer {}".format(nome))


# exercise 003

n1 = int(input("Digite um numero ->  "))
n2 = int(input("Digite outro numero ->  "))

print("a soma entre {} e {}, e igual a {}".format(n1, n2, (n1 + n2)))


# exercise 004

algo = input('Digite algo:  ')

print("seu tipo primitivo:  ", type(algo))
print('so tem espacos:  ', algo.isspace())
print('e um numero:  ', algo.isnumeric())
print('e alfabetico:  ', algo.isalpha())
print('e alfanumerico:  ', algo.isalnum())
print('esta em maiusculas:  ', algo.isupper())
print('esta em minusculas:  ', algo.islower())
print('esta capitalizada:  ', algo.istitle())


# exercise 005

ant = int(input('Digite um numero->  '))
print('o numero {}, tem como antecessor o numero {} e sucessor o numero {}'.format(ant, ant - 1, ant + 1))


# exercise 006

from math import sqrt

algoritimo = int(input('Digite um numero ->  '))

print('Seu dobro: {}  / Seu triplo: {} / Sua raiz quadrada: {:.0f} '.format(algoritimo*2, algoritimo*3, sqrt(algoritimo)))


# exercise 007

def menu2():
    
    nota = float(input('Digite sua primeira nota:  '))
    nota2 = float(input('Digite sua segunda nota:  '))

    if nota < 0:
        print(10 * '=')
        print('\nvalores invalidos!\n')
        print(10 * '=')
        return menu2()
    elif nota > 10:
        print(10 * '=')
        print('\nvalores invalidos!\n')
        print(10 * '=')
        return menu2()
    elif nota2 < 0:
        print(10 * '=')
        print('\nvalores invalidos!\n')
        print(10 * '=')
        return menu2()
    elif nota2 > 10:
        print(10 * '=')
        print('\nvalores invalidos!\n')
        print(10 * '=')
        return menu2() 
    else:
        media = (nota + nota2) / 2
        print(10 * '=')
        print('\nSua media ficou em: {}\n'.format(media))
        media_arred = round(media)
        print(10 * '=')
        print('\nSua media arredondada ficou: {}\n'.format(media_arred))

# se a media for igual ou maior que sete, esta a aprovado

    if media_arred >= 7:
        print(10 * '=')
        print('\nSituacao: Aprovado\n')
        print(10 * '=')
    else:
        print(10 * '=')
        print('\nSituacao: Reprovado\n')
        print(10 * '=')

menu2()


# exercise 008

nm = float(input('Insira um valor em metros ->  '))

nm_cm = nm * 100
nm_mm = nm * 1000

print('O valor digitado, em centimetros vale {} e em milimetros vale {}'.format(nm_cm, nm_mm))



# exercise 009 - tabuada sem usar o for

tabuada = int(input('Digite um numero para ver sua tabuada:  '))

print(10 * '-')
print('\n{} x {:2} = {}'.format(tabuada, 1, tabuada*1))
print('{} x {:2} = {}'.format(tabuada, 2, tabuada*2))
print('{} x {:2} = {}'.format(tabuada, 3, tabuada*3))
print('{} x {:2} = {}'.format(tabuada, 4, tabuada*4))
print('{} x {:2} = {}'.format(tabuada, 5, tabuada*5))
print('{} x {:2} = {}'.format(tabuada, 6, tabuada*6))
print('{} x {:2} = {}'.format(tabuada, 7, tabuada*7))
print('{} x {:2} = {}'.format(tabuada, 8, tabuada*8))
print('{} x {:2} = {}'.format(tabuada, 9, tabuada*9))
print('{} x {:2} = {}\n'.format(tabuada, 10, tabuada*10))
print(10 * '-')


# exercise 010

import requests

cart = float(input('Quanto de dinheiro voce tem na carteira? ->  '))

def pegar_cotacoes():
    requisicao = requests.get('http://economia.awesomeapi.com.br/json/last/USD-BRL')

    requisicao_dic = requisicao.json()

    dolar_req = float(requisicao_dic['USDBRL']['bid'])

    convertido = cart / dolar_req

    print(10 * '-')
    print("\nO valor atual do dolar esta em: R$ {:.2f}".format(dolar_req))
    print("Com R$ {:.2f} voce pode comprar U$ {:.2f}\n".format(cart, convertido))
    print(10 * '-')

pegar_cotacoes()


# exercise 011

larg_parede = float(input('Qual a largura da sua parede?  '))
alt_parede = float(input('Qual a altura da sua parede?  '))

area = larg_parede * alt_parede
tinta_total = area / 2

print('Sua parede tem {} metros quadrados, e sera necessario utilizar {} litros de tinta para pintar essa area total.'.format(area, tinta_total))


# exercise 012

preco_antigo = float(input('Digite o preco atual do seu produto: R$ '))
novo_preco = preco_antigo - (preco_antigo * 0.05)

print('O produto custava R$ {:.2f}, e com o reajuste de 5%, seu novo preco ficou em R$ {:.2f}'.format(preco_antigo, novo_preco))


# exercise 015
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

def menu():
    
    km = float(input('Quilometragem percorrida ->  '))
    dias = int(input('Dias ficados com o carro ->  '))

    if km <= 0 or dias <= 0:
        print('valor invalido')
        menu()

    else:
        valor = ((60 * dias) + (km * 0.15))
        print('Valor a pagar: R$ {:.2f}'.format(valor))

menu()
