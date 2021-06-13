inventario = []
resposta = "S"
while resposta == "S":
    inventario.append(input("Equipamento: "))
    inventario.append(float(input("Valor: ")))
    inventario.append(int(input("Numero Serial: ")))
    inventario.append(input("Departamento: "))
    resposta = input("Digite \"S\" para continuar: ").strip().upper()

for elemento in range(0, len(inventario)):
    print(inventario[elemento])
