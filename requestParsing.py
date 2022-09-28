import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import requestDTO
from DTO.tierDTO import tierDTO
from MariaDB.DBCon import DBConnection

class requestParsing:

    def parsing(self, params, dbCon):
        print(params)

        # reqDto = requestDTO()
        # userId = params['userRequest']['user']['id']
        # userId = userId.replace("\n", "")
        # content = params['userRequest']['utterance']
        # content = content.replace("\n", "")
        # header = content.split(" ")[0]

        #test data
        content=[]
        content.append("한은총재")
        content.append("나밟꿈")
        content.append("4등 못하면")
        content.append("솜포도")
        content.append("PAKA편집자")
        content.append("벤트탓옹")
        content.append("평타피하는중")
        content.append("진짜 섭섭한탑")
        content.append("cast")
        content.append("수성못")


        user=[]
        for i in range(0, 10):
            # get tier data from db
            userData = dbCon.getUserTier(content[i])
            tiers=tierDTO(content[i], userData[1], userData[2], userData[3], userData[4], userData[5], userData[6])
            user.append(tiers)

        return user
