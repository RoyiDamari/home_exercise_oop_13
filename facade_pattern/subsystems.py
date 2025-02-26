class Lights:
    @staticmethod
    def turn_on():
        print("Lights: ON")

    @staticmethod
    def turn_off():
        print("Lights: OFF")


class TV:
    @staticmethod
    def turn_on(channel=None):
        if channel:
            print(f"TV: ON (channel = {channel})")
        else:
            print("TV: ON")

    @staticmethod
    def turn_off():
        print("TV: OFF")


class AirConditioner:
    @staticmethod
    def set_temperature(temperature):
        print(f"Air Conditioner: Set to {temperature}°C")


class PopcornMaker:
    @staticmethod
    def turn_on():
        print("Popcorn Maker: ON")

    @staticmethod
    def make_popcorn():
        print("Popcorn Maker: Popcorn is ready!")

    @staticmethod
    def turn_off():
        print("Popcorn Maker: OFF")
