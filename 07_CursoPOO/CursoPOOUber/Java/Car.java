package CursoPOOUber.Java;

public class Car {
    Integer Id;
    String license;
    Account driver;
    Integer passenger;

    public Car(String license, Account driver){
        this.license = license;
        this.driver = driver;
    }

    void printDataCar(){
        System.out.println("License: " + license + " driver: " + driver.name);
    }
}
