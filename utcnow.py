from flask import Flask, jsonify
from datetime import datetime, timezone, timedelta

# Inicializa o aplicativo Flask
app = Flask(__name__)

def get_current_datetime():
    brasilia_tz = timezone(timedelta(hours=-3))
    current_datetime = datetime.now(brasilia_tz)
    return {"datetime": current_datetime.strftime("%d/%m/%Y %H:%M:%S")}

def get_current_week_dates():
    brasilia_tz = timezone(timedelta(hours=-3))
    today = datetime.now(brasilia_tz)
    start_of_week = today - timedelta(days=today.weekday())
    end_of_week = start_of_week + timedelta(days=6)
    return {"week_start": start_of_week.strftime("%d/%m/%Y"), "week_end": end_of_week.strftime("%d/%m/%Y")}

def get_current_month_dates():
    brasilia_tz = timezone(timedelta(hours=-3))
    today = datetime.now(brasilia_tz)
    start_of_month = today.replace(day=1)
    if today.month == 12:
        end_of_month = today.replace(month=12, day=31)
    else:
        next_month = today.replace(month=today.month + 1, day=1)
        end_of_month = next_month - timedelta(days=1)
    return {"month_start": start_of_month.strftime("%d/%m/%Y"), "month_end": end_of_month.strftime("%d/%m/%Y")}

def get_day_of_week():
    brasilia_tz = timezone(timedelta(hours=-3))
    today = datetime.now(brasilia_tz)
    days_of_week = ["segunda-feira", "terça-feira", "quarta-feira", "quinta-feira", "sexta-feira", "sábado", "domingo"]
    return {"day_of_week": days_of_week[today.weekday()]}

# Rotas da API
@app.route("/", methods=["GET"])
def home():
    return "Bem-vindo à API de data e hora!"

@app.route("/get_current_datetime", methods=["GET"])
def get_datetime():
    return jsonify(get_current_datetime())

@app.route("/get_current_week_dates", methods=["GET"])
def get_week_dates():
    return jsonify(get_current_week_dates())

@app.route("/get_current_month_dates", methods=["GET"])
def get_month_dates():
    return jsonify(get_current_month_dates())

@app.route("/get_day_of_week", methods=["GET"])
def get_weekday():
    return jsonify(get_day_of_week())

# Inicia o servidor Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
