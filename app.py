from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'secret_key'  # Para mostrar mensajes flash

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = request.form['nombre']
        edad = int(request.form['edad'])
        tarros = int(request.form['tarros'])

        precio_tarro = 9000
        total_sin_descuento = tarros * precio_tarro

        if edad >= 18 and edad <= 30:
            descuento = 0.15
        elif edad > 30:
            descuento = 0.25
        else:
            descuento = 0

        total_con_descuento = total_sin_descuento * (1 - descuento)

        return render_template(
            'ejercicio1.html',
            nombre=nombre,
            total_sin_descuento=total_sin_descuento,
            total_con_descuento=total_con_descuento,
            enviado=True
        )

    return render_template('ejercicio1.html', enviado=False)

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    usuarios = {'juan': 'admin', 'pepe': 'user'}

    if request.method == 'POST':
        usuario = request.form['usuario']
        contrasena = request.form['contrasena']

        if usuario in usuarios and usuarios[usuario] == contrasena:
            mensaje = f"Bienvenido {'administrador' if usuario == 'juan' else 'usuario'} {usuario}"
        else:
            mensaje = "Usuario o contraseña incorrectos"

        flash(mensaje)
        return redirect(url_for('ejercicio2'))

    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)
