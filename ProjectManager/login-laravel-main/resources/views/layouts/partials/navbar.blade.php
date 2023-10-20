<header class="p-3 bg-dark text-white">
  <div class="container">
    <div class="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
      <a href="/" class="d-flex align-items-center mb-2 mb-lg-0 text-white text-decoration-none">
        <svg class="bi me-2" width="40" height="32" role="img" aria-label="Bootstrap"><use xlink:href="#bootstrap"/></svg>
      </a>
@auth
      <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
        <li>
          <a href="/home" class="nav-link px-2 text-white">Inicio</a>
        </li>
        @if(Auth::User()->hasRole('administrador'))
        <li>
          <a href="/proyecto" class="nav-link px-2 text-white">Proyectos</a>
        </li>
        @endif
        
        <li>
          <a href="/actividad" class="nav-link px-2 text-white">Actividad</a>
        </li>
        @if(Auth::User()->hasRole('administrador'))
        <li>
          <a href="/usuario" class="nav-link px-2 text-white">Usuarios</a>
        </li>
       @endif
       @if(Auth::User()->hasRole('administrador'))
        <li>
          <a href="/apiexterna/proyecto" class="nav-link px-2 text-white">Proyectos Externos</a>
        </li>
        @endif
        @if(Auth::User()->hasRole('administrador'))
        <li>
          <a href="/apiexterna/actividad" class="nav-link px-2 text-white">Actividades externa</a>
        </li>
        @endif
        @if(Auth::User()->hasRole('administrador'))
        <li>
          <a href="/apiexterna/usuario" class="nav-link px-2 text-white">Actividades externa</a>
        </li>
        @endif
        
      </ul>

      {{auth()->user()->name}}
        <div class="text-end px-2">
          <a href="{{ route('logout.perform') }}" class="btn btn-outline-light me-2">Cerrar sesión</a>
        </div>
      @endauth

      @guest
        <div class="text-end">
          <a href="{{ route('login.perform') }}" class="btn btn-outline-light me-2">Iniciar sesión</a>
          <a href="{{ route('register.perform') }}" class="btn btn-warning">Crear Usuario</a>
        </div>
      @endguest
    </div>
  </div>
</header>