class Flight:
    counter = 1

    def __init__(self, origin, destination, duration):
        self.origin = origin
        self.destination = destination
        self.duration = duration
        self.id = Flight.counter
        Flight.counter += 1
        self.passengers = []

    def print_info(self):
        print(f"Flight origin: {self.origin}")
        print(f"Flight destination: {self.destination}")
        print(f"Flight duration: {self.duration}")

        print()
        print("Passengers")
        for passenger in self.passengers:
            print(f"{passenger.name}")

    def delay(self, amount):
        self.duration += amount

    def add_passenger(self, p):
        self.passengers.append(p)
        p.Flight_id = self.id

class Passenger:
    def __init__(self, name):
        self.name = name

def main():
    f1 = Flight("New York", "Paris", 540) 

    alice = Passenger("Alice")
    bob = Passenger("Bob")

    f1.add_passenger(alice)
    f1.add_passenger(bob)

    f1.print_info()

if __name__ == "__main__":
    main()
