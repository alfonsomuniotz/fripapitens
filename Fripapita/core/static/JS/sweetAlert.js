swal.fire({
        title:'Bienvenido/a a FRIPAPITA!',
        text:'Ven y encuentra la mejor comida rápida!',
        confirmButtonText:'Vamos a comer!',
        footer:'<span class="verde">Recuerda que puedes pedir a domicilio y retirar </span>',
        padding: '1rem',
        backdrop: `
    rgba(255,0,0,0.6)
    url("/images/nyan-cat.gif")
    left top
    no-repeat
  `,
        timer: 10000,
        timerProgressBar: true,
        allowOutsideClick: false,
        allowEscapeKey: false,
        allowEnterKey: false,
        ShowConfirmButton: true,
        confirmButtonColor: '#9b0303',
        color: '#9b0303',
        buttonsStyling: true,
        showClosebutton: true,
        closeButtonAriaLabel: 'cerrar ventana',
        imageUrl: '../static/IMG/logo_final.png',
        imageWidth: '200px',
        imageAlt: 'Logo de Fripapita'
        
        /*icon:'success',*/
        /*icon:'question',*/
        /*icon:'warning',*/
        /*icon:'error',*/
        /*icon:'info',*/
        //imageHeight: '',
        
    });






