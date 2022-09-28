import constlol
from scorelol import scorelol

class assembleTeam:

    def splitteam(self, user):
        con = constlol.const
        sc = scorelol()
        team=["", "", "", "", "", "", "", "", "", ""]
        used=[0,0,0,0,0,0,0,0,0,0]
        wrong=[0,0,0,0,0,0,0,0,0,0]
        tier=[0,0,0,0,0]

        #포지션별 숫자먼저
        #적은 순서대로 잡기
        for j in range(0,10):
            if user[j].top=='Y':
                tier[con.TOP] = tier[con.TOP]+1
            if user[j].jug == 'Y':
                tier[con.JUG] = tier[con.JUG]+1
            if user[j].mid == 'Y':
                tier[con.MID] = tier[con.MID]+1
            if user[j].adc == 'Y':
                tier[con.ADC] = tier[con.ADC]+1
            if user[j].sup == 'Y':
                tier[con.SUP] = tier[con.SUP]+1

        sorted_tier=[]
        sorted_used=[0,0,0,0,0]
        for j in range(0, 5):
            sorted_point = 0
            sorted_value = 100
            for k in range(0, 5):
                if tier[k]<sorted_value and sorted_used[k]==0:
                    sorted_value=tier[k]
                    sorted_point=k
            sorted_tier.append(sorted_point)
            sorted_used[sorted_point] = 1;


        #티어가 낮고 포지션이 적은 사람 먼저 채우기
        for p in range(0,5):
            for teams in range(0,2):
                position = tier[sorted_tier[p]]
                point=-1
                score = 100
                for i in range(0,10):
                    if position == con.TOP:
                        if user[i].top=='Y' and sc.getScore(user[i].tier, con.TOP)<score and used[i]==0:
                            point = i
                            score = sc.getScore(user[i].tier, con.TOP)

                    elif position == con.JUG:
                        if user[i].jug=='Y' and sc.getScore(user[i].tier, con.JUG)<score and used[i]==0:
                            point = i
                            score = sc.getScore(user[i].tier, con.JUG)

                    elif position == con.MID:
                        if user[i].mid=='Y' and sc.getScore(user[i].tier, con.MID)<score and used[i]==0:
                            point = i
                            score = sc.getScore(user[i].tier, con.MID)

                    elif position == con.ADC:
                        if user[i].adc=='Y' and sc.getScore(user[i].tier, con.ADC)<score and used[i]==0:
                            point = i
                            score = sc.getScore(user[i].tier, con.ADC)

                    elif position == con.SUP:
                        if user[i].sup=='Y' and sc.getScore(user[i].tier, con.SUP)<score and used[i]==0:
                            point = i
                            score = sc.getScore(user[i].tier, con.SUP)

                    if point!=-1:
                        team[position*2+teams]=point
                        used[point]=1

        rest=[]
        for i in range(0, 10):
            if used[i]==0:
                rest.append(i)

        # 남는 빈자리는 그냥 채우기
        for p in range(0, 10):
            if len(str(team[p]))==0:
                wrong[p]=1
                team[p]=rest.pop()

        for i in range (0, 10):
            print(user[team[i]].id+" "+str(wrong[i]))


        # 점수 맞추기
        point=[]
        for i in range(0, 10):
            point.append(sc.getScore(user[team[i]].tier, int(i/2)))

        print(str(point))

