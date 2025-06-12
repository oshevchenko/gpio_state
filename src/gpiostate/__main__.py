import gpiostate
import sys
from gpiostate import GpioPin
def main():

    if len(sys.argv) < 2:
        print("Usage: python -m gpiostate <gpio_pin>")
        sys.exit(1)

    try:
        gpio_pin = int(sys.argv[1])
    except ValueError:
        print("Invalid GPIO pin number. Please provide a valid integer.")
        sys.exit(1)

    factory_reset_btn = GpioPin(gpiochip = 'gpiochip3', offset=gpio_pin, inverted=True)
    state = factory_reset_btn.get_state()

    if state == gpiostate.GPIO_PIN_ACTIVE:
        state = "Active"
    elif state == gpiostate.GPIO_PIN_INACTIVE:
        state = "Inactive"
    else:
        state = "Unknown"

    print(f"GPIO pin {gpio_pin} state: {state}.")

if __name__ == "__main__":
    main()
