<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

use App\Models\User;
use App\Models\Domicilio;
use App\Models\Tarjeta;
use App\Models\Pedido;
use App\Models\RenglonPedido;

class UserController extends Controller
{
    /**
 * Display a listing of the resource.
     */
    public function index()
    {
        //
        if(Auth::check()){
            if(Auth::user()->role=="A"){
                $usuarios = User::where('role','=','A')->where('estado', '=', '1')->get();
                return view('usuarios.ListarUsuarios',compact('usuarios'));
            }
        }
        return redirect('/');
    }

    /**
     * Show the form for creating a new resource.
     */
    public function create()
    {
        //
        return view('registrar.registrarPersona');
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        //
        if ($request->has('flexCheckDefault')) {
            // El checkbox está marcado
            $validated = $request->validate([
                'nombre'=> 'required',
                'paterno'=>'required',
                'materno'=>'required',
                'nacimiento'=>'required',
                'genero'=> 'required',
                'telefono'=>'required',
                'email'=>'required',
                'password'=>'required',

                'pais'=>'required',
                'estado'=>'required',
                'ciudad'=>'required',
                'colonia'=>'required',
                'codigoPostal'=>'required',
                'calle'=>'required',
                'numero'=>'required',
                'entreCalles'=>'required',

                'tarjeta'=>'required',
                'numeroTarjeta'=>'required',
                'vencimiento'=>'required',
                'ccv'=>'required' 
            ]);
            $data=$request->all();
            //dd($data);
            $user = new User();
            $user->nombre = $data['nombre'];
            $user->paterno = $data['paterno'];
            $user->materno = $data['materno'];
            $user->fechanacimiento = $data['nacimiento'];
            $user->genero = $data['genero'];
            $user->telefono = $data['telefono'];
            $user->email = $data['email'];
            $user->password = $data['password'];
            // $user->estado = 1;
            // $user->role = "rol";
            // $user->name = "usuario";
            if(Auth::check()){
                if(Auth::user()->role=="A"){
                    $opcionSeleccionada = $request->input('rol');
                    if ($opcionSeleccionada) {
                        // La opción está seleccionada
                        if($opcionSeleccionada=="Administrador"){
                            $user->role = "A";
                        }
                    }
                }
            }
            $user->save();

            // El ID del usuario recién creado
            $usuarioId = $user->id;

            $domicilio = new Domicilio();
            $domicilio->pais = $data['pais'];
            $domicilio->estado = $data['estado'];
            $domicilio->ciudad = $data['ciudad'];
            $domicilio->codpost = $data['codigoPostal'];
            $domicilio->colonia = $data['colonia'];
            $domicilio->calle = $data['calle'];
            $domicilio->numext = $data['numero'];
            $domicilio->entrecalle = $data['entreCalles'];
            $domicilio->idUser = $usuarioId;
            $domicilio->save();

            $tarjeta = new Tarjeta();
            $tarjeta->nombre = $data['tarjeta'];
            $tarjeta->numerotarjeta = $data['numeroTarjeta'];
            $tarjeta->fecha = $data['vencimiento'];
            $tarjeta->ccv = $data['ccv'];
            $tarjeta->idUser = $usuarioId;
            $tarjeta->save();
            // User::create([
            //     'name'=>$data['nombre'],
            //     'paterno'=>$data['paterno'],
            //     'materno'=>$data['materno'],
            //     'fechanacimiento'=>$data['nacimiento'],
            //     'genero'=>$data['genero'],
            //     'telefono'=>$data['telefono'],
            //     'email'=>$data['email'],
            //     //'role'=>$data['rol'],
            //     //'username'=>$data['usuario'],
            //     'password'=>$data['contraseña'],
            //     'estado'=>1
            // ]);

            if(Auth::check()){
                if(Auth::user()->role=="A"){
                    return redirect('/usuario');
                }
            }

            $credentials = $request->only('email', 'password');

            if (Auth::attempt($credentials)) {
                // Autenticación exitosa
                $user = Auth::getProvider()->retrieveByCredentials($credentials);
                Auth::login($user);
                return $this->authenticated($request, $user);
            } else {
                // Autenticación fallida
                return redirect()->back()->withErrors(['message' => 'Correo o contraseña inválidas']);
            }
        } else {
            // El checkbox no está marcado
            $validated = $request->validate([
                'nombre'=> 'required',
                'paterno'=>'required',
                'materno'=>'required',
                'nacimiento'=>'required',
                'genero'=> 'required',
                'telefono'=>'required',
                'email'=>'required',
                'password'=>'required',

                'pais'=>'required',
                'estado'=>'required',
                'ciudad'=>'required',
                'colonia'=>'required',
                'codigoPostal'=>'required',
                'calle'=>'required',
                'numero'=>'required',
                'entreCalles'=>'required',
            ]);

            $data=$request->all();
            //dd($data);
            $user = new User();
            $user->name = $data['nombre'];
            $user->paterno = $data['paterno'];
            $user->materno = $data['materno'];
            $user->fechanacimiento = $data['nacimiento'];
            $user->genero = $data['genero'];
            $user->telefono = $data['telefono'];
            $user->email = $data['email'];
            $user->password = $data['password'];
            // $user->estado = 1;
            // $user->role = "rol";
            // $user->name = "usuario";
            if(Auth::check()){
                if(Auth::user()->role=="A"){
                    $opcionSeleccionada = $request->input('rol');
                    if ($opcionSeleccionada) {
                        // La opción está seleccionada
                        if($opcionSeleccionada=="Administrador"){
                            $user->role = "A";
                        }
                    }
                }
            }
            $user->save();

            // El ID del usuario recién creado
            $usuarioId = $user->id;

            $domicilio = new Domicilio();
            $domicilio->pais = $data['pais'];
            $domicilio->estado = $data['estado'];
            $domicilio->ciudad = $data['ciudad'];
            $domicilio->codpost = $data['codigoPostal'];
            $domicilio->colonia = $data['colonia'];
            $domicilio->calle = $data['calle'];
            $domicilio->numext = $data['numero'];
            $domicilio->entrecalle = $data['entreCalles'];
            $domicilio->idUser = $usuarioId;
            $domicilio->save();

            if(Auth::check()){
                if(Auth::user()->role=="A"){
                    return redirect('/usuario');
                }
            }

            $credentials = $request->only('email', 'password');

            if (Auth::attempt($credentials)) {
                // Autenticación exitosa
                $user = Auth::getProvider()->retrieveByCredentials($credentials);
                Auth::login($user);
                return $this->authenticated($request, $user);
            } else {
                // Autenticación fallida
                return redirect()->back()->withErrors(['message' => 'Correo o contraseña inválidas']);
            }
        }
    }

