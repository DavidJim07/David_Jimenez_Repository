<?php

namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class Pedido extends Model
{
    protected $table="pedido";
    protected $fillable=['id','cantidad','subtotal','fechaPedido','idUser','idDomicilio','idTarjeta'];

}