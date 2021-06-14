
class Main{
    public static void main(String[] args) {
        System.out.println("holas");
        UberX uberX = new UberX("AMQ123", new Account("Pablo", "ID123"), "Chevrolet", "Spark");
        uberX.setPassenger(3);
        uberX.printDataCar();

        UberVan uberV = new UberVan("AMQ123", new Account("Juan Carlos", "D876876"));
        uberV.setPassenger(5);
        uberV.printDataCar();
    }
}