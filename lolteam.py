from flask import Flask, json, request, jsonify
from requestParsing import requestParsing
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.logDTO import logDTO
from DTO.tierDTO import tierDTO
from DTO.requestDTO import requestDTO
from MariaDB.DBCon import DBConnection

app = Flask(__name__)


@app.route('/')
def home():
    return "Hello, Flask"

@app.route('/lolteam', methods=['POST'])
def restaurant():
    params = request.get_json()
    parser = requestParsing()
    user = parser.parsing(params, dbCon)



if __name__ == '__main__':
    dbCon = DBConnection('P')
    dbCon.dbConnection()
    app.run(host='0.0.0.0', port=10008, debug=True)