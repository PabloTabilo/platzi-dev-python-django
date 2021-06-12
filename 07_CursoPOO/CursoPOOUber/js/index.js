const { Car } = require('./Car');
const { Account } = require('./Account');

var car = new Car("AW456", new Account("Pablo", "ID123"));
car.printDataCar();