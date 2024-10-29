from pyfirmata2 import Arduino, INPUT, OUTPUT, util

PORTA = "COM5"
arduino = Arduino(PORTA)

it = util.Iterator(arduino)
it.start()
movimento = arduino.get_pin('d:2:i')
buzz = arduino.get_pin('d:3:o')
led = arduino.get_pin('d:13:o')

while True:
    valor = movimento.read()
    if valor == 0:
        led.write(0)
        buzz.write(0)
        print("esse aqiu esta no true: " , valor)
    valor = movimento.read()
    led.write(1)
    buzz.write(0)
    arduino.pass_time(1)
