#gestion de productos que estaran en la DB

class Producto:
    def __init__(self,nombrePrdoucto,categoria,precio,cantidad,):
        self.nombreProducto = nombrePrdoucto
        self.categoria = categoria
        self.precio = precio
        self.cantidad = cantidad

#configuracion con la base de datos PostgreSQL