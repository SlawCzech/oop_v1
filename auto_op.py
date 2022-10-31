class Auto:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.speed = 0
        self.max_speed = max_speed
        self.engine = False

    def start_engine(self):
        if not self.engine:
            self.engine = True
            print('Engine started')
        else:
            print('Engine already started')

    def stop_engine(self):
        self.engine = False
        print('Engine stopped')

    def accelerate(self, speed):
        if self.engine:
            self.speed = min(self.speed + speed, self.max_speed)
            print(f'Speed: {self.speed}')
        else:
            print('Engine not started')

    def decelerate(self, speed):
        if self.engine:
            self.speed = max(self.speed - speed, 0)
            print(f'Speed: {self.speed}')


bmw = Auto('BMW', 200)
audi = Auto('AUDI', 180)
mercedes = Auto('MERCEDES', 220)
fiat = Auto('FIAT', 160)

print(bmw)

print(bmw.brand)

bmw.accelerate(100)  # to jest syntactic sugar, który się używa
Auto.accelerate(bmw, 100)  # to jest to samo co œyżej
Auto.start_engine(bmw)  # to oznacza, że metoda należy do klasy, a nie do obiektu
bmw.accelerate(100)
bmw.accelerate(100)
bmw.accelerate(100)
bmw.decelerate(100)
bmw.decelerate(100)
bmw.decelerate(500)
bmw.stop_engine()
