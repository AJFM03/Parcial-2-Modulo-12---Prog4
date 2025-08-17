from flask import Flask, jsonify, abort
from data import VACUNAS

app = Flask(__name__)

# Endpoint: GET /vacunas -> Todos los registros
@app.route("/vacunas", methods=["GET"])
def get_vacunas():
    return jsonify(VACUNAS), 200

# Endpoint: GET /vacunas/<anio> -> Registro de un año específico
@app.route("/vacunas/<int:anio>", methods=["GET"])
def get_vacuna_por_anio(anio):
    registro = next((v for v in VACUNAS if v["anio"] == anio), None)
    if registro:
        return jsonify(registro), 200
    return jsonify({"error": "Año no encontrado"}), 404

# Endpoint opcional: GET /vacunas/provincia/<nombre>
@app.route("/vacunas/provincia/<string:nombre>", methods=["GET"])
def get_vacuna_por_provincia(nombre):
    # Simulación de datos regionales (ejemplo)
    regiones = ["Panamá", "Colón", "Chiriquí", "Coclé", "Veraguas"]
    if nombre.capitalize() not in regiones:
        return jsonify({"error": "Provincia no encontrada"}), 404
    
    # Simulamos datos iguales al promedio nacional
    datos = [{"anio": v["anio"], "porcentaje": round(v["porcentaje"] * 0.95, 1)} for v in VACUNAS]
    return jsonify({"provincia": nombre.capitalize(), "datos": datos}), 200

if __name__ == "__main__":
    app.run(debug=True, port=5000)
