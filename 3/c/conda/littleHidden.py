#1
n1 = int(input("Digite n1: "))
n2 = int(input("Digite n2: "))
if n1 > n2:
    print(n1)
else:
    print(n2)

#2
n = int(input("Digite n: "))
if n > 0:
    print("Positivo")
else:
    print("Negativo")

#3
letra = input("Digite letra: ")
if letra == "F" or letra == "f":
    print("Feminino")
elif letra == "M" or letra == "m":
    print("Masculino")
else:
    print("Invalido")

#4
a = input("Digite letra: ")
if len(a) == 1:
    if(a == "a" or a == "e" or  a == "i" or a == "o" or a == "u"  or a == "A" or "E" or a == "I" or a == "O" or a == "U"):
        print("Vogal")
    else: 
        print("Consoante")
else:
    print("Letra invalida")

#5
note1 = float(input("Digite nota1: "))
note2 = float(input("Digite nota2: "))
media = (note1 + note2) / 2
if media >= 7 and media <= 9:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com distinção")

#6
n1 = int(input("Digite N1: "))
n2 = int(input("Digite N2: "))
n3 = int(input("Digite N3: "))

array = []

array.append(n1)
array.append(n2)
array.append(n3)

array.sort(reverse=True)

print(array[0])

#7
n1 = int(input("Digite N1: "))
n2 = int(input("Digite N2: "))
n3 = int(input("Digite N3: "))

array = []

array.append(n1)
array.append(n2)
array.append(n3)

array.sort(reverse=True)

print(array[0])
print(array[len(array)-1])

#8
n1 = int(input("Digite N1: "))
n2 = int(input("Digite N2: "))
n3 = int(input("Digite N3: "))

array = []

array.append(n1)
array.append(n2)
array.append(n3)

array.sort(reverse=False)

print(array[0])

#9
n1 = int(input("Digite N1: "))
n2 = int(input("Digite N2: "))
n3 = int(input("Digite N3: "))

array = []

array.append(n1)
array.append(n2)
array.append(n3)

array.sort(reverse=True)

for element in array:
    print(element)

#10
periodo = input("Digite o Periodo(M/V/N): ")

if periodo == "M":
    print("Matutino")
elif periodo == "V":
    print("Vespertino")
elif periodo == "N":
    print("Noturno")
else:
    print("Periodo Invalido!")

#11
salario = float(input("Digite o salário: "))

if salario <= 280:
    porcentage = 20
elif salario <= 700:
    porcentage = 15
elif salario <= 1500:
    porcentage = 10
else:
    porcentage = 5

aumento = salario * (porcentage / 100)
novo_salario = salario + aumento

print(salario)
print(porcentage)
print(aumento)
print(novo_salario)

#12
valorH = float(input("Digite o valor da hora: "))
horas = float(input("Digite a quantidade de horas: "))

salario = valorH * horas

if salario <= 900:
    ir = 0
elif salario <= 1500:
    ir = 5
elif salario <= 2500:
    ir = 10
else:
    ir = 20

ir = (ir / 100) * salario
sindi = 0.03 * salario
fgts = 0.11 * salario

dTotal = ir + sindi + fgts

liquid = salario - dTotal

print(salario)
print(ir)
print(sindi)
print(fgts)
print(dTotal)
print(liquid)

#13
dia = int(input("Digite dia: "))

if dia == 1:
    print("Domingo")
elif dia == 2:
    print("Segunda")
elif dia == 3:
    print("Terça")
elif dia == 4:
    print("Quarta")
elif dia == 5:
    print("Quinta")
elif dia == 6:
    print("Sexta")
elif dia == 7:
    print("Sabado")
else:
    print("Dia invalido")

#14
n1 = float(input("Digite n1: "))
n2 = float(input("Digite n2: "))

media = (n1 + n2) / 2

if media >= 9:
    conceito = "A"
elif media >= 7.5 and media < 9:
    conceito = "B"
