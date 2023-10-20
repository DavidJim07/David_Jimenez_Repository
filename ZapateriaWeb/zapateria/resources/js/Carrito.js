document.addEventListener('DOMContentLoaded', () => {
    const baseDeDatos = [{
            id: 1,
            nombre: 'Zapatos',
            precio: 1030,
            imagen: '../Images/zapato1.jpg',
            cantidad: 0
        },
        {
            id: 2,
            nombre: 'Tenis',
            precio: 1252,
            imagen: '../Images/zapato2.jpg',
            cantidad: 0
        },
        {
            id: 3,
            nombre: 'Zandalias',
            precio: 839,
            imagen: '../Images/zapato3.jpg',
            cantidad: 0
        },
        {
            id: 4,
            nombre: 'Botas',
            precio: 962,
            imagen: '../Images/tenis1.jpg',
            cantidad: 0
        },
        {
            id: 5,
            nombre: 'Zandalias',
            precio: 839,
            imagen: '../Images/tenis2.jpg',
            cantidad: 0
        },
        {
            id: 6,
            nombre: 'Botas',
            precio: 962,
            imagen: '../Images/tenis3.jpeg',
            cantidad: 0
        }
    ];

    let carrito = [];
    const divisa = '$';
    const DOMitems = document.querySelector('#items');
    const DOMcarrito = document.querySelector('#carrito');
    const DOMtotal = document.querySelector('#total');
    const DOMbotonVaciar = document.querySelector('#boton-vaciar');
    const miLocalStorage = window.localStorage;

    function renderizarProductos() {
        baseDeDatos.forEach((info) => {
            const miNodo = document.createElement('div');
            miNodo.classList.add('card', 'col-sm-4');

            const miNodoCardBody = document.createElement('div');
            miNodoCardBody.classList.add('card-body');

            const miNodoTitle = document.createElement('h5');
            miNodoTitle.classList.add('card-title');
            miNodoTitle.textContent = info.nombre;

            const miNodoImagen = document.createElement('img');
            miNodoImagen.classList.add('img-fluid');
            miNodoImagen.setAttribute('src', info.imagen);
            miNodoImagen.style.width = '150px';
            miNodoImagen.style.height = '130px';

            miNodoImagen.addEventListener('mouseenter', function() {
                miNodoImagen.style.transform = 'scale(2)';
            });

            miNodoImagen.addEventListener('mouseleave', function() {
                miNodoImagen.style.transform = 'scale(1)';
            });

            const miNodoPrecio = document.createElement('p');
            miNodoPrecio.classList.add('card-text');
            miNodoPrecio.textContent = `${divisa}${info.precio}`;

            const miNodoBoton = document.createElement('button');
            miNodoBoton.classList.add('btn', 'btn-primary');
            miNodoBoton.textContent = 'Agregar al carrito';
            miNodoBoton.setAttribute('marcador', info.id);
            miNodoBoton.addEventListener('click', agregarProductoAlCarrito);

            const miLabel = document.createElement('label');
            miLabel.setAttribute('for', `talla-${info.id}`, 'mt-1');
            miLabel.textContent = 'Talla:';

            const miDropdown = document.createElement('select');
            miDropdown.classList.add('btn', 'btn-outline-primary', 'dropdown-toggle', 'mt-1', 'ml-1');
            miDropdown.setAttribute('data-toggle', 'dropdown');
            miDropdown.setAttribute('id', `talla-${info.id}`);
            for (let i = 20; i <= 34; i++) {
                const miOption = document.createElement('option');
                miOption.textContent = i;
                miDropdown.appendChild(miOption);
            }

            miNodoCardBody.appendChild(miNodoImagen);
            miNodoCardBody.appendChild(miNodoTitle);
            miNodoCardBody.appendChild(miNodoPrecio);
            miNodoCardBody.appendChild(miNodoBoton);
            miNodoCardBody.appendChild(miLabel);
            miNodoCardBody.appendChild(miDropdown);
            miNodo.appendChild(miNodoCardBody);
            DOMitems.appendChild(miNodo);
        });
    }

    function agregarProductoAlCarrito(evento) {
        carrito.push(evento.target.getAttribute('marcador'))
        renderizarCarrito();
        guardarCarritoEnLocalStorage();
    }

    function renderizarCarrito() {
        DOMcarrito.textContent = '';
        const carritoSinDuplicados = [...new Set(carrito)];
        carritoSinDuplicados.forEach((item) => {
            const miItem = baseDeDatos.filter((itemBaseDatos) => {
                return itemBaseDatos.id === parseInt(item);
            });
            const numeroUnidadesItem = carrito.reduce((total, itemId) => {
                return itemId === item ? total += 1 : total;
            }, 0);
            const miNodo = document.createElement('li');
            miNodo.classList.add('list-group-item', 'text-right', 'mx-2');
            miNodo.textContent = `${numeroUnidadesItem} x ${miItem[0].nombre} - ${miItem[0].precio}${divisa}`;
            const miBoton = document.createElement('button');
            miBoton.classList.add('btn', 'btn-danger', 'mx-5');
            miBoton.textContent = 'X';
            miBoton.style.marginLeft = '1rem';
            miBoton.dataset.item = item;
            miBoton.addEventListener('click', borrarItemCarrito);
            miNodo.appendChild(miBoton);
            DOMcarrito.appendChild(miNodo);
        });
        DOMtotal.textContent = calcularTotal();
    }

    function borrarItemCarrito(evento) {
        const id = evento.target.dataset.item;
        carrito = carrito.filter((carritoId) => {
            return carritoId !== id;
        });
        renderizarCarrito();
        guardarCarritoEnLocalStorage();

    }

    function calcularTotal() {
        return carrito.reduce((total, item) => {
            const miItem = baseDeDatos.filter((itemBaseDatos) => {
                return itemBaseDatos.id === parseInt(item);
            });
            return total + miItem[0].precio;
        }, 0).toFixed(2);
    }

    function vaciarCarrito() {
        carrito = [];
        renderizarCarrito();
        localStorage.clear();

    }

    function guardarCarritoEnLocalStorage() {
        miLocalStorage.setItem('carrito', JSON.stringify(carrito));
    }

    function cargarCarritoDeLocalStorage() {
        if (miLocalStorage.getItem('carrito') !== null) {
            carrito = JSON.parse(miLocalStorage.getItem('carrito'));
        }
    }

    DOMbotonVaciar.addEventListener('click', vaciarCarrito);
    cargarCarritoDeLocalStorage();
    renderizarProductos();
    renderizarCarrito();
});