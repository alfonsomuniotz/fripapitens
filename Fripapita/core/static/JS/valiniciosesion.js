$(document).ready(function(){
    $("#error").hide(); //ocultarfeederror
    $("#form-inicio-sesion").submit(function(){
      var mensaje = "Revisa los siguientes detalles en el formulario";
      if($("#username").val().trim().length == 0){
        mensaje = mensaje + " <br>No ingreso un usuario"
      }
      if($("#password").val().trim().length == 0){
        mensaje = mensaje +" <br>Debe ingresar una contraseña: "
      }
      if($("#password").val().trim().length <= 8){
        mensaje = mensaje + " <br>Contraseña incorrecta "
      }
      if(mensaje != "Revisa los siguientes detalles en el formulario"){
        $("#error").html(mensaje);
        $("#error").show();
        event.preventDefault();
      }
    });
  });