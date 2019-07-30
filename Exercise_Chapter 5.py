###########################################################################
# Description: This is the exercises of chapter 5 in Investment Sciense.
# Author: Yeda Cui

def AddDim(lst, addlst):
    donelst = []
    if len(lst) is 0:
        for i in addlst:
            donelst.append([i])
    else:
        for i in lst:
            for j in addlst:
                donelst.append(i+[j])
    return donelst


# Exercise 2

net_return = [4, 5, 3, 4.3, 1, 1.5, 2.5, 0.3, 1, 2]
outlay = [2, 3, 1.5, 2.2, 0.5, 1.5, 2.5, 0.1, 0.6, 1]

def OptimalInvest(n, net_return, outlay):
# While using the function, you may set the condition by yourself!

    class INVEST:
        number = 0
        net_return = 0
        outlay = 0
        def __init__(self, invest):
            self.invest = invest
            INVEST.number += 1

        def GetReturn(self):
            length = len(self.invest)
            sum = 0
            for i in range(length):
                sum = sum + INVEST.net_return[self.invest[i]]
            return sum

        def GetOutlay(self):
            length = len(self.invest)
            sum = 0
            for i in range(length):
                sum = sum + INVEST.outlay[self.invest[i]]
            return sum

        def GetCondition(self):
            if (self.invest[0] in [1 ,3]) and (self.invest[1] == 4):
                return False
            else:
                if self.GetOutlay()>5:
                    return False
                else:
                    return True
    INVEST.net_return = net_return
    INVEST.outlay = outlay

    Invest_List = []
    for i in range(len(n)):
        addlst = list(range(sum(n[0:i]),sum(n[0:i+1])))
        Invest_List = AddDim(Invest_List, addlst)

    invests = []
    for i in Invest_List:
        invests.append(INVEST(i))

    Invest_List = invests

    return_list = []
    Invest_Avialbe = []
    for i in range(len(Invest_List)):
        if Invest_List[i].GetCondition():
            return_list.append(Invest_List[i].GetReturn())
            Invest_Avialbe.append(Invest_List[i])

    return([Invest_Avialbe[return_list.index(max(return_list))].invest,
            Invest_Avialbe[return_list.index(max(return_list))].GetReturn(),
            Invest_Avialbe[return_list.index(max(return_list))].GetOutlay()])


# exercise 3

class INVEST:
    number = 0
    net_return = 0
    outlay = 0

    def __init__(self, invest):
        self.invest = invest
        INVEST.number += 1

    def GetReturn(self):
        length = len(self.invest)
        sum = 0
        for i in range(length):
            sum = sum + INVEST.net_return[self.invest[i]]
        return sum

    def GetOutlay(self):
        length = len(self.invest)
        sum = 0
        for i in range(length):
            sum = sum + INVEST.outlay[self.invest[i]]
        return sum

    def GetCondition(self):
        if (self.invest[0] in [1, 3]) and (self.invest[1] == 4):
            return False
        else:
            if self.GetOutlay() > 5:
                return False
            else:
                return True


INVEST.net_return = net_return
INVEST.outlay = outlay

Invest_List = []
for i in range(len(n)):
    addlst = list(range(sum(n[0:i]), sum(n[0:i + 1])))
    Invest_List = AddDim(Invest_List, addlst)

invests = []
for i in Invest_List:
    invests.append(INVEST(i))

Invest_List = invests

return_list = []
Invest_Avialbe = []
for i in range(len(Invest_List)):
    if Invest_List[i].GetCondition():
        return_list.append(Invest_List[i].GetReturn())
        Invest_Avialbe.append(Invest_List[i])

return ([Invest_Avialbe[return_list.index(max(return_list))].invest,
         Invest_Avialbe[return_list.index(max(return_list))].GetReturn(),
         Invest_Avialbe[return_list.index(max(return_list))].GetOutlay()])





