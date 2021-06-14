import java.util.ArrayList;
import java.util.Map;

public class UberVan extends Car {
    Map<String, Map<String, Integer>> typeCarAccepted;
    ArrayList<String> seatsMaterial;

    public UberVan(String license, Account driver){
        super(license, driver);
    }

    public UberVan(String license, Account driver, Map<String, Map<String, Integer>> typeCarAccepted, ArrayList<String> seatsMaterial){
        super(license, driver);
        this.typeCarAccepted = typeCarAccepted;
        this.seatsMaterial = seatsMaterial;
    }
    @Override
    public void setPassenger(int p) {
        // TODO Auto-generated method stub
        if(p == 6)
            super.setPassenger(p);
        else
            System.out.println("this is a van men, not accept this number of passengers: " + p);
    }
}
