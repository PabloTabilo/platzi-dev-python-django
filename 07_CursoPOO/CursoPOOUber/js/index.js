import Car from "./Car.js";
import UberX from "./UberX.js";
import Account from "./Account.js";

var car = new Car("AW456", new Account("Pablo", "ID123"));
car.printDataCar();

var uberX = new UberX("AWasd", new Account("Caco", "456"), "Chevrolet", "Spark");
uberX.printDataCar();