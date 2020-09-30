
listaRegistro = []
clientes = 1
continuar = "si"
Total = 0

while continuar == "si":
    cliente = input("Nombre del cliente: ")
    producto = input("Producto: ")
    costo = float(input("Costo (en dolares ): "))

    registro = dict(
        numClientes=clientes, cliente=cliente, producto=producto, costo=costo
    )
    
    listaRegistro.append(registro)

    clientes += 1
    Total += registro["costo"]
    continuar = input("¿Quiere agregar más productos? si/no")

for registro in listaRegistro:
    print(registro)
print("El costo total es de " + str(Total) + " dolares")