    /**
     * Display the specified resource.
     */
    public function show(string $id)
    {
        //
        if(Auth::check()){
            if(Auth::user()->role=="A"){
                $user = User::where('id','=',$id)->first();
                return view('usuarios.ConsultarUsuarios',compact('user'));
            }
        }
        return redirect('/');
    }

    /**
     * Show the form for editing the specified resource.
     */
    public function edit(string $id)
    {
        //
        if(Auth::check()){
            if(Auth::user()->role=="A"){
                $user = User::where('id','=',$id)->first();
                return view('usuarios.ModificarUsuarios',compact('user'));
            }
        }
        return redirect('/');
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, string $id)
    {
        //
        $validated = $request->validate([
            'nombre'=> 'required',
            'paterno'=>'required',
            'materno'=>'required',
            'nacimiento'=>'required',
            'genero'=> 'required',
            'telefono'=>'required',
        ]);

        $data=$request->all();
        //dd($data);
        $user = User::where('id','=',$id)->first();
        $user->name = $data['nombre'];
        $user->paterno = $data['paterno'];
        $user->materno = $data['materno'];
        $user->fechanacimiento = $data['nacimiento'];
        $user->genero = $data['genero'];
        $user->telefono = $data['telefono'];
        $user->save();

        return redirect('/usuario');
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(string $id)
    {
        //
        $user = User::where('id','=',$id)->first();
        $user->estado=0;
        $user->save();
        Tarjeta::where('idUser','=',$id)->delete();
        Domicilio::where('idUser','=',$id)->delete();
        return redirect('/usuario');
    }
    
    protected function authenticated(Request $request, $user)
    {
        return redirect()->route('home.index');
    }

    public function pedidos()
    {
        //dd("Pedidos");
        if(Auth::check()){
            if(Auth::user()->role=="U"){
                $usuario = User::where('id','=',Auth::user()->id)->first();
                $domicilios=array();
                $tarjetas=array();
                $pedidos = Pedido::where('idUser','=',Auth::user()->id)->get();
                foreach($pedidos as $pedido){
                    array_push($tarjetas, Tarjeta::where('id','=',$pedido->idTarjeta)->first());
                    array_push($domicilios, Domicilio::where('id','=',$pedido->idDomicilio)->first());
                }
                return view('usuarios.PedidoUsuario',compact('usuario','domicilios','tarjetas','pedidos'));
            }
        }
        return redirect('/');
    }
}
