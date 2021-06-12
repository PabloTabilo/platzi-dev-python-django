package CursoPOOUber.Java;

class Main{
    public static void main(String[] args) {
        System.out.println("holas");
        Car car = new Car("AMQ123", new Account("Pablo", "ID123"));
        car.printDataCar();
    }
}