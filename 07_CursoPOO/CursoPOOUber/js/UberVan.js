import Car from "./Car.js";

export default class UberVan extends Car{
    constructor(license, driver, typeCarAccepted, seatsMaterial){
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }
}