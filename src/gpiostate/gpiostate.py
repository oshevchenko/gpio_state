import gpiod

GPIO_PIN_ACTIVE = 1
GPIO_PIN_INACTIVE = 0

class GpioPin:
    """
    Class to manage GPIO line.
    """
    def __init__(self, gpiochip = 'gpiochip3', offset = 1, inverted = False):
        self._line = gpiod.Chip(gpiochip).get_line(offset)
        self._line.request(consumer='gpiostate.py', type=gpiod.LINE_REQ_DIR_IN)
        self._inverted = inverted

    def get_state(self):
        """
        Get the current state of the GPIO line.
        """
        state = None
        try:
            state = self._line.get_value()
        except Exception as e:
            print(f"Error reading GPIO state: {e}")

        if self._inverted:
            if state == 1:
                state = GPIO_PIN_INACTIVE
            elif state == 0:
                state = GPIO_PIN_ACTIVE
        else:
            if state == 1:
                state = GPIO_PIN_ACTIVE
            elif state == 0:
                state = GPIO_PIN_INACTIVE
        return state
