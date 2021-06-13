equipamentos= []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(float(input("Valor: ")))
    seriais.append(int(input("Número Serial: ")))
    departamentos.append(input("Departamento: "))
    resposta = input("Digite \"S\"para continuar: ").strip().upper()
for indice in range(0, len(equipamentos)):
    print("\nEquipamento..: ", (indice+1))
    print("Nome...........: ", equipamentos[indice])
    print("Valor..........: ", valores[indice])
    print("Serais.........: ", seriais[indice])
    print("Departamento...: ", departamentos[indice])
    print("=" * 20)
busca = input("\nDigite o nome do equipamento que deseja buscar: ")
for indice in range(0, len(equipamentos)):
    if busca == equipamentos[indice]:
        print('Valor...:', valores[indice])
        print('Serial..:', seriais[indice])

despreciacao = input("Digite o nome do equipamento que será depreciado: ")
for indice in range(0, len(equipamentos)):
    if despreciacao == equipamentos[indice]:
        print("O valor atual do indice é ", valores[indice])
        valores[indice] = valores[indice] * 0.9
        print(f"O novo valor é ", valores[indice])
serial = int(input("Digite o serial a ser excluido: "))
for i in range(0, len(seriais)):
    if serial == seriais[i]:
        print('Equipamento encontrado será deletado!!')
        del equipamentos[i]
        del valores[i]
        del seriais[i]
        del departamentos[i]
        break
for indice in range(0, len(equipamentos)):
    print("\nEquipamento..: ", (indice+1))
    print("Nome...........: ", equipamentos[indice])
    print("Valor..........: ", valores[indice])
    print("Serais.........: ", seriais[indice])
    print("Departamento...: ", departamentos[indice])
    print("=" * 20)
