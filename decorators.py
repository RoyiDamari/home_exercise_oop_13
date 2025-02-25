import logging
import time

logging.basicConfig(filename='app.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def password(func):
    def wrapper():
        entered = input("Enter password: ")
        if entered == "1234":
            return func()
        else:
            print("wrong password")
            logging.error(f"Failed password attempt - entered {entered}")
    return wrapper

@password
def say_hello():
    print("hello...")


def logme(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Calling function {func.__name__} with args={args}")
        result = func(*args, **kwargs)
        logging.info(f"Function {func.__name__} ended")
        return result

    return wrapper


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed = end_time - start_time
        print(f"{func.__name__} running time is {elapsed:.4f} seconds")
        logging.info(f"{func.__name__} running time is {elapsed:.4f} seconds")
        return result
    return wrapper

@timer
@logme
def star_print(msg):
    time.sleep(0.5)
    print('************', msg)


if __name__ == "__main__":
    say_hello()
    star_print("Hello Decorator!")
