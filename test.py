from assembleTeam import assembleTeam
import sys, os
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from DTO.requestDTO import requestDTO
from DTO.tierDTO import tierDTO

assemble = assembleTeam()

user1=tierDTO("한은총재", 5, "Y", "N", "Y", "N", "Y")
user2=tierDTO("대봉동", 5, "Y", "N", "N", "N", "N")
user3=tierDTO("뽀뇨", 4, "Y", "N", "N", "Y", "Y")
user4=tierDTO("머스탱", 3, "Y", "N", "Y", "N", "N")
user5=tierDTO("수성못", 2, "N", "N", "Y", "N", "N")
user6=tierDTO("엔비코", 3, "N", "Y", "N", "N", "N")
user7=tierDTO("순 줌", 2, "N", "N", "N", "N", "Y")
user8=tierDTO("음 식", 1, "N", "N", "N", "N", "Y")
user9=tierDTO("케이윌", 1, "Y", "N", "N", "Y", "N")
user10=tierDTO("워윅킴", 5, "Y", "N", "N", "N", "N")

user=[];
user.append(user1)
user.append(user2)
user.append(user3)
user.append(user4)
user.append(user5)
user.append(user6)
user.append(user7)
user.append(user8)
user.append(user9)
user.append(user10)

assemble.splitteam(user)