<?php
class Car{
    public $id;
    public $license;
    public $driver;
    public $passenger;

    public function __construct($license, $driver){
        $this->license = $license;
        $this->driver = $driver;
    }
    public function printDataCar(){
        echo "
        license: $this->license,
        conductor: {$this->driver->name},
        document: {$this->driver->document},
        passenger: $this->passenger

        ";
    }
    public function getPassenger(){
        return $this->passenger;
    }
    public function setPassenger($p){
        if($p == 4){
            $this->passenger = $p;
        }else{
            echo "Necesitas 4 passengers";
        }
    }
}

?>