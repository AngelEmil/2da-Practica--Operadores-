# 3-- Pedir peso y altura para calcular la masa corporal: mc = peso / altura^2.

P = int(input("digite su Peso en Kilogramos "))
A = int (input("digite su Altura en metros "))

mc = P / A ** 2

print("Su masa corporal es", mc)