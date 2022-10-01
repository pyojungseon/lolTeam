import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import requestDTO
from DTO.logDTO import logDTO
from DTO.tierDTO import tierDTO
from MariaDB.DBCon import DBConnection

class requestParsing:

    def parsing(self, params, dbCon):
        print(str(params))
        #log = logDTO("team", str(params))
        #dbCon.insertLogData(log)
        content = params['nick']
        print("parsing data : ")
        for i in range(0, 10):
            print(content[i])

        user=[]
        for i in range(0, 10):
            # get tier data from db
            userData = dbCon.getUserTier(content[i])
            print(str(userData))
            if userData[1]=="I":
                tier_number = 6
            elif userData[1]=="B":
                tier_number = 5
            elif userData[1]=="S":
                tier_number = 4
            elif userData[1]=="G":
                tier_number = 3
            elif userData[1]=="P":
                tier_number = 2
            elif userData[1] == "D":
                tier_number = 1
            elif userData[1] == "M":
                tier_number = 0

            tiers=tierDTO(content[i], tier_number, userData[2], userData[3], userData[4], userData[5], userData[6])
            user.append(tiers)

        return user
