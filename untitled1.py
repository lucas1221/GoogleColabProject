# -*- coding: utf-8 -*-
"""Untitled1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lKL-TtOWAlIF7PGilYLBSjPgwy065lez
"""

matriz = [[1,2,3],[4,5,6],[7,8,9]]
m = 3
n = 3
def calculosMatriz(matriz, m, n): 
  media = 0
  somaMaiorMedia = 0
  impar = 0
  ij = m * n
  maiorMenor = 0
  quantidadeMaior = 0
  maior = matriz[0][0]
  menor = matriz[0][0]
  contador = 0
  #for para percorrer as linhas
  for i in range(m):
    #for para percorrer as colunas
    for j in range(n):
      media = media + matriz[i][j]
  media = media / ij

  for i in range(m):
    for j in range(n):
      if matriz[i][j] > media:
        somaMaiorMedia = somaMaiorMedia + matriz[i][j]

  for i in range(m):
    for j in range(n):
      if (matriz[i][j] % 2) == 1:
        impar = impar + matriz[i][j]

  for i in range(m):
    for j in range(n):
      if matriz[i][j] > maior:
        maior = matriz[i][j]

  for i in range(m):
    for j in range(n):
      if matriz[i][j] < menor:
        menor = matriz[i][j]

  maiorMenor = maior - menor

  for i in range(m):
    for j in range(n):
      if matriz[i][j] > maiorMenor:
        contador = contador + 1
 
  print("SOMA DOS VALORES ÍMPARES DA MATRIZ")
  print(impar)
  print("SOMA DOS VALORES MAIORES QUE A MÉDIA")
  print(somaMaiorMedia)
  print("QUANTIDADE DE VALORES MAIORES DO QUE A SUBTRAÇÃO DO MAIOR PELO MENOR")
  print(contador)

calculosMatriz(matriz, m, n)

lis[10]

lis[15] = 1

print(lis)

matriz = [[0,0,0,1], [0,0,0,2], [0,0,0,3]]
def linhaMaiorSomaMatriz(matriz):
  linha = 0
  coluna = 0
  maior = 0
  soma = 0
  soma2 = 0
  soma3 = 0
  vetorSoma = []
  for 0 in range(3):
    for j in range(3):
        soma = soma + matriz[0][j]
  for 1 in range(3):
    for j in range(3):
        soma2 = soma2 + matriz[1][j]
  for 2 in range(3):
    for j in range(3):
        soma3 = soma3 + matriz[2][j]   

  vetorSoma[0] = soma
  vetorSoma[1] = soma2
  vetorSoma[2] = soma3
  
  print(matriz)
  print("O maior elemento está localizado em")
  print(linha, coluna)
localizaMaior(matriz)

def linhaMaiorSomaMatriz(matriz):
    lista = []
    linha = 0
    while linha < 3:
        coluna = 0
        soma = 0
        while coluna < 3:
            soma = soma + matriz[linha][coluna]
            coluna = coluna + 1
        lista.append(soma)
        linha = linha + 1

    cont = 0
    maior = lista[0]
    posicao = 0
    while cont < 3:
        if lista[cont]>maior:
            maior = lista[cont]
            posicao = cont
        cont = cont + 1

    print(matriz)
    print('A linha de maior soma é de número:', posicao)
    print('A maior soma é:', maior)

matriz = [[1,2,3],[4,5,6],[7,8,9]]
linhaMaiorSomaMatriz(matriz)

vetor = [1,2,3,4,5]

def verificaParImpar(vetor):
  par = []
  impar = []
  for i in range(len(vetor)):
    if vetor[i] % 2 == 0:
      par.append(vetor[i])
    else:
      impar.append(vetor[i])
  print("VETOR ORIGINAL")
  print(vetor)
  print("VETOR PAR")
  print(par)
  print("VETOR IMPAR")
  print(impar)

verificaParImpar(vetor)