elif media >= 6 and media < 7.5:
    conceito = "C"
elif media >= 4 and media < 6:
    conceito = "D"
elif media >= 0 and media < 4:
    conceito = "E"

print(n1)
print(n2)
print(media)
print(conceito)

if conceito == "A" or conceito == "B" or conceito == "C":
    print("Aprovado")
else:
    print("Reprovado")

#15
l1 = float(input("Digite l1: "))
l2 = float(input("Digite l2: "))
l3 = float(input("Digite l3: "))

if l1 + l2 > l3 and l1 + l3 > l2 and l2 + l3 > l1:
    print("Formam triangulo")
    
    if l1 == l2 == l3:
        print("Equilátero.")
    elif l1 == l2 or l1 == l3 or l2 == l3:
        print("Isósceles.")
    else:
        print("Escaleno.")
else:
    print("Não formam triângulo")

#16
import math

a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

if a == 0:
    print("Não é de segundo grau")
else:
    delta = b ** 2 - 4 * a * c
    
    if delta < 0:
        print("Sem raizes reais")
    elif delta == 0:
        raiz = -b / (2 * a)
        print(raiz)
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        print(raiz1)
        print(raiz2)

#17
ano = int(input("Digite um ano: "))
if ano % 4 == 0:
    print("Bissexto")
else:
    print("Não bissexto")

#18
from datetime import datetime

data = input("Digite uma data: ")

try:
    dataV = datetime.strptime(data, "%d/%m/%Y")
    print("Data Valida")
except ValueError:
    print("Data Invalida")

#19
numero = int(input("Digite um número: "))

if numero >= 1000:
    print("Tem que ser abaixo de 1000")
else:
    centenas = numero // 100
    dezenas = (numero % 100) // 10
    unidades = numero % 10

    descricao = ""
    if centenas > 0:
        descricao += f"{centenas} centena{'s' if centenas > 1 else ''}"
        if dezenas > 0 or unidades > 0:
            descricao += ", "
    if dezenas > 0:
        descricao += f"{dezenas} dezena{'s' if dezenas > 1 else ''}"
        if unidades > 0:
            descricao += " e "
    if unidades > 0 or (centenas == 0 and dezenas == 0):
        descricao += f"{unidades} unidade{'s' if unidades > 1 else ''}"

    print(f"{numero} = {descricao}")

#20
note1 = float(input("Digite nota1: "))
note2 = float(input("Digite nota2: "))
note3 = float(input("Digite nota3: "))

media = (note1 + note2 + note3) / 3
if media >= 7 and media <= 9:
    print("Aprovado")
elif media < 7:
    print("Reprovado")
elif media == 10:
    print("Aprovado com distinção")

#21
while True:
    valor_saque = int(input("Digite o valor do saque: "))
    if 10 <= valor_saque <= 600:
        break
    else:
        print("deve ser maior que 10 e menor que 600")

notas_100 = valor_saque // 100
resto = valor_saque % 100

notas_50 = resto // 50
resto = resto % 50

notas_10 = resto // 10
resto = resto % 10

notas_5 = resto // 5
resto = resto % 5

notas_1 = resto

if notas_100 > 0:
    print(f"{notas_100} nota{'s' if notas_100 > 1 else ''} de 100 reais")
if notas_50 > 0:
    print(f"{notas_50} nota{'s' if notas_50 > 1 else ''} de 50 reais")
if notas_10 > 0:
    print(f"{notas_10} nota{'s' if notas_10 > 1 else ''} de 10 reais")
if notas_5 > 0:
    print(f"{notas_5} nota{'s' if notas_5 > 1 else ''} de 5 reais")
if notas_1 > 0:
    print(f"{notas_1} nota{'s' if notas_1 > 1 else ''} de 1 real")

#22
n = int(input("Digite n: "))
if n % 2 == 0:
    print("par")
else:
    print("impar")

#23
n = float(input("Digite n: "))

if n == int(n) and n == round(n):
    print("Inteiro")
