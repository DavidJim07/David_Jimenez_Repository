<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Zapato extends Model
{
    use HasFactory;
    protected $table="zapato";
    protected $fillable=['id','color','estilo','material','modelo','url','estado'];

    public function zapato(){
        return $this->hasMany(Zapato::class);
    }

}
