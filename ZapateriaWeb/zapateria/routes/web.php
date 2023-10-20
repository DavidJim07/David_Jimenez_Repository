<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\RegisterController;
use App\Http\Controllers\LogoutController;
use App\Http\Controllers\LoginController;
use App\Http\Controllers\HomeController;
use App\Http\Controllers\VentaProducto;
use App\Http\Controllers\DomicilioController;
use App\Http\Controllers\TarjetaController;
use App\Http\Controllers\UserController;
use App\Http\Controllers\ZapatoController;
use App\Http\Controllers\TallaController;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
*/

Route::get('/', function () {
    return redirect()->route('home.index');
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

Route::resource('/usuario', UserController::class);

Route::get('/usuario/create', [UserController::class, 'create']);
Route::get('/usuario', [UserController::class, 'index']);
Route::get('/usuario/{id}', [UserController::class, 'show']);
Route::get('/usuario/{id}/edit', [UserController::class, 'edit']);
Route::post('/tarjeta/create', [TarjetaController::class, 'registrar']);
Route::post('/tarjeta/store', [TarjetaController::class, 'store']);
Route::post('/domicilio/create', [DomicilioController::class, 'create']);
Route::post('/domicilio/store', [DomicilioController::class, 'store']);
Route::post('/venta/producto', [VentaProducto::class, 'store']);
Route::post('/proceder/pago', [VentaProducto::class, 'procederPago']);
//Route::post('/login', 'LoginController@login')->name('login.perform');
//Route::post('/proceder/pago', 'VentaProducto@procederPago')->name('proceder.pago');

Route::resource('/zapatos', ZapatoController::class);
Route::resource('/talla', TallaController::class);
Route::get('/talla/surtir/{id}',[ TallaController::class, 'create']);
Route::get('/talla/listado/{id}',[ TallaController::class, 'index']);
Route::get('/talla/resurtir/{id}',[ TallaController::class, 'resurtir']);
Route::get('/pedidos',[ UserController::class, 'pedidos']);

Route::post('/confirmar/pedido', [VentaProducto::class, 'realizarPedido']);