# importamos las clases y métodos
from flask import Flask, render_template, redirect, request
from flask_bootstrap import Bootstrap

app = Flask(__name__)
Bootstrap(app)

@app.route('/', methods=['GET', 'POST'])
def aritmetica():
    if request.method == "POST":
        # Valores que recibo del form n1, n2 son pasados
        num1 = float(request.form.get('n1'))
        num2 = float(request.form.get('n2'))
        # Realizamos operaciones aritméticas
        suma = num1 + num2
        resta = num1 - num2
        multiplicacion = num1 * num2
        division = num1 / num2
        return render_template('aritmetica.html', total_suma=suma, total_resta=resta, total_multiplicacion=multiplicacion, total_division=division)

    return render_template('aritmetica.html')
@app.route('/divisa', methods=['GET', 'POST'])
def divisa():
    if request.method=="POST":
        #Valores que recibo del form moneda
        moneda = request.form.get('monedausa')
        if moneda:  # Verificar si el valor existe
            monedausa = float(moneda)
            # Realizamos operaciones aritmeticas
            monedacol = monedausa * 4211.29  # Cambiado la coma por punto
            monedaarg = monedausa * 970.77   # Cambiado la coma por punto
            monedaeuro = monedausa * 0.90    # Cambiado la coma por punto
            return render_template('divisa.html', col=monedacol, arg=monedaarg, euro=monedaeuro)
    return render_template('divisa.html')

if __name__ == "__main__":
    app.run(debug=True)


