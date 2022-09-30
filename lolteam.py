from flask import Flask, json, request, jsonify, Response
from requestParsing import requestParsing
import sys
import os
import ssl
from flask_cors import CORS, cross_origin

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.logDTO import logDTO
from DTO.tierDTO import tierDTO
from DTO.requestDTO import requestDTO
from MariaDB.DBCon import DBConnection
from assembleTeam import assembleTeam

app = Flask(__name__)
CORS(app, resources={r"/*":{"origins":"*"}})

@app.route('/')
def home():
    return "Hello, Flask"

@app.route('/test', methods=['POST'])
@cross_origin()
def posttest():
    data=str(request.get_data())
    print(data)
    resp=Response(data)
    #resp.headers['Access-Control-Allow-Credentials'] = 'true'
    resp.headers["Access-Control-Allow-Origin"] = "*"
    return resp

@app.route('/lolteam', methods=['POST'])
@cross_origin()
def restaurant():
    params = request.get_json()
    parser = requestParsing()
    user = parser.parsing(params, dbCon)

    assemble = assembleTeam()
    teamA = assemble.splitteam(user)
    teamAscore=teamA[5]
    teamBscore=teamA[6]
    teamB=[]
    for i in range(0,10):
        if teamA[(int)(i/2)]!=i:
            teamB.append(i)

    send_data={
        "teamA":[
            {
                "top":user[teamA[0]].id,
                "jug":user[teamA[1]].id,
                "mid":user[teamA[2]].id,
                "adc":user[teamA[3]].id,
                "sup":user[teamA[4]].id,
                "score":teamAscore
            }
        ],
        "teamB":[
            {
                "top": user[teamB[0]].id,
                "jug": user[teamB[1]].id,
                "mid": user[teamB[2]].id,
                "adc": user[teamB[3]].id,
                "sup": user[teamB[4]].id,
                "score":teamBscore
            }
        ]
    }


    return send_data


if __name__ == '__main__':
    dbCon = DBConnection('P')
    dbCon.dbConnection()
    ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS)
    ssl_context.load_cert_chain(certfile='cert.pem', keyfile='privkey.pem')
    app.run(host="0.0.0.0", port=10500, ssl_context=ssl_context, debug=True)
    #app.run(host="0.0.0.0", port=10500, debug=True)