else:
    print("Decimal")

#24
n1 = float(input("Digite n1: "))
n2 = float(input("Digite n2: "))

op = input("Digite a op: ")

if op == "+":
    resultado = n1 + n2
elif op == "-":
    resultado = n1 - n2
elif op == "*":
    resultado = n1 * n2
elif op == "/":
    resultado = n1 / n2
else:
    print("Operação inválida.")

parImp = "par" if resultado % 2 == 0 else "ímpar"

posNeg = "positivo" if resultado > 0 else "negativo"

intDec = "inteiro" if resultado == int(resultado) else "decimal"

print(resultado)
print(parImp)
print(posNeg)
print(intDec)

#25
cont = 0

p1 = input("Telefonou para a vítima? (sim ou não): ").lower()
if p1 == "sim":
    cont += 1

p2 = input("Esteve no local do crime? (sim ou não): ").lower()
if p2 == "sim":
    cont += 1

p3 = input("Mora perto da vítima? (sim ou não): ").lower()
if p3 == "sim":
    cont += 1

p4 = input("Devia para a vítima? (sim ou não): ").lower()
if p4 == "sim":
    cont += 1

p5 = input("Já trabalhou com a vítima? (sim ou não): ").lower()
if p5 == "sim":
    cont += 1

if cont == 2:
    print("Suspeito")
elif cont >= 3 and cont <= 4:
    print("Cúmplice")
elif cont == 5:
    print("Assassino")
else:
    print("Inocente")

#26
litros = float(input("Digite os litros: "))
tipo = input("Digite o tipo: ").upper()

precoA = 1.90 
precoG = 2.50  

if tipo == "A":
    if litros <= 20:
        valor_total = litros * (precoA - (0.03 * precoA))
    else:
        valor_total = litros * (precoA - (0.05 * precoA))
elif tipo == "G":
    if litros <= 20:
        valor_total = litros * (precoG - (0.04 * precoG))
    else:
        valor_total = litros * (precoG - (0.06 * precoG))
else:
    print("tipo invalido")

print(valor_total)

#27
qMo = float(input("Digite o Kg do morango: "))
qMa = float(input("Digite o Kg da maçã: "))

precoMorango = 2.50  
precoMorangoAcima = 2.20
precoMaca = 1.80  
precoMacaAcima = 1.50  

if qMo <= 5:
    valorMo = qMo * precoMorango
else:
    valorMo = qMo * precoMorangoAcima

if qMa <= 5:
    valorMa = qMa * precoMaca
else:
    valorMa = qMa * precoMacaAcima

total = valorMo + valorMa

if qMo + qMa > 8 or total > 25.00:
    total *= 0.9  

print(total)

#28
tipo = input("Digite o tipo: (File Duplo, Alcatra ou Picanha): ").capitalize()
quantidade = float(input("Digite o Kg da carne:  "))

precoFduplo = 4.90
precoFduploA = 5.80
precoAlcatra = 5.90
precoAlcatraA = 6.80
precoPicanha = 6.90
precoPicanhaA = 7.80

if quantidade <= 5:
    if tipo == "File Duplo":
        total = quantidade * precoFduplo
    elif tipo == "Alcatra":
        total = quantidade * precoAlcatra
    elif tipo == "Picanha":
        total = quantidade * precoPicanha
    else:
        print("Tipo invalido")

else:
    if tipo == "File Duplo":
        total = quantidade * precoFduploA
    elif tipo == "Alcatra":
        total = quantidade * precoAlcatraA
    elif tipo == "Picanha":
        total = quantidade * precoPicanhaA
    else:
        print("Tipo inválido")

tipoPagamento = input("Digite o tipo de pagamento: ").capitalize()

desconto = 0
if tipoPagamento == "Cartão Tabajara":
    desconto = total * 0.05

pagar = total - desconto

print(tipo)
print(quantidade)
print(total)
print(tipoPagamento)
print(desconto)
print(pagar)