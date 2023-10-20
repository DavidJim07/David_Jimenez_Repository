@extends('layouts.app-master')
@section('content')

<div>
    <br>
    @foreach ($images as $row)
    <div class="mt-5/10 zoom">
        <center>
            <img src="{{URL::to('/')}}/images/{{$row->image}}" alt="Image" width="300 px" height="300 px" >
        </center>
    </div>
    @endforeach
</div>
@endsection