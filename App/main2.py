import pymysql
from app import app
from config import mysql
from flask import jsonify
from flask import flash, request

@app.route('/create', methods=['POST'])
def create_visita():
    try:        
        _json = request.json
        _fecha = _json['fecha']
        _peso = _json['peso']
        _imc = _json['imc']
        _trigliceridos = _json['trigliceridos']	
        _glucemia = _json['glucemia']
        _HbA1c = _json['HbA1c']
        _revisionPies = _json['revisionPies']
        _controlado = _json['controlado']
        _ayudaMutua = _json['ayudaMutua']
        _complicaciones = _json['complicaciones']
        _referencia = _json['referencia']
        _baja = _json['baja']     
        _hdl = _json['hdl'] 
        _ldl = _json['ldl']
        _cintura = _json['cintura']
        _sistolica = _json['sistolica']
        _diastolica = _json['diastolica']
        _noFarmacologico = _json['noFarmacologico']
        _farmacologico = _json['farmacologico']
        _observaciones = _json['observaciones']
        _Paciente_expediente = _json['Paciente_expediente']
        
        if _fecha and _peso and _imc and _trigliceridos and _glucemia and _HbA1c and _revisionPies and _controlado and _ayudaMutua and _complicaciones and _referencia and _baja  and _hdl and _ldl and _cintura and _sistolica and _diastolica and _noFarmacologico and _farmacologico and _observaciones and _Paciente_expediente and request.method == 'POST':         
            conn = mysql.connect()
            cursor = conn.cursor(pymysql.cursors.DictCursor)		
            sqlQuery = "INSERT INTO visita(fecha, peso, imc, trigliceridos, glucemia, HbA1c, revisionPies, controlado, ayudaMutua, complicaciones, referencia, baja, hdl, ldl, cintura, sistolica, diastolica,  noFarmacologico,  farmacologico, observaciones, Paciente_expediente) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            bindData = (_fecha, _peso, _imc, _trigliceridos, _glucemia, _HbA1c, _revisionPies, _controlado, _ayudaMutua, _complicaciones, _referencia, _baja, _hdl, _ldl, _cintura, _sistolica, _diastolica, _noFarmacologico, _farmacologico, _observaciones, _Paciente_expediente)            
            cursor.execute(sqlQuery, bindData)
            conn.commit()
            respone = jsonify('AGREGADO CORRECTAMENTE')
            respone.status_code = 200
            return respone
        else:
            return showMessage()
    except Exception as e:
        print(e)
    finally:
        cursor.close() 
        conn.close()          
     
      
@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run()