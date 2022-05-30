function alertaCerrar(){
    Swal.fire({
        title: 'Esta seguro?',
        text: "Estas apunto de cerrar sesion!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Cerrar Sesion!',
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            'Bien, Hasta Luego!',
            'Tu seccion se ha cerrado.',
            'success'
          ).then(function(){
            window.location.href = "/logout/";
          })
        }
      })
}

function alertaBorrarProducto(codigo){
  Swal.fire({
      title: 'Esta seguro?',
      text: "Estas apunto de eliminar este producto!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si, Eliminar!',
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire(
          'Listo !',
          'El producto se ha eliminado.',
          'success'
        ).then(function(){
          window.location.href = "/eliminar_productos/"+codigo+"/";
        }).then(function(){
          window.location.href = "/listar_productos";
        })
      }
    })
}

function borrarusuario(rut){
  Swal.fire({
      title: 'Esta seguro?',
      text: "Estas apunto de borrrar este usuario!",
      icon: 'warning',
      showCancelButton: true,
      confirmButtonColor: '#3085d6',
      cancelButtonColor: '#d33',
      confirmButtonText: 'Si, Eliminar usuario!',
    }).then((result) => {
      if (result.isConfirmed) {
        Swal.fire(
          'Listo!',
          'El usuario se ha eliminado.',
          'success'
        ).then(function(){
          window.location.href = "/eliminar_usuario/"+rut+"/";
        }).then(function(){
          window.location.href = "/listar_usuarios";
        })
      }
    })
}