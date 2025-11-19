#corazon del sistema 
#importacion para la interfaz grafica
import tkinter as tk
from tkinter import messagebox

#1.importacion de modulos
from ventas.sistemaVentas import Venta
from inventario.productos import productos

#2.logica del programa y menu 

#menu principal
def menu ():
    print("ingrese el producto ")
    producto = input()
    
#configuracion con la base de datos y conexion 


if __name__ == "__main__":
    menu()