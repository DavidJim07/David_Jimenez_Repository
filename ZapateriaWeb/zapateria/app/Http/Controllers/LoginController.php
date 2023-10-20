<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;
use App\Http\Requests\LoginRequest;
use App\Models\User;

class LoginController extends Controller
{
    //
    public function show()
    {
        if(Auth::check()){
            return redirect()->route('Index');
        }
        return view('welcome');
    }

    public function login(Request $request){
        //dd("Evaluao el login");

        $credentials = $request->only('email', 'password');
        //dd(var_dump($credentials));
        //$this->validarLogin($credentials['email'],$credentials['password']);

        if (Auth::attempt($credentials)) {
            // Autenticación exitosa
            //return redirect()->intended('/dashboard');
            $user = Auth::getProvider()->retrieveByCredentials($credentials);
            Auth::login($user);
            return $this->authenticated($request, $user);
        } else {
            // Autenticación fallida
            //$usuarios = User::all();
            //dd($usuarios,"Credenciales invalidas");
            //validarLogin($credentials->email,$credentials->password);
            return redirect()->back()->withErrors(['message' => 'Correo o contraseña inválidas']);
            //return redirect()->to('login')->withErrors(trans('auth.failed'));
        }
        // if(!Auth::validate($credentials)):
        //     dd($credentials);
        //    return redirect()->to('login')->withErrors(trans('auth.failed'));
        // endif;
        // if($credentials->permitirAcceso($credentials->email,$credentials->password)):
        //     dd($credentials."Hola");
        //    return redirect()->to('login')->withErrors(trans('auth.failed'));
        // endif;
    }

    protected function authenticated(Request $request, $user)
    {
        return redirect()->route('home.index');
    }

    public function validarLogin($email,$password){
        //dd($email,$password);
        $user = User::where('email','=',$email)->first();
        dd($user,"Usuario");
    }
}
