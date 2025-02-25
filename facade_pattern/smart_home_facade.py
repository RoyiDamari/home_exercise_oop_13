from subsystems import Lights, TV, AirConditioner, PopcornMaker


class SmartHomeFacade:

    def __init__(self, lights = Lights(), tv = TV(), ac = AirConditioner(), popcorn_maker = PopcornMaker()):
        self.lights = lights
        self.tv = tv
        self.ac = ac
        self.popcorn_maker = popcorn_maker

    def say_good_morning(self):

        print("\n=== Good Morning Routine ===")
        self.lights.turn_on()
        self.tv.turn_on(channel="Music Channel")
        self.ac.set_temperature(22)

    def say_watch_movie(self):

        print("\n=== Watch Movie Routine ===")
        self.popcorn_maker.turn_on()
        self.popcorn_maker.make_popcorn()
        self.popcorn_maker.turn_off()
        self.lights.turn_off()
        self.tv.turn_on(channel="Netflix")
        self.ac.set_temperature(18)


    def say_good_night(self):

        print("\n=== Good Night Routine ===")
        self.lights.turn_off()
        self.tv.turn_off()
        self.ac.set_temperature(28)



