from car import Car
from account import Account

if __name__ == "__main__":
    print("This is main")
    car = Car("AMS234", Account("Pablo", "id123"))
    print(vars(car))