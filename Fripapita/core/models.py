from django.db import models 
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ForeignKey
# Create your models here.


class Rol(models.Model):
    idTipo=models.AutoField(primary_key=True,verbose_name='id del tipo de usuario')
    descripcion=models.CharField(max_length=50,verbose_name='descripcion del tipo de usuario')

    def __str__(self):
        return self.descripcion

class Categoria(models.Model):
    idCat = models.AutoField(primary_key=True,verbose_name='id de categoria')
    nombreCat =models.CharField(max_length=100,verbose_name='nombre de categoria')

    def __str__(self) -> str:
        return self.nombreCat

class Producto(models.Model):
    idProducto = models.AutoField( primary_key =True ,verbose_name='id producto')
    nombreProducto = models.CharField(max_length= 100, verbose_name='nombre de producto',null= True )
    stock= models.IntegerField(verbose_name='cantidad de stock')
    precio= models.IntegerField(verbose_name='precio del producto')
    desc= models.CharField(max_length=2000,verbose_name='descripcion del producto')
    foto = models.ImageField(upload_to="fotos",verbose_name="Foto del producto", null = True)
    categoria = models.ForeignKey(Categoria,on_delete=CASCADE)
    
    def __str__(self):
        return self.nombreProducto

class Usuario(models.Model):
    rut= models.CharField(primary_key= True,max_length=15, verbose_name='rut de ususario')
    nombre= models.CharField(max_length=50,null=True, verbose_name='nombre ')
    telefono=models.CharField(max_length=15,verbose_name='telefono',null=True)
    contrasenia= models.CharField(max_length=16,null=True,verbose_name='contraseña de usuario')
    mail= models.CharField(max_length=30,null=True,verbose_name='mail de usuario')
    direccion= models.CharField(max_length=30,verbose_name="direccion",null=True)
    rol=models.ForeignKey(Rol,on_delete=CASCADE)
    
    def __str__(self):
        return self.nombre


class Venta(models.Model):
    idVenta = models.AutoField(primary_key=True, verbose_name='id de venta')
    fechaVenta = models.DateField(verbose_name='fecha de la venta')
    totalVenta= models.IntegerField(verbose_name='total de la venta')
    estadoVenta = models.CharField(max_length=40,verbose_name='estado de la venta')
    tipoPago = models.CharField(max_length=40, verbose_name='tipo de pago')
    usuario = models.ForeignKey(Usuario, on_delete=CASCADE)
    
    def __Str__(self):
        return self.estadoVenta

class Carrito(models.Model):
    idCarrito=models.AutoField(primary_key=True,verbose_name='id de carrito')
    cantidad=models.IntegerField(verbose_name='cantidad de productos en carrito')
    subTotal=models.IntegerField(verbose_name='total del carrito')
    producto=models.ForeignKey(Producto, on_delete=CASCADE)
    usuario=models.ForeignKey(Usuario,on_delete=CASCADE)
