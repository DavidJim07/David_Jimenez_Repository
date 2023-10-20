<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

use App\Models\User;

class usuarioController extends Controller
{
    /**
     * Display a listing of the resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function index()
    {
        //
        $usuarios = User::all();
        return view('usuario.listado', compact('usuarios'));
    }
    public function filtro(Request $request)
    {
        $data=$request->all();
        $usuarios=User::where('estado','1')
        ->where('name','like','%'.$data['nombre'].'%')
        ->get();
        return view('usuario.contenido',compact('usuarios'));
        //return "Hola desde funcion filtro";
    }
    /**
     * Show the form for creating a new resource.
     *
     * @return \Illuminate\Http\Response
     */
    public function create()
    {
        //
        return view('usuario.nuevo');
    }

    /**
     * Store a newly created resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @return \Illuminate\Http\Response
     */
    public function store(Request $request)
    {
        //
        $validated = $request->validate([
            'nombre'=> 'required',
            'paterno'=>'required',
            'materno'=>'required',
            'fecha'=>'required',
            'genero'=>'required',
            'telefono'=>'required',
            'email'=>'required',
            'rol'=>'required',
            'usuario'=>'required',
            'contraseña'=>'required'
        ]);
        $data=$request->all();
        //dd($data);
        User::create([
            'name'=>$data['nombre'],
            'paterno'=>$data['paterno'],
            'materno'=>$data['materno'],
            'nacimiento'=>$data['fecha'],
            'genero'=>$data['genero'],
            'telefono'=>$data['telefono'],
            'email'=>$data['email'],
            'role'=>$data['rol'],
            'username'=>$data['usuario'],
            'password'=>$data['contraseña']
        ]);
        return redirect('/usuario');
    }

    /**
     * Display the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function show($id)
    {
        //
        $usuario = User::where('id','=',$id)->first();
        return view('usuario.consulta',compact('usuario'));
    }

    /**
     * Show the form for editing the specified resource.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function edit($id)
    {
        $usuario = User::where('id','=',$id)->first();
        return view('usuario.modificar',compact('usuario'));
    }

    public function editPassword($id)
    {
        $usuario = User::where('id','=',$id)->first();
        //dd($usuario);
        return view('usuario.modificarPassword',compact('usuario'));
    }

    /**
     * Update the specified resource in storage.
     *
     * @param  \Illuminate\Http\Request  $request
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function update(Request $request, $id)
    {
        //
        $data=$request->all();

        $usuario  = User::find($id);
        //dd($usuario);

        $usuario->name=$data['nombre'];
        $usuario->paterno=$data['paterno'];
        $usuario->materno=$data['materno'];
        $usuario->nacimiento=$data['fecha'];
        $usuario->genero=$data['genero'];
        $usuario->telefono=$data['telefono'];
        $usuario->email=$data['email'];
        $usuario->role=$data['rol'];
        $usuario->username=$data['usuario'];

        $usuario->save();

        return redirect('/usuario');
    }

    /**
     * Remove the specified resource from storage.
     *
     * @param  int  $id
     * @return \Illuminate\Http\Response
     */
    public function destroy($id)
    {
        //
        $usuario  = User::find($id);
        $usuario->estado="0";
        $usuario->save();

        return redirect('/usuario');
    }
}
