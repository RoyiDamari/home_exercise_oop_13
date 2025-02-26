from smart_home_facade import SmartHomeFacade


def main():
    # Create the Facade
    smart_home = SmartHomeFacade()

    # Now we can use the facade's simple methods
    smart_home.say_good_morning()
    smart_home.say_watch_movie()
    smart_home.say_good_night()


if __name__ == "__main__":
    main()
