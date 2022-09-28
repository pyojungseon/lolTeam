from assembleTeam import assembleTeam
from requestParsing import requestParsing
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import requestDTO
from DTO.tierDTO import tierDTO
from MariaDB.DBCon import DBConnection



assemble = assembleTeam()
parser = requestParsing()
dbCon = DBConnection('P')
dbCon.dbConnection()
assemble.splitteam(parser.parsing("a"), dbCon)