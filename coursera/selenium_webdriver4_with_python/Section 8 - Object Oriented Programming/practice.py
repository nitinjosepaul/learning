class Car(object):
    def __init__(self, make, model):
        self.make = make
        self.model = model
        print(f"Created car instance: {self.make} {self.model}")

    def drive(self):
        print(f"{self.make} {self.model} started")

    def stop(self):
        print(f"{self.make} {self.model} stopped")

class BMW(Car):
    def __init__(self):
        super().__init__(make='BMW', model='XM Label')

    def start_deep_sleep(self):
        print("Starting deep sleep mode")

    def stop_deep_sleep(self):
        print("Stopping deep sleep mode")

b = BMW()
b.drive()
b.stop()
b.start_deep_sleep()
b.stop_deep_sleep()