import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import requestDTO
from DTO.tierDTO import tierDTO
from MariaDB.DBCon import DBConnection

class requestParsing:

    def parsing(self, params, dbCon):
        print(params)

        reqDto = requestDTO()
        userId = params['userRequest']['user']['id']
        userId = userId.replace("\n", "")
        content = params['userRequest']['utterance']
        content = content.replace("\n", "")
        header = content.split(" ")[0]

        user=tierDTO()[10]
        for i in range(0, 10):
            user[i].id=content[i];
            # get tier data from db
            userData = dbCon.getUserTier(content[i])
            user[i].tier=userData.tier
            user[i].top=userData.top
            user[i].jug=userData.jug
            user[i].mid=userData.mid
            user[i].adc=userData.adc
            user[i].sup=userData.sup

        return user
