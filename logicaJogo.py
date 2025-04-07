import random
result = 0
n1 = random.randint(0,9)
n2 = random.randint(0,9)
operador = ["+","-","*","/"]
opEsc=random.choice(operador)
print(opEsc)
if opEsc == "+":
    result = n1 + n2
elif opEsc == "-":
    result = n1 - n2
elif opEsc == "*":
    result = n1 * n2
else:
    result = n1 / n2

print(n1,opEsc,n2,"=",result)
