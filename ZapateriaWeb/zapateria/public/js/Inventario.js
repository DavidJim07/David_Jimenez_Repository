const baseDeDatos = [
  {
    id: 1,
    nombre: 'Zapatos',
    precio: 1030,
    imagen: '../Images/zapato1.jpg',
    cantidad: 0,
    talla: '42',
    material: 'Cuero',
    estilo: 'Casual',
    color: 'Negro'
  },
  {
    id: 2,
    nombre: 'Zapatos',
    precio: 1252,
    imagen: '../Images/zapato2.jpg',
    cantidad: 0,
    talla: '41',
    material: 'Sintético',
    estilo: 'Deportivo',
    color: 'Negro'
  },
  {
    id: 3,
    nombre: 'Zapatos',
    precio: 839,
    imagen: '../Images/zapato3.jpg',
    cantidad: 0,
    talla: '39',
    material: 'Piel',
    estilo: 'Casual',
    color: 'Negro'
  },
  {
    id: 4,
    nombre: 'Tenis',
    precio: 962,
    imagen: '../Images/tenis1.jpg',
    cantidad: 0,
    talla: '43',
    material: 'Cuero',
    estilo: 'Casual',
    color: 'Negro'
  },
  {
    id: 5,
    nombre: 'Tenis',
    precio: 839,
    imagen: '../Images/tenis2.jpg',
    cantidad: 0,
    talla: '39',
    material: 'Piel',
    estilo: 'Casual',
    color: 'Negro'
  },
  {
    id: 6,
    nombre: 'Tenis',
    precio: 962,
    imagen: '../Images/tenis3.jpeg',
    cantidad: 0,
    talla: '43',
    material: 'Cuero',
    estilo: 'Casual',
    color: 'Negro'
  }
];

const tablaProductos = document.getElementById('tabla-productos');

function mostrarProductos() {
  let html = '';
  baseDeDatos.forEach((producto) => {
    html += `
      <tr>
        <td>${producto.id}</td>
        <td>${producto.nombre}</td>
        <td>${producto.precio}</td>
        <td><img src="${producto.imagen}" width="50"></td>
        <td>${producto.talla}</td>
        <td>${producto.material}</td>
        <td>${producto.estilo}</td>
        <td>${producto.color}</td>
        <td>
          <input type="number" value="${producto.cantidad}" disabled id="cantidad-${producto.id}">
        </td>
        <td>
          <button class="btn btn-primary editar" data-id="${producto.id}">Editar</button>
          <button class="btn btn-danger eliminar" data-id="${producto.id}">Eliminar</button>
          <button class="btn btn-success resurtir" data-id="${producto.id}">Resurtir</button>
          <button class="btn btn-success guardar d-none" data-id="${producto.id}">Guardar</button>
          <button class="btn btn-danger cancelar d-none" data-id="${producto.id}">Cancelar</button>
        </td>
      </tr>
    `;
  });
  tablaProductos.innerHTML = html;

  const botonesEditar = document.querySelectorAll('.editar');
  botonesEditar.forEach((botonEditar) => {
    botonEditar.addEventListener('click', (event) => {
      const idProducto = event.target.getAttribute('data-id');
      window.location.href = 'Editar.html';
    });
  });

  const botonesEliminar = document.querySelectorAll('.eliminar');
  botonesEliminar.forEach((botonEliminar) => {
    botonEliminar.addEventListener('click', (event) => {
      const idProducto = event.target.getAttribute('data-id');
      const productoIndex = baseDeDatos.findIndex((producto) => producto.id === Number(idProducto));
      baseDeDatos.splice(productoIndex, 1);
      mostrarProductos();
    });
  });

}

mostrarProductos();