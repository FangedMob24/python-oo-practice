"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self,start):
        """Saves the start number and initialize the number to be increased"""
        self.origin = start
        self.following_num = start - 1

    def generate(self):
        """Increases the number by one"""
        self.following_num += 1
        return self.following_num
    
    def reset(self):
        """Resets the number to the original start number"""
        self.following_num = self.origin - 1