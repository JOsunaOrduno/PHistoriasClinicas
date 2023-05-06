@app.route('/prueba', methods=['POST'])
def prueba_paciente():
    try:        
        _entidadNac = request.form['entidad']
        _curp = request.form['curp']
        _sexo = request.form['sexo']
        _talla = request.form['talla']	
        _domicilio = request.form['domicilio']
        _telefono = request.form['telefono']
        _fechaNac = request.form['fechaNac']
        if request.method == 'POST':
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO paciente(entNacimiento, curp, sexo, talla, domicilio, telefono, fechaNac) VALUES(%s, %s, %s, %s, %s, %s, %s)"
            bindData = (_entidadNac, _curp, _sexo, _talla, _domicilio, _telefono,  _fechaNac)            
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
    
#Funciona bien ejecutando el main de la pagina principal, 
# se debe solo cambiar los request json por request form de los nombres del html
# Las variables no importan, solo importan en el sqlQuery donde se inserta en la base de datos, 
# es importante que sea correcto todo, no les dira dode esta el error pero no esta mal la app, son los datos que le meten

