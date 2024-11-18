from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def Inicio():
    return render_template('Inicio.html')


@app.route('/Ejercicio1', methods=['GET', 'POST'])
def Ejercicio1():
    if request.method == 'POST':

        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])
        promedio = (nota1 + nota2 + nota3) / 3
        mensaje1 = None
        mensaje2 = None
        aprobado = 'Reprobado.'

        rango_notas = (10 <= nota1 <= 70 and 10 <= nota2 <= 70 and 10 <= nota3 <= 70)
        rango_asist = (0 <= asistencia <= 100)

        if not rango_notas:
            mensaje1 = 'Las notas deben estar entre un rango de 10 a 70.'
            aprobado = 'Notas fuera de rango.'

        if not rango_asist:
            mensaje2 = 'La asistencia tiene que estar en un rango de 0 a 100.'
            aprobado = 'Asistencia fuera de rango.'

        if promedio < 40:
            mensaje1 = 'Promedio debajo del mínimo (40).'

        if asistencia < 75:
            mensaje2 = 'Asistencia debajo del mínimo (75%).'

        if rango_notas and rango_asist and promedio >= 40 and asistencia >= 75:
            aprobado = 'Aprobado.'
            mensaje1 = '¡Felicidades!'

        return render_template('Ejercicio1.html',
                               promedio=promedio, aprobado=aprobado,
                               mensaje1=mensaje1, mensaje2=mensaje2)
    return render_template('Ejercicio1.html')


@app.route('/Ejercicio2', methods=['GET', 'POST'])
def Ejercicio2():
    if request.method == 'POST':
        nombres = [str(request.form['nombre1']), str(request.form['nombre2']), str(request.form['nombre3'])]

        nombrelargo = max(nombres, key=len)
        nombrecantidad = len(nombrelargo)

        return render_template('Ejercicio2.html',
                               nombrelargo=nombrelargo, nombrecantidad=nombrecantidad)
    return render_template('Ejercicio2.html')


if __name__ == '__main__':
    app.run()
