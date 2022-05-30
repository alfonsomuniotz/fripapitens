from django.shortcuts import redirect, render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Usuario,Rol
from django.contrib.auth.models import User


def home(request):
    return render(request,'core/home.html')
    
def registro(request):
    
    return render(request,'core/registro.html')

def forgetpassword(request):
    return render(request,'core/forgetpassword.html')

def log(request):
    return render(request,'core/log.html')

# Create your views here.
def listadousuario(request):
    usuario = Usuario.objects.all()
    contexto ={"usuario":usuario}
    return render(request, 'OTY/listadousuario.html',contexto)
#registrar usuario

def registrar_usuario(request):
    nombre_g=request.POST['username']
    rut_g= request.POST['Rut']
    telefono_g= request.POST['Telefono']
    mail_g=request.POST['email']
    ccontra_g=request.POST['password']
    

    tipousuario_g=Rol.objects.get(idTipo=2)

    Usuario.objects.create(rut=rut_g, nombre=nombre_g, telefono=telefono_g, contrasenia=ccontra_g, mail=mail_g, rol= tipousuario_g)
    User.objects.create_user(id = rut_g, username = nombre_g, password=ccontra_g, first_name=nombre_g, email=mail_g, is_staff=1, is_superuser=0)

    messages.success(request,'usuario creado con exito')
    return redirect('registro')
    #------------------------------------------

#eliminar usuario

def eliminar_usuario(request, rutu):
    usuario1 = Usuario.objects.get(rut=rutu)
    usuario1.delete() #elimina el registro
    messages.success(request,'usuario Eliminado')
    return redirect('listadousuario')
#-----------------------------------

#modificacion de usuario admin

def modificar_usuario(request, rut_g):
    usuario1 = Usuario.objects.get(rut=rut_g)
    tipo1= Rol.objects.all()
    contexto = {
        "usuario" : usuario1,
        "tipousuario": tipo1
    }
    return render(request, 'OTY/modificarusuario.html', contexto)

def modificar(request):
    rut_g=request.POST['rut']
    tipo_g=request.POST['tipo']

    usuario1=Usuario.objects.get(rut=rut_g)
    user2=User.objects.get(id=rut_g)

    tipo_g2= Rol.objects.get(idTipo=tipo_g)
    usuario1.tipousuario = tipo_g2

    if tipo_g2.idTipo == 1:
        user2.is_superuser = 1
    if tipo_g2.idTipo == 2:
        user2.is_superuser = 0
    usuario1.save() #update

    messages.success(request,'usuario actualizado')
    return redirect('listadousuario')
    #----------------------------

#modificar usuario 

def modificar_usuario1(request, rut):
    usuario1 = Usuario.objects.get(rut=rut)
    contexto = {
        "usuario" : usuario1,
    }
    return render(request, 'OTY/modificarusuario1.html', contexto)


def modificaru(request):
    nombre_g=request.POST['nombre']
    apellido1_g=request.POST['apellido1']
    apellido2_g=request.POST['apellido2']
    rut_g= request.POST['rut']
    nombre_usuario_g=request.POST['nombreu']
    mail_g=request.POST['correo']
    ccontra_g=request.POST['ccontra']
    direccion=request.POST['direccion']
#-------------

#login
def login_view(request):
    u = request.POST['username']
    c = request.POST['password']

    user = authenticate(username = u, password = c)

    if user is not None:
        if user.is_active:
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,'Usuario Inactivo')
    else:
        messages.error(request,'Usuario y/o contraseña incorrecta')

    return redirect('log')

def logout_view(request):
    logout(request)
    return redirect('home')