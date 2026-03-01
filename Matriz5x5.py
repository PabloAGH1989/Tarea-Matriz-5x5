
Matriz = [ [0 for _ in range(5)] for _ in range(5)]
for i in range (5):
    for j in range (5):
        Valor = int (input(f"Ingrese el valor para la posición[{i}][{j}]:"))
        Matriz [i][j]= Valor
print("    Matriz Ingresada:  ")
for i in range (5):
    for j in range (5):
        print (Matriz[i][j], end = " ")
    print()
