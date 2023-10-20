<script src="https://kit.fontawesome.com/d4a14445d4.js" crossorigin="anonymous"></script>

<nav class="menu-container">
    <!-- burger menu -->
    <input type="checkbox" aria-label="Toggle menu" />
    <span></span>
    <span></span>
    <span></span>
    <link rel="stylesheet" href="{{ asset('css/barra.css') }}">
    
    <a href="#" class="menu-logo">
        <i class="fa-solid fa-shoe-prints fa-beat fa-2xl" style="color: #cdcdcd;"></i>
    </a>
    
    <div class="menu">
        <ul>
            @if(Auth::check())
                @auth
                    @if(auth()->user()->role=="U")
                    <li>
                        <a class="nav-link" href="/home">Inicio</a>
                    </li>
                    @endif
                @endauth
            @else
                <li>
                    <a class="nav-link" href="/home">Inicio</a>
                </li>
            @endif
            @if(Auth::check())
                @auth
                    @if(auth()->user()->role=="A")
                    <li>
                        <a class="nav-link" href="/zapatos">Zapatos</a>
                    </li>
                    @endif
                @endauth
            @endif
            @if(Auth::check())
                @auth
                    @if(auth()->user()->role=="A")
                    <li>
                        <a class="nav-link" href="/usuario">Usuarios</a>
                    </li>
                    @endif
                @endauth
            @endif
            @if(Auth::check())
                @auth
                    @if(auth()->user()->role=="U")
                    <li>
                        <a class="nav-link" href="/pedidos">Mis pedidos</a>
                    </li>
                    @endif
                @endauth
            @endif
            <li>
                <a href="#blog">
                    Informacion
                </a>
            </li>
            <li>
                <a href="#docs">
                    Redes Sociales
                </a>
            </li>
        </ul>
        <ul>
            <li>
                @if(Auth::check())
                    @auth
                        {{auth()->user()->name}} {{auth()->user()->paterno}}
                        <i class="fa-solid fa-user fa-lg" style="color: #cdcdcd;">
                            <a href="{{ route('logout.perform') }}" class="btn btn-outline-info me-2">Logout</a>
                        </i>
                    @endauth
                @else
                    <i class="fa-solid fa-user fa-lg" style="color: #cdcdcd;">
                        <a href="{{ route('login.show') }}" class="btn btn-outline-success me-2">Logear</a>
                        <a href="/usuario/create" class="btn btn-outline-danger me-2">Registrate</a>
                    </i>
                @endif
            </li>
        </ul>
    </div>
</nav>

<!-- <nav class="navbar navbar-expand-lg navbar-light bg-light rounded mb-3 pb-3"> 
    <div class="container-fluid">
        <a class="navbar-brand" href="#">
            <img src="{{ asset('imagenes/icono.png') }}" width="50px" height="50px" alt="Logo de la Zapatería">
        </a>
        <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarNav">
            <ul class="navbar-nav mr-auto custom-list">
                <li class="nav-item active">
                    <a class="nav-link" href="/home">Carrito</a>
                </li>
                <li class="nav-item active">
                    <a class="nav-link" href="/zapatos">Zapatos</a>
                </li>
            </ul>
            <form class="d-flex" role="search">
                <input class="form-control mr-sm-2" type="search" placeholder="Buscar" aria-label="Buscar">
                <button class="btn btn-light my-2 my-sm-0" type="submit">
                    <img src="{{ asset('imagenes/lupa.png') }}" width="26px" height="26px" alt="Lupa">
                </button>
            </form>
        </div>
        <ul class="navbar-nav">
            <li class="nav-item">
                @if(Auth::check())
                    @auth
                        {{auth()->user()->name}} {{auth()->user()->paterno}}
                        <a href="{{ route('logout.perform') }}" class="btn btn-outline-info me-2">Logout</a>
                    @endauth
                @else
                    <a href="{{ route('login.show') }}" class="btn btn-success">Logear</a>
                    <a href="/usuario/create" class="btn btn-danger">Regístrate</a>
                @endif
            </li>
        </ul>
    </div>
</nav> -->
