# auto - brand, speed, max_speed, engine

bmw = {
    'brand': 'BMW',
    'speed': 0,
    'max_speed': 250,
    'engine': False,
}


def auto_factory(brand, max_speed):
    return {
        'brand': brand,
        'speed': 0,
        'max_speed': max_speed,
        'engine': False,
    }


audi = auto_factory('AUDI', 180)
mercedes = auto_factory('MERCEDES', 220)
fiat = auto_factory('FIAT', 160)


def start_engine(car):
    if not car['engine']:
        car['engine'] = True
        print('Engine started')
    else:
        print('Engine already started')


def stop_engine(car):
    car['engine'] = False
    print('Engine stopped')


def accelerate(car, speed):
    if car['engine']:
        car['speed'] = min(car['speed'] + speed, car['max_speed'])
        print(f'Speed: {car["speed"]}')
    else:
        print('Engine not started')


def decelerate(car, speed):
    if car['engine']:
        car['speed'] = max(car['speed'] - speed, 0)
        print(f'Speed: {car["speed"]}')


accelerate(bmw, 100)
start_engine(bmw)
accelerate(bmw, 100)
accelerate(bmw, 100)
accelerate(bmw, 100)
decelerate(bmw, 100)
decelerate(bmw, 100)
decelerate(bmw, 500)
stop_engine(bmw)
