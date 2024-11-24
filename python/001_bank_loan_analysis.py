# A program to check if the loan is going to be approved or not.
#
name = str(input("Qual o seu nome? "))
print("Prazer em te conhecer, {}!".format(name))
valor = input("Qual o valor do imóvel que você quer financiar? R$ ")
salario = input(("Qual a sua renda mensal? R$ "))
prazo = int(input("Em quantos anos você gostaria de financiar? "))
parcela = float(valor)/float(prazo)/12

if parcela >float(salario)*0.3:
    print("Sentimos muito mas seu financiamento não foi aprovado.")
else:
    print("APROVADO! O valor da sua prestação será de {:.2f}".format(parcela))
