OUT = "GPIO.HIGH"
LOW = "GPIO.LOW"
HIGH = "GPIO.HIGH"


def setup(pin, GPIO_OUT):
    return (str(pin)+str(GPIO_OUT))

def output(pin, GPIO_OUT):
    return (str(pin)+str(GPIO_OUT))

def input(pin):
    return (str(pin))
