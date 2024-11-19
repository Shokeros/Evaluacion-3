from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def inicio():
    return render_template('Inicio.html')


@app.route('/Ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        nombre = str(request.form['nombre'])
        edad = int(request.form['edad'])
        cant_tarros = int(request.form['cant_tarros'])
        precio_tarros = cant_tarros * 9000
        descuento = 0
        nuevo_precio = precio_tarros

        if 18 <= edad <= 30:
            descuento = precio_tarros * 0.15
            nuevo_precio -= - descuento

        if 30 < edad:
            descuento = precio_tarros * 0.25
            nuevo_precio -= descuento

        return render_template('Ejercicio1.html',
                               nombre=nombre, precio_tarros=precio_tarros,
                               descuento=descuento, nuevo_precio=nuevo_precio)

    return render_template('Ejercicio1.html')


@app.route('/Ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        usuarios = [{'nombre': 'juan', 'contrasena': 'admin'},
                    {'nombre': 'pepe', 'contrasena': 'user'}]
        nombreusuario = str(request.form['nombreusuario'])
        contrasenausuario = str(request.form['contrasenausuario'])
        mensaje = 'Usuario o contraseña incorrectos.'

        for usuario in usuarios:
            if usuario['nombre'] == nombreusuario and usuario['contrasena'] == contrasenausuario:

                if usuario['nombre'] == 'juan' and usuario['contrasena'] == 'admin':
                    mensaje = 'Bienvenido administrador Juan.'

                if usuario['nombre'] == 'pepe' and usuario['contrasena'] == 'user':
                    mensaje = 'Bienvenido usuario Pepe.'

        return render_template('Ejercicio2.html',
                               mensaje=mensaje)

    return render_template('Ejercicio2.html')


if __name__ == '__main__':
    app.run()
