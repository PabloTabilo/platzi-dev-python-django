
public class Car {
    private Integer Id;
    private String license;
    private Account driver;
    private Integer passenger = 0;

    public Car(String license, Account driver){
        this.license = license;
        this.driver = driver;
    }

    void printDataCar(){
        System.out.println("License: " + license + " driver: " + driver.name + "; passengers: " + passenger);
    }

    public Integer getPassenger(){return passenger;}
    public void setPassenger(int p){
        if(p > 0 && p < 7)
            this.passenger = p;
        else
            System.err.println("Not possible passenger for " + p);
    }

    public Integer getId() {
        return Id;
    }

    public void setId(Integer id) {
        Id = id;
    }

    public String getLicense() {
        return license;
    }

    public void setLicense(String license) {
        this.license = license;
    }

    public Account getDriver() {
        return driver;
    }

    public void setDriver(Account driver) {
        this.driver = driver;
    }
}
