import pymysql
from app import app
from config import mysql
from flask import jsonify, render_template, redirect, url_for
from flask import flash, request




@app.route('/edit/<expediente>')
def get_paciente(expediente):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM paciente WHERE expediente =%s", expediente)       
    d = cursor.fetchone()   
    return render_template('edit-paciente.html', paciente = d)


@app.route('/update/<expediente>', methods=['POST'])                                                                             
def update_paciente(expediente):
    if request.method == 'POST':
        _entidadNac = request.form['entidad']
        _curp = request.form['curp']
        _sexo = request.form['sexo']
        _talla = request.form['talla']	
        _domicilio = request.form['domicilio']
        _telefono = request.form['telefono']
        _fechaNac = request.form['fechaNac']
        
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)	
        
        cursor.execute(""" 
            UPDATE paciente
            SET entNacimiento = %s,
                curp = %s,
                sexo = %s,
                talla = %s,
                domicilio = %s,
                telefono = %s,
                fechaNac = %s
            where expediente = %s
        """, (_entidadNac, _curp, _sexo, _talla, _domicilio, _telefono, _fechaNac, expediente))
        conn.commit() 
        flash('Registro')
    return redirect(url_for('tasks')) 


@app.route('/consulta/<_expediente>')
def mostrarIdentidad(_expediente):
    conn = mysql.connect()
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM paciente WHERE expediente =%s", _expediente)       
    id = cursor.fetchone()
    cursor.execute("SELECT * FROM diagnostico WHERE paciente_expediente =%s", _expediente)    
    diag = cursor.fetchone()  
    cursor.execute("SELECT * FROM visita WHERE paciente_expediente =%s", _expediente)                                                                                                                                   
    visit = cursor.fetchall()                                                                                     
    return render_template('tasks2.html', d = id, d2 = diag, d3 = visit)



@app.route('/login', methods=['POST'])
def login():
        _usuario = request.form['usuario']
        _password = request.form['password']

        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
            
        cursor.execute("SELECT * FROM usuario WHERE usuario = %s AND password = %s", (_usuario, _password))
        user = cursor.fetchone()
        cursor.close()    
        conn.connect()

        if user is not None:
            return redirect(url_for('tasks'))
        else:
            return render_template('index.html', message="Las credenciales no son correctas")

@app.route('/tasks')
def tasks():
    _Paciente_expediente= "88"
    conn = mysql.connect()
    cursor = conn.cursor()
    #cursor.execute("SELECT * FROM paciente WHERE expediente =%s", _Paciente_expediente)                                                                                                                                     
    cursor.execute('SELECT * FROM paciente')  
    #cursor.execute("SELECT * FROM paciente WHERE expediente LIKE " + ("'"+ _Paciente_expediente + "%'")) 
    #print("SELECT * FROM paciente WHERE expediente LIKE " + ("'"+ _Paciente_expediente + "%'"))                                                                                                                              
    data = cursor.fetchall()    
    return render_template('tasks.html', contacts = data)


@app.route('/search' , methods=['POST'])
def search():
    _Paciente_expediente= request.form['expBus']
    conn = mysql.connect()
    cursor = conn.cursor()
    #cursor.execute("SELECT * FROM paciente WHERE expediente =%s", _Paciente_expediente)                                                                                                                                     
    #cursor.execute('SELECT * FROM paciente')  
    cursor.execute("SELECT * FROM paciente WHERE expediente LIKE " + ("'"+ _Paciente_expediente + "%'")) 
    #print("SELECT * FROM paciente WHERE expediente LIKE " + ("'"+ _Paciente_expediente + "%'"))                                                                                                                              
    data = cursor.fetchall()    
    return render_template('tasks.html', contacts = data)

@app.route('/create', methods=['POST'])
def create_postman():
    try:        
        _json = request.json
        _entidadNac = _json['entidadNac']
        _curp = _json['curp']
        _sexo = _json['sexo']
        _talla = _json['talla']	
        _domicilio = _json['domicilio']
        _telefono = _json['telefono']
        _spss = _json['spss']	
        _fechaNac = _json['fechaNac']
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)	
            	
            sqlQuery = "INSERT INTO paciente(entNacimiento, curp, sexo, talla, domicilio, telefono, spss, fechaNac) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            bindData = (_entidadNac, _curp, _sexo, _talla, _domicilio, _telefono, _spss, _fechaNac)            
            cursor.execute(sqlQuery, bindData)
            #cursor.execute("INSERT INTO paciente(entNacimiento, curp, sexo, talla, domicilio, telefono, spss, fechaNac) VALUES(2, 2, 2, 2, 2, 2, 2, 2023-1-1)")
            conn.commit()
            respone = jsonify('Employee added successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  


@app.route('/visita', methods=['POST'])
def create_visita():       
        _fecha = request.form['fecha']
        _peso = request.form['peso']
        _talla = request.form['talla']
        _cintura = request.form['cintura']
        _trigliceridos = request.form['trigliceridos']	
        _glucemia = request.form['glucemia']
        _HbA1c = request.form['tension']
        _revisionPies =  request.form['pies'] 
        _controlado = request.form['control']
        _complicaciones = request.form['complicaciones']

        _referencia = request.form['referencia']
        _baja = request.form['baja']
        #_total = request.form['total']  
        _ldl = request.form['ldl']
        _hdl = request.form['hdl'] 
        _sistolica = request.form['sistolica']
        _diastolica = request.form['diastolica']
        _noFarmacologico = request.form['nofarmacologico']
        _farmacologico = request.form['farmacologico']
        _observaciones = request.form['notas']
        _Paciente_expediente = request.form['Paciente_expediente']
 
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)		
        sqlQuery = "INSERT INTO visita(fecha, peso, talla, trigliceridos, glucemia, HbA1c, revisionPies, controlado, complicaciones, referencia, baja, ldl, hdl, cintura, sistolica, diastolica,  noFarmacologico,  farmacologico, observaciones, Paciente_expediente) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        bindData = (_fecha, _peso, _talla, _trigliceridos, _glucemia, _HbA1c, _revisionPies, _controlado, _complicaciones, _referencia, _baja, _ldl, _hdl, _cintura, _sistolica, _diastolica, _noFarmacologico, _farmacologico, _observaciones, _Paciente_expediente)            
        cursor.execute(sqlQuery, bindData)
        conn.commit()
        flash('Visita registrada!')
        return redirect(url_for('tasks'))


