<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <link rel="stylesheet" type="text/css" href="{{ asset('css/bootstrap.css')}}">
</head>
<body>
    @include('menu')
    <div class="container-fluid">
        <div class="card">
        <div class="card-header">
            Modificar Contraseña
        </div>
        @if($errors->any())
            <div class="alert alert-danger">
                <ul>
                    @foreach($errors->all() as $error)
                        <li>{{$error}}</li>
                    @endforeach
                </ul>
            </div>
        @endif
        <div class="card-body">
            <form action="/usuario/{{$usuario->id}}/updp" method="post">
                @method('PUT')
                @csrf
                <div class="mb-3">
                    <label for="lastPassword" class="form-label">Contraseña Antigua:</label>
                    <input type='text' name='lastPassword' id='lastPassword' class="form-control" value="{{old('lastPassword')}}">
                </div>
                <div class="mb-3">
                    <label for="newPassword" class="form-label">Contraseña Nueva:</label>
                    <input type='text' name='newPassword' id='newPassword' class="form-control" value="{{old('newPassword')}}">
                </div>
                <button type="submit" class="btn btn-primary">Submit</button>
            </form>
        </div>
        </div>
    
    </div>
    
    <script type="text/javascript" src="{{ asset('js/bootstrap.js') }}"></script>
    
</body>
</html>