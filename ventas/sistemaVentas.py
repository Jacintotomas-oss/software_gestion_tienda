import tkinter as tk
from tkinter import messagebox
from inventario.productos import productos 
#modulo 1 para software de una tienda 
#en este modulo se manejaran las ventas de los productos 
# los productos estan en una base de datos en SQL server 

#se importo la clase productos del modulo productos
#clase venta 
class Venta:
    def __init__(self, producto, cantidad,precio_unitario,categoria):
        self.producto = producto 
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.categoria = categoria
    
    
#seccion de atencion al cliente

def regitrarVenta (producto,cantidad,precio_unitario,categoria):
    #funcion para registrar una venta
    Venta = Venta(producto,cantidad,precio_unitario,categoria)
    
    
    
#cancelar venta


    


