$(document).ready(function(){
    $("#error").hide(); //ocultarfeederror
    $("#form-registro").submit(function(){
      var mensaje = "Revisa los siguientes detalles en el formulario";
      //Usuario
      
      
      if($("#Rut").val().trim().length == 0){
        mensaje = mensaje + " <br>-No ingreso rut";
      }
      if($("#Rut").val().trim().length >= 12){
        mensaje = mensaje + " <br>-rut no valido";
      }
      if($("#username").val().trim().length == 0){
        mensaje = mensaje + " <br>-No ingreso usuario";
      }
      if($("#username").val().trim().length < 5){
        mensaje = mensaje + " <br>-El usuario debe contener 5 caracteres";
      }
      if($("#Telefono").val().trim().length == 0){
        mensaje = mensaje + " <br>-No ingreso usuario";
      }
      if($("#Telefono").val().trim().length < 11){
        mensaje = mensaje + " <br>-El telefono debe contener +56 9 y los 8 numeros restantes caracteres";
      }
      //Correo
      if($("#email").val().trim().length == 0){
        mensaje = mensaje + "<br>-No ingreso correo";
      }
      //Contraseña
      if ($("#pasword").val() != $("#ccontra").val()) {
        mensaje = mensaje + "<br>-Las contraseñas deben ser iguales";
      }
      if ($("#password").val().trim().length == 0) {
        mensaje = mensaje + "<br>-La contraseña no debe estar vacia";
      }
      if ($("#password").val().trim().length < 8) {
        mensaje = mensaje + "<br>-La contraseña debe tener mas 8 caracteres";
      }
      //Terminos
      //if ($("#checko").is(':not(:checked)')) {
      //  mensaje = mensaje + "<br>Debe acaeptar los terminos"
      //}
      if( $('#TERMINOS').is(':checked') ) {    
    }else{
      mensaje = mensaje + "<br>-Debe acaeptar los terminos"
    }
      if(mensaje != "Revisa los siguientes detalles en el formulario"){
        $("#error").html(mensaje);
        $("#error").show();
        event.preventDefault();
    }
    });
  });