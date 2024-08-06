from arduino import Arduino
from flask import Flask, render_template
import datetime

LED = 13
estado = {'led': False}
app = Flask (_name__)

@app.route('/')
def inicio():
    return mostra_estado()

@app.route('/led/1')
def ligar_led():
    arduino = Arduino()
    arduino.digitalWrite(LED, 1)
    estado['led'] = True
    return mostra_estado()

@app.route('/led/0')
def desl_led():
    arduino = Arduino()
    arduino.digitalWrite(LED, 0)
    estado['led'] = False
    return mostra_estado()

def mostra_estado():
    return render_template('controle-led-bootstrap.html', **estado)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", debug = True)
