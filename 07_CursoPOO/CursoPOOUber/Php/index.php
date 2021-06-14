<?php

require_once("car.php");
require_once("uberX.php");
require_once("uberVan.php");
require_once("Account.php");

$uberX = new UberX("CVB123", new Account("Pablo Ignacio", "AMS123"), "Chevrolet", "Spark");
$uberX->printDataCar();

$uberVan = new UberVan("OJL395", new Account("Raúl Ramírez", "AND456"), "Nissan", "Versa");
$uberVan->setPassenger(6);
$uberVan->printDataCar();

?>