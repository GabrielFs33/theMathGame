import random
result = 0
n1 = random.randint(0,9)
n2 = random.randint(0,9)
operador = ["+","-","*","/"]
opEsc=random.choice(operador)

if opEsc == "+":
    result = n1 + n2
elif opEsc == "-":
    result = n1 - n2
elif opEsc == "*":
    result = n1 * n2
else:
    result = n1 / n2

print(n1,"?",n2,"=",result)
resposta=input("Qual o operador ?")
#configuração para resposta 
if resposta == opEsc:
    print("Parabéns você acertou!")
else:
    print("Infelizmente você errou!")

