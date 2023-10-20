<?php

namespace App\Models;
use Illuminate\Database\Eloquent\Model;

class RenglonPedido extends Model
{
    protected $table="renglonpedido";
    protected $fillable=['id','cantidad','idZapato','idTalla','idPedido'];

}