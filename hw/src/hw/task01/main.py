import logging
from abc import ABC, abstractmethod

logging.basicConfig(level=logging.INFO)


class Vehicle(ABC):
    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Двигун запущено")


class Motorcycle(Vehicle):
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        logging.info(f"{self.make} {self.model}: Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make, model) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Vehicle:
        return Car(make, f"{model} (US Spec)")

    def create_motorcycle(self, make, model) -> Vehicle:
        return Motorcycle(make, f"{model} (US Spec)")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model) -> Vehicle:
        return Car(make, f"{model} (EU Spec)")

    def create_motorcycle(self, make, model) -> Vehicle:
        return Motorcycle(make, f"{model} (EU Spec)")


if __name__ == "__main__":
    # Приклад використання фабрик для створення транспортних засобів з регіональними специфікаціями.
    us_factory = USVehicleFactory()
    eu_factory = EUVehicleFactory()

    vehicle1 = us_factory.create_car("Ford", "Mustang")
    vehicle1.start_engine()  # Очікуваний результат: Ford Mustang (US Spec): Двигун запущено

    vehicle2 = eu_factory.create_motorcycle("Harley-Davidson", "Sportster")
    vehicle2.start_engine()  # Очікуваний результат: Harley-Davidson Sportster (EU Spec): Мотор заведено
