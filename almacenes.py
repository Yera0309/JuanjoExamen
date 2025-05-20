#ALMACENES EL PELUCHITO
#Gestion de inventario en python

#almacenar informacion de varios productos
#PRODUCTO:
#ID
#NOMBRE
#PRECIO AL DETAL
#PRECIO POR MAYOR
#DESCRPCION
#CANTIDAD BODEGA

#(1. AGREGAR UN PRODUCTO, 2 VER LOS PRODUCTOS 3.SALIR)

opcion=None

print("ALMACENES PELUCHITOS")
print("1. Digita nombre del producto")
print("2. agregar otro producto")
print("3. SALIR")

listaProducto=[]
while opcion != 3:
    tarea={}
    opcion=int(input("Digita una opcion por favor: "))
    if opcion == 1:
       print("Tomamndo el pedido")
       tarea['id']=input("Digata el id del producto: ")
       tarea['Nombre']=input("Digita el nombre del pedido: ")
       tarea['descripcion']=input("Digita una descripcion: ")
       tarea['PrecioDetal']=input("Digita precio detal: ")
       tarea['PrecioPorMayor']=input("Digita precio por mayor: ")
       tarea['cantidadBodega']=input("¿cuantos hay en bodega?: ")
       
       listaProducto.append(tarea)
    elif opcion == 2:
       print("Agregar otro producto")
       print(listaProducto)
    elif opcion == 3:
        print("saliendo")
        break
    else:
        print("Opcion invalida")