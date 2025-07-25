import math

# Teste do GIT

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

    # 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
        # Dá pra fazer de duas formas, com uma outra variável ou impriminto direto a variável.upper()
texto = str(input("Digite uma palavra: "))
print(texto.upper())

texto_upper = texto.upper()
print(texto_upper)

    # 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
nome_completo = str(input("Digite seu nome completo: "))
print(nome_completo.lower())

nome_completo_min = nome_completo.lower()
print("Nome completo em minúsculas: ", nome_completo_min)

    # 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços 
    # em branco no início e no final.
frase = str(input("Digite uma frase: "))
print(frase.strip())

frase_sem_espaco = frase.strip()
print(frase_sem_espaco)

    # 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, 
    # imprima o dia, o mês e o ano separadamente.
data_ddmmaa = (input("Digite uma data no formato dd/mm/aaaa: "))
dia, mes, ano = data_ddmmaa.split("/")
print("Dia: ", dia)   # Aqui é um exemplo de impressão de variável após ums string, coloca a vírgula para separar
print("Mês: ", mes)
print("Ano: ", ano)

    # 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
    # Imprimi de duas formas
nome = str(input("Digite seu nome: "))
sobrenome = str(input("Digite seu sobrenome: "))

print(nome + "", sobrenome)  # Aqui depois do espaço "", coloca a virgula para imprimir a segunda variável
print(f"{nome} {sobrenome}")

    # 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne 
    # o resultado da operação AND entre elas.
valor1 = bool(input("Digite um valor, True or False: " ) == 'True')
valor2 = bool(input("Digite um valor, True or False: ") == 'True')

result_and =  valor1 and valor2
print(result_and)

# Exemplo de entrada
valor1 = False
valor2 = True
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)

    # 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
valor1or = bool(input("Digite um valor, True or False: " ) == 'True')
valor2or = bool(input("Digite um valor, True or False: ") == 'True')

result_or =  valor1or or valor2or
print(result_or)

# Exemplo de entrada
valor1or = False
valor2or = True
resultado_or = valor1or or valor2or
print("Resultado do AND lógico:", resultado_or)

    # 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
        # No input, .lower(): Converte a string digitada para minúsculas (ex: "True" vira "true", "FALSE" vira "false").
        # == 'true': Compara a string em minúsculas com a string 'true'. Se forem iguais, o resultado é True, 
        # caso contrário, é False. 
valor1 = (input("Digite um valor: ").lower() == 'true')
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)

    # 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
compare1 = input("Digite uma palavra ou número: ")
compare2 = input("Digite outra palavra ou número: ")
compara = compare1 == compare2

print ("Note: Se True entradas são iguais, senão, são diferentes\n")
print(compara)

    # 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
compare1dif = input("Digite uma palavra ou número: ")
compare2dif = input("Digite outra palavra ou número: ")
compara_dif = compare1dif != compare2dif

print ("Note: Se True entradas são DIFERENTES, senão, são IGUAIS\n")
print(compara_dif)

    # 21: Conversor de Temperatura
while True:  # Inicia um loop infinito
    try:
        celsius = float(input("Digite a temperatura em Celsius: "))
        # Se a linha acima não der erro, o código continua aqui
        fahrenheit = (celsius * 9/5) + 32
        print(f"{celsius}°C é igual a {fahrenheit}°F.")
        break  # Sai do loop se a entrada for válida
    except ValueError:
        # Se um ValueError ocorrer (entrada não numérica), este bloco é executado
        print("Entrada inválida. Por favor, digite um NÚMERO para a temperatura.")
        # O loop continua automaticamente, pedindo a entrada novamente
