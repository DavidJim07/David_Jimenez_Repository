<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Domicilio extends Model
{
    use HasFactory;
    protected $table="domicilio";
    protected $fillable=['id','pais','estado','ciudad','codpost','colonia','calle','numext','entrecalle','idUser'];

    public function domicilio(){
        return $this->hasMany(Domicilio::class);
    }
}