@app.route('/regisrarP', methods=['POST'])
def registrar_paciente():
        _expediente = request.form['expediente']  
        _entidadNac = request.form['entidad']
        _curp = request.form['curp']
        _sexo = request.form['sexo']
        _talla = request.form['talla']	
        _domicilio = request.form['domicilio']
        _telefono = request.form['telefono']
        _fechaNac = request.form['fechaNac']

        _familiares =''.join(request.form.getlist('familiares[]')) 
        _personales =''.join(request.form.getlist('personales[]')) 

        _ingreso = request.form['ingreso-reingreso']
        _dm = request.form['tipo-dm']
        _hta = request.form.get('hta')
        _obesidad = request.form.get('obesidad')
        _dis = request.form.get('dislipidemias')
        _sindromeMetabolico = request.form.get('metabolico')
        _sobrepeso = request.form.get('sobrepeso')
        _deteccion = request.form['deteccion']
        _tratamientoPrevio = request.form['tratamiento']
        _covid = request.form['covid']
        
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)	
            sqlQuery = "INSERT INTO paciente(expediente, entNacimiento, curp, sexo, talla, domicilio, telefono, fechaNac) VALUES(%s, %s, %s, %s, %s, %s, %s, %s)"
            bindData = (_expediente, _entidadNac, _curp, _sexo, _talla, _domicilio, _telefono,  _fechaNac)            
            cursor.execute(sqlQuery, bindData)
            cursor.execute("INSERT INTO antecedentesfamiliares(Paciente_expediente, mapaAntecedentesFamiliares) VALUES(%s, %s) ",(_expediente, _familiares)  )
            cursor.execute(" INSERT INTO antecedentespersonales(Paciente_expediente, mapaAntecedentesPersonales) VALUES(%s, %s)", (_expediente, _personales) )
            sqlQuery = "INSERT INTO diagnostico(Paciente_expediente, ingreso, dm, hta, obesidad, dis, sindromeMetabolico, sobrepeso, deteccion, tratamientoPrevio, covid) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            bindData = (_expediente, _ingreso, _dm, _hta, _obesidad, _dis, _sindromeMetabolico, _sobrepeso, _deteccion, _tratamientoPrevio, _covid)
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            flash('Paciente registrado!')
            return redirect(url_for('tasks'))     

@app.route('/paciente')
def paciente():
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT expediente, entNacimiento, curp, sexo, talla, domicilio, telefono, spss, fechaNac FROM paciente")
        empRows = cursor.fetchall()
        respone = jsonify(empRows)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()  



@app.route('/paciente/<expediente>')
def emp_details(expediente):
    try:
        conn = mysql.connect()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        cursor.execute("SELECT entNacimiento, curp, sexo, talla, domicilio, telefono, spss, fechaNac FROM paciente WHERE expediente =%s", expediente)
        empRow = cursor.fetchone()
        respone = jsonify(empRow)
        respone.status_code = 200
        return respone
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 



@app.route('/update', methods=['PUT'])
def update_emp():
    try:
        _json = request.json
        _expediente = _json['expediente']
        _entidadNac = _json['entNacimiento']
        _curp = _json['curp']
        _sexo = _json['sexo']
        _talla = _json['talla']	
        _domicilio = _json['domicilio']
        _telefono = _json['telefono']
        _spss = _json['spss']	
        _fechaNac = _json['fechaNac']
        if _expediente and _entidadNac and _curp and _sexo and _talla and _domicilio and _telefono and _spss and _fechaNac and request.method == 'PUT':			
            sqlQuery = "UPDATE paciente SET entNacimiento=%s, curp=%s, sexo=%s, talla=%s, domicilio=%s, telefono=%s, spss=%s, fechaNac=%s WHERE expediente=%s"
            bindData = (_entidadNac, _curp, _sexo, _talla, _domicilio, _telefono, _spss, _fechaNac, _expediente)
            conn = mysql.connect()
            cursor = conn.cursor()
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('Employee updated successfully!')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close() 



@app.route('/delete/<expediente>')
def delete_emp(expediente):
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM paciente WHERE expediente = %s', expediente)
    conn.commit()
 #   respone = jsonify('Employee deleted successfully!')
 #   respone.status_code = 200
    return redirect(url_for('tasks'))
        
       
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 200
    return respone



@app.route('/')
def index():                                                                  
        return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)

