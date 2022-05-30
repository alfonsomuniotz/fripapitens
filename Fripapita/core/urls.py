from django.urls import path
#from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from .views import registro, home, registrar_usuario, log, forgetpassword, login_view, logout_view



urlpatterns=[ 
   path('',home, name='home'),
    #Aqui van mis html normales de navegación
#    path('index',index, name='index'),
#    path('login',login, name='login'),

#
     #Esto es de las personas
#    path('form_persona', form_persona, name='form_persona'),

#    path('register/' , Register , name="register"),
   path('forgetpassword', forgetpassword ,name="forgetpassword"),
#    path('change-password/<token>/' , ChangePassword , name="change_password"),
#    path('logout/' , Logout , name="logout"),
  path ('registro',registro,name="registro"),
  path ('registrar_usuario',registrar_usuario,name="registrar_usuario"),
  path('log',log,name="log"),


  path('login/',LoginView.as_view(template_name='core/log.html'),name="login"),
  path('sesion',login_view,name="sesion"),
  path('logout',logout_view,name="logout"),
  #path('eliminar/<rutu>',eliminar_usuario, name="eliminar_usuario"),

]


