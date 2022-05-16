function alertaCerrar(){
    Swal.fire({
        title: 'Esta seguro?',
        text: "Estas apunto de cerrar seccion!",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Cerrar Seccion!',
      }).then((result) => {
        if (result.isConfirmed) {
          Swal.fire(
            'Bien, Hasta Luego!',
            'Tu seccion se ah cerrado.',
            'success'
          ).then(function(){
            window.location.href = "/";
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
          'El producto se ah eliminado.',
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
          'El usuario se ah eliminado.',
          'success'
        ).then(function(){
          window.location.href = "/eliminar_usuario/"+rut+"/";
        }).then(function(){
          window.location.href = "/listar_usuarios";
        })
      }
    })
}