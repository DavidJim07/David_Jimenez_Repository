var csrfToken = "{{ csrf_token() }}";
$.ajax({
    url: '/venta/producto',
    method: 'POST',
    headers: {
      'X-CSRF-TOKEN': csrfToken
    },
    data: { dato: cargarCarrito(), texto: "Holaaa" },
    success: function(response) {
      console.log('Solicitud exitosa');
      console.log('Respuesta del servidor:', response);
    },
    error: function(xhr, status, error) {
      console.log('Error en la solicitud');
      console.log('Código de estado:', xhr.status);
      console.log('Mensaje de error:', error);
    }
});

function cargarCarrito() {
    const miLocalStorage = window.localStorage;
    if (miLocalStorage.getItem('carrito') !== null) {
        return JSON.parse(miLocalStorage.getItem('carrito'));
    }else{
        return null;
    }
}