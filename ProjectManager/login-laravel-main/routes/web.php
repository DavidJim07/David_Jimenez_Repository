<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\RegisterController;
use App\Http\Controllers\ActividadController;
use App\Http\Controllers\ProyectoController;
use App\Http\Controllers\RelacionController;
use App\Http\Controllers\usuarioController;
use App\Http\Controllers\ImageController;
use App\Http\Controllers\ApiController;
use App\Http\Controllers\RecuperarController;
use App\Http\Controllers\ActividadesExternasController;
use App\Models\Actividad;
use App\Models\Proyecto;
use App\Models\Relacion;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/


/* Route::get('/register', [RegisterController::class, 'show']);
Route::post('/action-register', [RegisterController::class, 'register']); */
Route::get('/', function () {
    return view('home.index');
});

Route::group(['namespace' => 'App\Http\Controllers'], function()
{   
    Route::get('/home', 'HomeController@index')->name('home.index');

    Route::group(['middleware' => ['guest']], function() {

        Route::get('/register', 'RegisterController@show')->name('register.show');
        Route::post('/register', 'RegisterController@register')->name('register.perform');

        Route::get('/login', 'LoginController@show')->name('login.show');
        Route::post('/login', 'LoginController@login')->name('login.perform');

    });

    Route::group(['middleware' => ['auth']], function() {
        Route::get('/logout', 'LogoutController@perform')->name('logout.perform');
    });
});

Route::POST('/usuario/filtro', [usuarioController::class, 'filtro']);
Route::get('/actividad/{id}/imagen', [ActividadController::class, 'imagen']);
Route::POST('/actividad/filtro', [ActividadController::class, 'filtro']);
Route::POST('/proyecto/filtro', [ProyectoController::class, 'filtro']);
Route::get('/usuario/{id}/editPassword',[usuarioController::class, 'editPassword']);
Route::put('/usuario/{id}/updp',[usuarioController::class, 'updatePassword']);
Route::resource('/proyecto', ProyectoController::class);
Route::resource('/actividad', ActividadController::class);
Route::resource('/relacion', RelacionController::class);
Route::resource('/usuario', usuarioController::class);
// Route::resource('/apiexterna/proyectos', ActividadesExternasController::class , 'indexPro');
// Route::resource('/apiexterna/actividades', ActividadesExternasController::class , 'indexAct');
// Route::resource('/apiexterna/usuarios', ActividadesExternasController::class , 'indexUsu');
Route::resource('/recuperar', RecuperarController::class);

//Rutas para imagen
Route::get('/imagen', [ImageController::class,'index']);
Route::get('/imagen/create', [ImageController::class,'create']);
Route::post('/imagen/create', [ImageController::class,'store']);
