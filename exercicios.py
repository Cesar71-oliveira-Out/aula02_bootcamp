import math

print("Operação de soma no Python\n")

    # 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.
num1ad = int(input("Digite o primeiro número: "))
num2ad = int(input("Digite o segundo número: "))
soma = num1ad + num2ad

print(soma)
print("A soma é: ", soma)
print(f"O valor da soma {num1ad} + {num2ad} é: {soma}\n")  # Lembrar do f para as variáveis e deixar tudo dentro das ""

print("Resto da divisão de um número dividido por 5 no Python\n")

    # 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.
numero = int(input("Digite um número: "))
div = 5
resto = numero % div

print(resto)
print("O resto da divisão é: ", resto)
print(f"O resto da divisão do número por 5 de é: {resto}\n")

print("Operação de multiplicação no Python\n")

    # 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.
num1vs = int(input("Digite o primeiro número: "))
num2vs = int(input("Digite o segundo número: "))
resultadovs = num1vs * num2vs

print(resultadovs)
print("A multiplicação dos dois números é: ", resultadovs)
print(f"O valor da multiplicação de {num1vs} * {num2vs} é: {resultadovs}\n") # Lembrar do f para as vars e tudo dentro das ""

print("Operação de divisão inteira no Python\n")

    # 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.
num1dv = int(input("Digite o primeiro número: "))
num2dv = int(input("Digite o segundo número: "))
resultadodv = num1dv // num2dv

print(resultadodv)
print("O resultado da divisão é: ", resultadodv)
print(f"O valor da divisão de {num1dv} dividido por {num2dv} é: {resultadodv}\n") # Lembrar do f para as var e tudo dentro das ""

print("Calculando o quadrado de um número no Python\n")

    # 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.
numqd = int(input("Digite um número "))
quadrado = numqd ** 2

print(quadrado)
print("O quadrado é: ", quadrado)
print(f"O quadrado de {numqd} é: {quadrado}\n")

print("Operação soma de números float no Python\n")

    # 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
numfloa1 = float(input("Digite um número decimal: "))
numfloa2 = float(input("Digite mais um número decimal: "))
resultadofloa = numfloa1 + numfloa2

print(resultadofloa)
print("A somda dos números decimais é: ", resultadofloa)
print(f"A soma de {numfloa1} e {numfloa2} é: {resultadofloa}\n")

print("Cálculo da média no Python\n")

    # 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
numm1 = float(input("Digite um número: "))
numm2 = float(input("Digite mais um número: "))
resultadomedia = (numm1 + numm2) // 2

print(resultadomedia)
print("A média dos números é: ")
print(f"A Média de {numm1} e {numm2} é: {resultadomedia}\n")

print("Calculando a potência de um número no Python\n")

    # 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
numbase = float(input("Digite a base: "))
numexp = float(input("Digite expoente: "))
potencia = numbase ** numexp

print(potencia)
print("O resultado é: ", potencia)
print(f"A potência de {numbase} elevado a {numexp} é: {potencia}\n")

print("Convertendo temperatura de Celsius para Fahrenheit no Python\n")

    # 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32

print(fahrenheit)
print("A temperatura convertida para Fahrenheit é: ", fahrenheit)
print(f"{celsius}°C é igual a {fahrenheit}°F\n")

print("Calculando a área de um círculo com base no raios no Python\n")

    # 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
raio = float(input("Digite o raio do círculo: "))
CONSTANTE_PI = 3.14159
areadocirculo = CONSTANTE_PI * raio ** 2

print(areadocirculo)
print("A área do círculo é: ", areadocirculo)
print(f"A área de um círculo com raio de {raio} é {areadocirculo}\n")

        # 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
        # Ou pode usar o método math, com o import math, conforme o código abaixo.
raio = float(input("Digite o raio do círculo: "))
areadocirculo = math.pi * raio ** 2
print(f"A área do círculo é: {areadocirculo:.2f}\n") # :.2f é usado para definir a quantidade de números após a vírgula

