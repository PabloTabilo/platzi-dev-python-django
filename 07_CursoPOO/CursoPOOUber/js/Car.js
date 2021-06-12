const { Account } = require('./Account');
class Car{
    Car(license, driver){
        console.log(driver);
        this.id;
        this.license = license;
        this.driver = Account("","");
        this.passenger;
        console.log(this.driver);
    }
    printDataCar(){
        console.log(this.driver);
    }
}

module.exports = {
    Car,
}