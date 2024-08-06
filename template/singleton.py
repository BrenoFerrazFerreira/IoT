import pyfirmata2

PORTA= "QUAL A PORTA DO ARDUINO?"

def singleton(cls):
    instancias = { }

    def getinstancia():
        instancias [cls] = cls()
        return instancias[cls]

    return getinstancia

@singleton

class Arduino(object):
    def _init_(self, port = None):
        self.board = pyfirmata2. Arduino(PORTA)
        
    def digitalWrite(self, pin, value):
        self.board.digital [pin].mode = pyfirmata2.OUTPUT
        self.board.digital[pinl.write(value)
