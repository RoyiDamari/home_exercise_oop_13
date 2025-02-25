class Lights:
    def turn_on(self):
        print("Lights: ON")

    def turn_off(self):
        print("Lights: OFF")


class TV:
    def turn_on(self, channel=None):
        if channel:
            print(f"TV: ON (channel = {channel})")
        else:
            print("TV: ON")

    def turn_off(self):
        print("TV: OFF")


class AirConditioner:
    def set_temperature(self, temperature):
        print(f"Air Conditioner: Set to {temperature}°C")


class PopcornMaker:
    def turn_on(self):
        print("Popcorn Maker: ON")

    def make_popcorn(self):
        print("Popcorn Maker: Popcorn is ready!")

    def turn_off(self):
        print("Popcorn Maker: OFF")
