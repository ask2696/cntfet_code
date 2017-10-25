# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:56:41 2017

@author: chetan and M.B.Srinivas
"""
def Gen_CyclicFun(inputs1,terms1,templistin1):
    orList=[]
    for i in range(inputs1):
        andlist=[]
        for j in range(terms1):
            andlist.append(templistin1[(j+i)%inputs1])
        #print(andlist)
        orList.append(min(andlist))
    #print(orList)
    return max(orList)

def CountV(value,listx):
    
    Count=0;
    for i in listx:
        if(i==value):
            Count=Count+1
    return Count 

def LeastCost1(node,map_dict1):
    Child_Graph1=dict();
    #Minimation = 0
    if (node=='X0'):
        Child_Graph1 = { "FX0" : []}
        if((map_dict1['F00']==map_dict1['F10']) and (map_dict1['F10']==map_dict1['F20'])):
            Child_Graph1["FX0"]=['F00']
            Child_Graph1.update({'F00':[map_dict1['F00']]})
        elif((map_dict1['F00'] == 0) and (map_dict1['F10'] == 1) and (map_dict1['F20'] == 2)):
            Child_Graph1.update({'FX0':['X']})
        elif((map_dict1['F00'] == 2) and (map_dict1['F10'] == 2) and (map_dict1['F20'] == 0)):
            Child_Graph1.update({'FX0':['PTIX']})
        elif((map_dict1['F00'] == 2) and (map_dict1['F10'] == 0) and (map_dict1['F20'] == 0)):
            Child_Graph1.update({'FX0':['NTIX']})
        elif((map_dict1['F00'] == 0) and (map_dict1['F10'] == 0) and (map_dict1['F20'] == 2)):
            Child_Graph1.update({'FX0':['PTIXB']})
        elif((map_dict1['F00'] == 0) and (map_dict1['F10'] == 2) and (map_dict1['F20'] == 2)):
            Child_Graph1.update({'FX0':['NTIXB']})
        elif((map_dict1['F00'] == 2) and (map_dict1['F10'] == 0)):
            Child_Graph1.update({'FX0':['F010','F20']})
            Child_Graph1.update({'F010':['NTIX']})
            Child_Graph1.update({'F20':[map_dict1['F20']]})
        elif((map_dict1['F10'] == 2) and (map_dict1['F20'] == 0)):
            Child_Graph1.update({'FX0':['F00','F120']})
            Child_Graph1.update({'F120':['PTIX']})
            Child_Graph1.update({'F00':[map_dict1['F00']]})
        elif((map_dict1['F00'] == 0) and (map_dict1['F10'] == 2)):
            Child_Graph1.update({'FX0':['F010','F20']})
            Child_Graph1.update({'F010':['NTIXB']})
            Child_Graph1.update({'F20':[map_dict1['F20']]})
        elif((map_dict1['F10'] == 0) and (map_dict1['F20'] == 2)):
            Child_Graph1.update({'FX0':['F00','F120']})
            Child_Graph1.update({'F120':['PTIXB']})
            Child_Graph1.update({'F00':[map_dict1['F00']]})
        elif(map_dict1['F00']==map_dict1['F10']):
            Child_Graph1["FX0"]=['F010','F20']
            Child_Graph1.update({'F010':[map_dict1['F00']]})
            Child_Graph1.update({'F20':[map_dict1['F20']]})
                    #Minimation = 1
        elif(map_dict1['F10']==map_dict1['F20']):
            Child_Graph1["FX0"]=['F00','F120']
            Child_Graph1.update({'F120':[map_dict1['F10']]})
            Child_Graph1.update({'F00':[map_dict1['F00']]})
                    #Minimation = 1
        else:
            Child_Graph1["FX0"]=['F00','F120']
            Child_Graph1.update({'F120':['F10','F20']})
            Child_Graph1.update({'F00':[map_dict1['F00']]})
            Child_Graph1.update({'F10':[map_dict1['F10']]})
            Child_Graph1.update({'F20':[map_dict1['F20']]})
                    
    if (node=='0Y'):
        Child_Graph1 = { "F0Y" : []}
        if((map_dict1['F00']==map_dict1['F01'])and (map_dict1['F01']==map_dict1['F02'])):
            Child_Graph1["F0Y"]=['F00']
            Child_Graph1.update({'F00':[map_dict1['F00']]})
        elif((map_dict1['F00'] == 0) and (map_dict1['F01'] == 1) and (map_dict1['F02'] == 2)):
            Child_Graph1.update({'F0Y':['Y']})
        elif((map_dict1['F00'] == 2) and (map_dict1['F01'] == 2) and (map_dict1['F02'] == 0)):
            Child_Graph1.update({'F0Y':['PTIY']})
        elif((map_dict1['F00'] == 2) and (map_dict1['F01'] == 0) and (map_dict1['F02'] == 0)):
            Child_Graph1.update({'F0Y':['NTIY']})
        elif((map_dict1['F00'] == 0) and (map_dict1['F01'] == 0) and (map_dict1['F02'] == 2)):
            Child_Graph1.update({'F0Y':['PTIYB']})
        elif((map_dict1['F00'] == 0) and (map_dict1['F01'] == 2) and (map_dict1['F02'] == 2)):
            Child_Graph1.update({'F0Y':['NTIYB']})
        elif((map_dict1['F00'] == 2) and (map_dict1['F01'] == 0)):
            Child_Graph1.update({'F0Y':['F001','F02']})
            Child_Graph1.update({'F001':['NTIY']})
            Child_Graph1.update({'F02':[map_dict1['F02']]})
        elif((map_dict1['F01'] == 2) and (map_dict1['F02'] == 0)):
            Child_Graph1.update({'F0Y':['F00','F012']})
            Child_Graph1.update({'F012':['PTIY']})
            Child_Graph1.update({'F00':[map_dict1['F00']]})
        elif((map_dict1['F00'] == 0) and (map_dict1['F01'] == 2)):
            Child_Graph1.update({'F0Y':['F001','F02']})
            Child_Graph1.update({'F001':['NTIYB']})
            Child_Graph1.update({'F02':[map_dict1['F02']]})
        elif((map_dict1['F01'] == 0) and (map_dict1['F02'] == 2)):
            Child_Graph1.update({'F0Y':['F00','F012']})
            Child_Graph1.update({'F012':['PTIYB']})
            Child_Graph1.update({'F00':[map_dict1['F00']]})
        elif(map_dict1['F00']==map_dict1['F01']):
            Child_Graph1["F0Y"]=['F001','F02']
            Child_Graph1.update({'F001':[map_dict1['F00']]})
            Child_Graph1.update({'F02':[map_dict1['F02']]})
                    #Minimation = 1
        elif(map_dict1['F01']==map_dict1['F02']):
            Child_Graph1["F0Y"]=['F00','F012']
            Child_Graph1.update({'F012':[map_dict1['F01']]})
            Child_Graph1.update({'F00':[map_dict1['F00']]})
                    #Minimation = 1
        else:
            Child_Graph1["F0Y"]=['F00','F012']
            Child_Graph1.update({'F012':['F01','F02']})
            Child_Graph1.update({'F00':[map_dict1['F00']]})
            Child_Graph1.update({'F01':[map_dict1['F01']]})
            Child_Graph1.update({'F02':[map_dict1['F02']]})
            
    if (node=='X2'):
        Child_Graph1 = { "FX2" : []}
        if((map_dict1['F02']==map_dict1['F12']) and (map_dict1['F12']==map_dict1['F22'])):
            Child_Graph1["FX2"]=['F22']
            Child_Graph1.update({'F22':[map_dict1['F22']]})
        elif((map_dict1['F02'] == 0) and (map_dict1['F12'] == 1) and (map_dict1['F22'] == 2)):
            Child_Graph1.update({'FX2':['X']})
        elif((map_dict1['F02'] == 2) and (map_dict1['F12'] == 2) and (map_dict1['F22'] == 0)):
            Child_Graph1.update({'FX2':['PTIX']})
        elif((map_dict1['F02'] == 2) and (map_dict1['F12'] == 0) and (map_dict1['F22'] == 0)):
            Child_Graph1.update({'FX2':['NTIX']})
        elif((map_dict1['F02'] == 0) and (map_dict1['F12'] == 0) and (map_dict1['F22'] == 2)):
            Child_Graph1.update({'FX2':['PTIXB']})
        elif((map_dict1['F02'] == 0) and (map_dict1['F12'] == 2) and (map_dict1['F22'] == 2)):
            Child_Graph1.update({'FX2':['NTIXB']})
        elif((map_dict1['F02'] == 2) and (map_dict1['F12'] == 0)):
            Child_Graph1.update({'FX2':['F012','F22']})
            Child_Graph1.update({'F012':['NTIX']})
            Child_Graph1.update({'F22':[map_dict1['F22']]})
        elif((map_dict1['F12'] == 2) and (map_dict1['F22'] == 0)):
            Child_Graph1.update({'FX2':['F02','F122']})
            Child_Graph1.update({'F122':['PTIX']})
            Child_Graph1.update({'F02':[map_dict1['F02']]})
        elif((map_dict1['F02'] == 0) and (map_dict1['F12'] == 2)):
            Child_Graph1.update({'FX2':['F012','F22']})
            Child_Graph1.update({'F012':['NTIXB']})
            Child_Graph1.update({'F22':[map_dict1['F22']]})
        elif((map_dict1['F12'] == 0) and (map_dict1['F22'] == 2)):
            Child_Graph1.update({'FX2':['F02','F122']})
            Child_Graph1.update({'F122':['PTIXB']})
            Child_Graph1.update({'F02':[map_dict1['F02']]})
        elif(map_dict1['F02']==map_dict1['F12']):
            Child_Graph1["FX2"]=['F012','F22']
            Child_Graph1.update({'F012':[map_dict1['F02']]})
            Child_Graph1.update({'F22':[map_dict1['F22']]})
                    #Minimation = 1
        elif(map_dict1['F12']==map_dict1['F22']):
            Child_Graph1["FX2"]=['F02','F122']
            Child_Graph1.update({'F122':[map_dict1['F12']]})
            Child_Graph1.update({'F02':[map_dict1['F02']]})
                    #Minimation = 1
        else:
            Child_Graph1["FX2"]=['F02','F122']
            Child_Graph1.update({'F122':['F12','F22']})
            Child_Graph1.update({'F02':[map_dict1['F02']]})
            Child_Graph1.update({'F12':[map_dict1['F12']]})
            Child_Graph1.update({'F22':[map_dict1['F22']]})
                    
    if (node=='2Y'):
        Child_Graph1 = { "F2Y" : []}
        if((map_dict1['F20']==map_dict1['F21'])and (map_dict1['F21']==map_dict1['F22'])):
            Child_Graph1["F2Y"]=['F22']
            Child_Graph1.update({'F22':[map_dict1['F22']]})
        elif((map_dict1['F20'] == 0) and (map_dict1['F21'] == 1) and (map_dict1['F22'] == 2)):
            Child_Graph1.update({'F2Y':['Y']})
        elif((map_dict1['F20'] == 2) and (map_dict1['F21'] == 2) and (map_dict1['F22'] == 0)):
            Child_Graph1.update({'F2Y':['PTIY']})
        elif((map_dict1['F20'] == 2) and (map_dict1['F21'] == 0) and (map_dict1['F22'] == 0)):
            Child_Graph1.update({'F2Y':['NTIY']})
        elif((map_dict1['F20'] == 0) and (map_dict1['F21'] == 0) and (map_dict1['F22'] == 2)):
            Child_Graph1.update({'F2Y':['PTIYB']})
        elif((map_dict1['F20'] == 0) and (map_dict1['F21'] == 2) and (map_dict1['F22'] == 2)):
            Child_Graph1.update({'F2Y':['NTIYB']})
        elif((map_dict1['F20'] == 2) and (map_dict1['F21'] == 0)):
            Child_Graph1.update({'F2Y':['F201','F22']})
            Child_Graph1.update({'F201':['NTIY']})
            Child_Graph1.update({'F22':[map_dict1['F22']]})
        elif((map_dict1['F21'] == 2) and (map_dict1['F22'] == 0)):
            Child_Graph1.update({'F2Y':['F20','F212']})
            Child_Graph1.update({'F212':['PTIY']})
            Child_Graph1.update({'F20':[map_dict1['F20']]})
        elif((map_dict1['F20'] == 0) and (map_dict1['F21'] == 2)):
            Child_Graph1.update({'F2Y':['F201','F22']})
            Child_Graph1.update({'F201':['NTIYB']})
            Child_Graph1.update({'F22':[map_dict1['F22']]})
        elif((map_dict1['F21'] == 0) and (map_dict1['F22'] == 2)):
            Child_Graph1.update({'F2Y':['F20','F212']})
            Child_Graph1.update({'F212':['PTIYB']})
            Child_Graph1.update({'F20':[map_dict1['F20']]})
        elif(map_dict1['F20']==map_dict1['F21']):
            Child_Graph1["F2Y"]=['F201','F22']
            Child_Graph1.update({'F201':[map_dict1['F20']]})
            Child_Graph1.update({'F22':[map_dict1['F22']]})
                    #Minimation = 1
        elif(map_dict1['F21']==map_dict1['F22']):
            Child_Graph1["F2Y"]=['F20','F212']
            Child_Graph1.update({'F212':[map_dict1['F21']]})
            Child_Graph1.update({'F20':[map_dict1['F20']]})
                    #Minimation = 1
        else:
            Child_Graph1["F2Y"]=['F20','F212']
            Child_Graph1.update({'F212':['F21','F22']})
            Child_Graph1.update({'F20':[map_dict1['F20']]})
            Child_Graph1.update({'F21':[map_dict1['F21']]})
            Child_Graph1.update({'F22':[map_dict1['F22']]})
    

    if (node=='X1'):
        Child_Graph1 = { "FX1" : []}
        if((map_dict1['F01']==map_dict1['F11']) and (map_dict1['F11']==map_dict1['F21'])):
            Child_Graph1["FX1"]=['F11']
            Child_Graph1.update({'F11':[map_dict1['F11']]})
        elif((map_dict1['F01'] == 0) and (map_dict1['F11'] == 1) and (map_dict1['F21'] == 2)):
            Child_Graph1.update({'FX1':['X']})
        elif((map_dict1['F01'] == 2) and (map_dict1['F11'] == 2) and (map_dict1['F21'] == 0)):
            Child_Graph1.update({'FX1':['PTIX']})
        elif((map_dict1['F01'] == 2) and (map_dict1['F11'] == 0) and (map_dict1['F21'] == 0)):
            Child_Graph1.update({'FX1':['NTIX']})
        elif((map_dict1['F01'] == 0) and (map_dict1['F11'] == 0) and (map_dict1['F21'] == 2)):
            Child_Graph1.update({'FX1':['PTIXB']})
        elif((map_dict1['F01'] == 0) and (map_dict1['F11'] == 2) and (map_dict1['F21'] == 2)):
            Child_Graph1.update({'FX1':['NTIXB']})
        elif((map_dict1['F01'] == 2) and (map_dict1['F11'] == 0)):
            Child_Graph1.update({'FX1':['F011','F21']})
            Child_Graph1.update({'F011':['NTIX']})
            Child_Graph1.update({'F21':[map_dict1['F21']]})
        elif((map_dict1['F11'] == 2) and (map_dict1['F21'] == 0)):
            Child_Graph1.update({'FX1':['F01','F121']})
            Child_Graph1.update({'F121':['PTIX']})
            Child_Graph1.update({'F01':[map_dict1['F01']]})
        elif((map_dict1['F01'] == 0) and (map_dict1['F11'] == 2)):
            Child_Graph1.update({'FX1':['F011','F21']})
            Child_Graph1.update({'F011':['NTIXB']})
            Child_Graph1.update({'F21':[map_dict1['F21']]})
        elif((map_dict1['F11'] == 0) and (map_dict1['F21'] == 2)):
            Child_Graph1.update({'FX1':['F01','F121']})
            Child_Graph1.update({'F121':['PTIXB']})
            Child_Graph1.update({'F01':[map_dict1['F01']]})
        elif(map_dict1['F01']==map_dict1['F11']):
            Child_Graph1["FX1"]=['F011','F21']
            Child_Graph1.update({'F011':[map_dict1['F01']]})
            Child_Graph1.update({'F21':[map_dict1['F21']]})
                    #Minimation = 1
        elif(map_dict1['F11']==map_dict1['F21']):
            Child_Graph1["FX1"]=['F01','F121']
            Child_Graph1.update({'F121':[map_dict1['F11']]})
            Child_Graph1.update({'F01':[map_dict1['F01']]})
                    #Minimation = 1
        else:
            Child_Graph1["FX1"]=['F01','F121']
            Child_Graph1.update({'F121':['F11','F21']})
            Child_Graph1.update({'F01':[map_dict1['F01']]})
            Child_Graph1.update({'F11':[map_dict1['F11']]})
            Child_Graph1.update({'F21':[map_dict1['F21']]})
                    
    if (node=='1Y'):
        Child_Graph1 = { "F1Y" : []}
        if((map_dict1['F10']==map_dict1['F11'])and (map_dict1['F11']==map_dict1['F12'])):
            Child_Graph1["F1Y"]=['F11']
            Child_Graph1.update({'F11':[map_dict1['F11']]})
        elif((map_dict1['F10'] == 0) and (map_dict1['F11'] == 1) and (map_dict1['F12'] == 2)):
            Child_Graph1.update({'F1Y':['Y']})
        elif((map_dict1['F10'] == 2) and (map_dict1['F11'] == 2) and (map_dict1['F12'] == 0)):
            Child_Graph1.update({'F1Y':['PTIY']})
        elif((map_dict1['F10'] == 2) and (map_dict1['F11'] == 0) and (map_dict1['F12'] == 0)):
            Child_Graph1.update({'F1Y':['NTIY']})
        elif((map_dict1['F10'] == 0) and (map_dict1['F11'] == 0) and (map_dict1['F12'] == 2)):
            Child_Graph1.update({'F1Y':['PTIYB']})
        elif((map_dict1['F10'] == 0) and (map_dict1['F11'] == 2) and (map_dict1['F12'] == 2)):
            Child_Graph1.update({'F1Y':['NTIYB']})
        elif((map_dict1['F10'] == 2) and (map_dict1['F11'] == 0)):
            Child_Graph1.update({'F1Y':['F101','F12']})
            Child_Graph1.update({'F101':['NTIY']})
            Child_Graph1.update({'F12':[map_dict1['F12']]})
        elif((map_dict1['F11'] == 2) and (map_dict1['F12'] == 0)):
            Child_Graph1.update({'F1Y':['F10','F112']})
            Child_Graph1.update({'F112':['PTIY']})
            Child_Graph1.update({'F10':[map_dict1['F10']]})
        elif((map_dict1['F10'] == 0) and (map_dict1['F11'] == 2)):
            Child_Graph1.update({'F1Y':['F101','F12']})
            Child_Graph1.update({'F101':['NTIYB']})
            Child_Graph1.update({'F12':[map_dict1['F12']]})
        elif((map_dict1['F11'] == 0) and (map_dict1['F12'] == 2)):
            Child_Graph1.update({'F1Y':['F10','F112']})
            Child_Graph1.update({'F112':['PTIYB']})
            Child_Graph1.update({'F10':[map_dict1['F10']]})
        elif(map_dict1['F10']==map_dict1['F11']):
            Child_Graph1["F1Y"]=['F101','F12']
            Child_Graph1.update({'F101':[map_dict1['F10']]})
            Child_Graph1.update({'F12':[map_dict1['F12']]})
        elif(map_dict1['F11']==map_dict1['F12']):
            Child_Graph1["F1Y"]=['F10','F112']
            Child_Graph1.update({'F112':[map_dict1['F11']]})
            Child_Graph1.update({'F10':[map_dict1['F10']]})
            Child_Graph1.update({'F12':[map_dict1['F12']]})
                    #Minimation = 1
                    #Minimation = 1
        else:
            Child_Graph1["F1Y"]=['F10','F112']
            Child_Graph1.update({'F112':['F11','F12']})
            Child_Graph1.update({'F10':[map_dict1['F10']]})
            Child_Graph1.update({'F11':[map_dict1['F11']]})
            Child_Graph1.update({'F12':[map_dict1['F12']]})
            
    return Child_Graph1;
    
def LeastCost2(node,map_dict2):
    Child_Graph2=dict();
    if (node =='X01'):
        equal=1
        for i in [0,1,2]:
            for j in [0,1]:
                if(map_dict2['F'+str(i)+str(j)]!=map_dict2['F00']):
                    equal=0;
        if(equal==1):
            Child_Graph2["FX01"] =[map_dict2['F00']]
        elif(map_dict2['F00']==map_dict2['F01']) and (map_dict2['F10']==map_dict2['F11']) and (map_dict2['F20']==map_dict2['F21']):
            Child_Graph2["FX01"]=['FX0']
            Child_Graph2.update(LeastCost1('X0',map_dict2))
        elif((map_dict2['F00']==map_dict2['F01']) and (map_dict2['F01']==map_dict2['F11']) and (map_dict2['F11']==map_dict2['F00'])):
            Child_Graph2["FX01"] = ['F0101','F201']
            Child_Graph2.update({ "F0101" : [map_dict2['F00']]})
            Child_Graph2.update({ "F201" : ['F20','F21']})
            Child_Graph2.update({ "F20" : [map_dict2['F20']]})
            Child_Graph2.update({ "F21" : [map_dict2['F21']]})
        elif((map_dict2['F10']==map_dict2['F11']) and (map_dict2['F11']==map_dict2['F21']) and (map_dict2['F21']==map_dict2['F20'])):
            Child_Graph2["FX01"] = ['F001','F1201']
            Child_Graph2.update({ "F1201" : [map_dict2['F10']]})
            Child_Graph2.update({ "F001" : ['F00','F01']})
            Child_Graph2.update({ "F00" : [map_dict2['F00']]})
            Child_Graph2.update({ "F01" : [map_dict2['F01']]})
        else:
            Child_Graph2["FX01"] =['FX0','FX1']
            Child_Graph2.update(LeastCost1('X0',map_dict2))
            Child_Graph2.update(LeastCost1('X1',map_dict2))
    elif(node=='X12'):
        #print ('in X12')
        equal=1
        for i in [0,1,2]:
            for j in [1,2]:
                if(map_dict2['F'+str(i)+str(j)]!=map_dict2['F22']):
                    equal=0;
        if(equal==1):
            #print ('0 X12')
            Child_Graph2["FX12"]=[map_dict2['F22']]
        elif(map_dict2['F01']==map_dict2['F02']) and (map_dict2['F11']==map_dict2['F12']) and (map_dict2['F21']==map_dict2['F22']):
            #print ('1 X12')
            Child_Graph2["FX12"]=['FX2']
            Child_Graph2.update(LeastCost1('X1',map_dict2))
        elif((map_dict2['F01']==map_dict2['F02']) and (map_dict2['F02']==map_dict2['F12']) and (map_dict2['F12']==map_dict2['F11'])):
            #print ('2 X12')
            Child_Graph2["FX12"]=['F0112','F212']
            #print ('21 X12')
            Child_Graph2.update({ "F0112" : [map_dict2['F01']]})
            Child_Graph2.update({ "F212" : ['F21','F22']})
            Child_Graph2.update({ "F21" : [map_dict2['F21']]})
            Child_Graph2.update({ "F22" : [map_dict2['F22']]})
        elif((map_dict2['F11']==map_dict2['F12']) and (map_dict2['F12']==map_dict2['F22']) and (map_dict2['F22']==map_dict2['F21'])):
            #print ('3 X12')
            Child_Graph2["FX12"]=['F012','F1212']
            Child_Graph2.update({ "F1212" : [map_dict2['F11']]})
            Child_Graph2.update({ "F012" : ['F01','F02']})
            Child_Graph2.update({ "F01" : [map_dict2['F01']]})
            Child_Graph2.update({ "F02" : [map_dict2['F02']]})
        else:
            #print ('4 X12')
            Child_Graph2["FX12"]=['FX1','FX2']
            Child_Graph2.update(LeastCost1('X1',map_dict2))
            Child_Graph2.update(LeastCost1('X2',map_dict2))
    elif(node=='01Y'):
        equal=1
        for i in [0,1]:
            for j in [0,1,2]:
                if(map_dict2['F'+str(i)+str(j)]!=map_dict2['F00']):
                    equal=0;
        if(equal==1):
            Child_Graph2["F01Y"]=[map_dict2['F00']]
        elif(map_dict2['F00']==map_dict2['F10']) and (map_dict2['F01']==map_dict2['F11']) and (map_dict2['F02']==map_dict2['F12']):
            #print('Test')            
            Child_Graph2["F01Y"]=['F0Y']
            Child_Graph2.update(LeastCost1('0Y',map_dict2))
        elif((map_dict2['F00']==map_dict2['F10']) and (map_dict2['F10']==map_dict2['F11']) and (map_dict2['F11']==map_dict2['F00'])):
            Child_Graph2["F01Y"]=['F0101','F012']
            Child_Graph2.update({ "F0101" : [map_dict2['F00']]})
            Child_Graph2.update({ "F012" : ['F02','F12']})
            Child_Graph2.update({ "F02" : [map_dict2['F02']]})
            Child_Graph2.update({ "F12" : [map_dict2['F12']]})
        elif((map_dict2['F01']==map_dict2['F11']) and (map_dict2['F11']==map_dict2['F12']) and (map_dict2['F12']==map_dict2['F02'])):
            Child_Graph2["F01Y"]=['F010','F0112']
            Child_Graph2.update({ "F0112" : [map_dict2['F01']]})
            Child_Graph2.update({ "F010" : ['F00','F10']})
            Child_Graph2.update({ "F00" : [map_dict2['F00']]})
            Child_Graph2.update({ "F10" : [map_dict2['F10']]})
        else:
            Child_Graph2["F01Y"]=['F0Y','F1Y']
            Child_Graph2.update(LeastCost1('0Y',map_dict2))
            Child_Graph2.update(LeastCost1('1Y',map_dict2))
    elif(node=='12Y'):
        equal=1
        for i in [1,2]:
            for j in [0,1,2]:
                if(map_dict2['F'+str(i)+str(j)]!=map_dict2['F22']):
                    equal=0;
        if(equal==1):
            Child_Graph2["F12Y"]=[map_dict2['F22']]
        elif(map_dict2['F10']==map_dict2['F20']) and (map_dict2['F11']==map_dict2['F21']) and (map_dict2['F12']==map_dict2['F22']):
            Child_Graph2["F12Y"]=['F2Y']
            Child_Graph2.update(LeastCost1('2Y',map_dict2))
        elif((map_dict2['F10']==map_dict2['F20']) and (map_dict2['F20']==map_dict2['F21']) and (map_dict2['F21']==map_dict2['F11'])):
            Child_Graph2["F12Y"]=['F1201','F122']
            Child_Graph2.update({ "F1201" : [map_dict2['F10']]})
            Child_Graph2.update({ "F122" : ['F12','F22']})
            Child_Graph2.update({ "F12" : [map_dict2['F12']]})
            Child_Graph2.update({ "F22" : [map_dict2['F22']]})
        elif((map_dict2['F11']==map_dict2['F21']) and (map_dict2['F21']==map_dict2['F22']) and (map_dict2['F22']==map_dict2['F12'])):
            Child_Graph2["F12Y"]=['F120','F1212']
            Child_Graph2.update({ "F1212" : [map_dict2['F11']]})
            Child_Graph2.update({ "F120" : ['F10','F20']})
            Child_Graph2.update({ "F10" : [map_dict2['F10']]})
            Child_Graph2.update({ "F20" : [map_dict2['F20']]})
        else:
            Child_Graph2["F12Y"]=['F1Y','F2Y']
            Child_Graph2.update(LeastCost1('1Y',map_dict2))
            Child_Graph2.update(LeastCost1('2Y',map_dict2))
    return Child_Graph2;

def Minimize(listout,map_dict):
    
    BTDD_graph = { "FXY" : []}
    Minimation = 0;
	#Rule 0
    X01equal=1
    X12equal=1
    Y01equal=1
    Y12equal=1
    for i in [0,1,2]:
        for j in [0,1]:
            if(map_dict['F'+str(i)+str(j)]!=map_dict['F00']):
                X01equal=0;
    for i in [0,1,2]:
        for j in [1,2]:
            if(map_dict['F'+str(i)+str(j)]!=map_dict['F22']):
                X12equal=0;
    for i in [0,1]:
        for j in [0,1,2]:
            if(map_dict['F'+str(i)+str(j)]!=map_dict['F00']):
                Y01equal=0;
    for i in [1,2]:
         for j in [0,1,2]:
            if(map_dict['F'+str(i)+str(j)]!=map_dict['F22']):
                Y12equal=0;
                
                    
    if(X01equal==1):
        BTDD_graph["FXY"]=['FX01','FX2']
        Minimation = 1;
    elif(X12equal==1):
        BTDD_graph["FXY"]=['FX0','FX12']
        Minimation = 1;
    elif(Y01equal==1):
        BTDD_graph["FXY"]=['F01Y','F2Y']
        Minimation = 1;
    elif(Y12equal==1):
        BTDD_graph["FXY"]=['F0Y','F12Y']
        Minimation = 1;
          
    elif(map_dict['F00']==map_dict['F10']) and (map_dict['F01']==map_dict['F11']) and (map_dict['F02']==map_dict['F12']):
        #print("X01 2")
        BTDD_graph["FXY"]=['F01Y','F2Y']
        Minimation = 1;
		#BTDD_graph.update({'F01Y':[],'F2Y':[]})
	
    elif(map_dict['F10']==map_dict['F20']) and (map_dict['F11']==map_dict['F21']) and (map_dict['F12']==map_dict['F22']):
		#print("X0 12")
        BTDD_graph["FXY"]=['F0Y','F12Y']
        Minimation = 1;
			#BTDD_graph.update({'F0Y':[],'F12Y':[]})
    elif(map_dict['F00']==map_dict['F01']) and (map_dict['F10']==map_dict['F11']) and (map_dict['F20']==map_dict['F21']):
		#print("Y01 2")
        BTDD_graph["FXY"]=['FX01','FX2']
        Minimation = 1;
				#BTDD_graph.update({'FX01':[],'FX2':[]})
    elif(map_dict['F01']==map_dict['F02']) and (map_dict['F11']==map_dict['F12']) and (map_dict['F21']==map_dict['F22']):
		#print("Y0 12")
        BTDD_graph["FXY"]=['FX0','FX12']
        Minimation = 1;
					#BTDD_graph.update({'FX0':[],'FX12':[]})
    else:
		#Rule 1
        RowCol = [0,2]
        for i in RowCol:
            # Check for equal Row
            if(map_dict['F'+str(i)+'0'] == map_dict['F'+str(i)+'1']) and (map_dict['F'+str(i)+'0'] == map_dict['F'+str(i)+'2']):
                
				#SameRow=i;
                if (i==0):
                    					#print("one row X0 12")
                    BTDD_graph["FXY"]=['F0Y','F12Y']
                    Minimation = 1;
								#BTDD_graph.update({'F0Y':[],'F12Y':[]})
                else:
                    #print("one row X01 2")
                    BTDD_graph["FXY"]=['F01Y','F2Y']
                    Minimation = 1;
								#BTDD_graph.update({'F01Y':[],'F2Y':[]})
            elif((map_dict['F'+str(i)+'0'] == 0) and (map_dict['F'+str(i)+'1'] == 1) and (map_dict['F'+str(i)+'2'] == 2)):
                if (i==0):
					#print("one row X0 12 012")
                    BTDD_graph["FXY"]=['F0Y','F12Y']
                    Minimation = 1;
                else:
                    #print("one row X01 2 012")
                    BTDD_graph["FXY"]=['F01Y','F2Y']
                    Minimation = 1;
							# Check for equal Column
            elif((map_dict['F'+str(i)+'0'] == 0) and ((map_dict['F'+str(i)+'1'] == 2) or (map_dict['F'+str(i)+'1'] == 0)) and (map_dict['F'+str(i)+'2'] == 2)):
                if (i==0):
					#print("one row X0 12 012")
                    BTDD_graph["FXY"]=['F0Y','F12Y']
                    Minimation = 1;
                else:
                    #print("one row X01 2 012")
                    BTDD_graph["FXY"]=['F01Y','F2Y']
                    Minimation = 1;
            elif((map_dict['F'+str(i)+'0'] == 2) and ((map_dict['F'+str(i)+'1'] == 2) or (map_dict['F'+str(i)+'1'] == 0)) and (map_dict['F'+str(i)+'2'] == 0)):
                if (i==0):
					#print("one row X0 12 012")
                    BTDD_graph["FXY"]=['F0Y','F12Y']
                    Minimation = 1;
                else:
                    #print("one row X01 2 012")
                    BTDD_graph["FXY"]=['F01Y','F2Y']
                    Minimation = 1;
            elif(map_dict['F0'+str(i)] == map_dict['F1'+str(i)]) and (map_dict['F0'+str(i)] == map_dict['F2'+str(i)]):
				#SameCol=i;
                if (i==0):
					#print("one col Y0 12")
                    BTDD_graph["FXY"]=['FX0','FX12']
                    Minimation = 1;
									#BTDD_graph.update({'FX0':[],'FX12':[]})
                else:
					#print("one col Y01 2")
                    BTDD_graph["FXY"]=['FX01','FX2']
                    Minimation = 1;
									#BTDD_graph.update({'FX01':[],'FX2':[]})
            elif((map_dict['F0'+str(i)] == 0) and (map_dict['F1'+str(i)] == 1) and (map_dict['F2'+str(i)] == 2)):
                if (i==0):
					#print("one col Y0 12 012")
                    BTDD_graph["FXY"]=['FX0','FX12']
                    Minimation = 1;
                else:
					#print("one col Y01 2 012")
                    BTDD_graph["FXY"]=['FX01','FX2']
                    Minimation = 1;
            elif((map_dict['F0'+str(i)] == 0) and ((map_dict['F1'+str(i)] == 2) or (map_dict['F1'+str(i)] == 0))  and (map_dict['F2'+str(i)] == 2)):
                if (i==0):
					#print("one col Y0 12 012")
                    BTDD_graph["FXY"]=['FX0','FX12']
                    Minimation = 1;
                else:
					#print("one col Y01 2 012")
                    BTDD_graph["FXY"]=['FX01','FX2']
                    Minimation = 1;
            elif((map_dict['F0'+str(i)] == 2) and ((map_dict['F1'+str(i)] == 2) or (map_dict['F1'+str(i)] == 0))  and (map_dict['F2'+str(i)] == 0)):
                if (i==0):
					#print("one col Y0 12 012")
                    BTDD_graph["FXY"]=['FX0','FX12']
                    Minimation = 1;
                else:
					#print("one col Y01 2 012")
                    BTDD_graph["FXY"]=['FX01','FX2']
                    Minimation = 1;
    if(Minimation == 0):
		#print('no options')
        BTDD_graph["FXY"]=['FX0','FX12']
								#BTDD_graph.update({'FX0':[],'FX12':[]})
    Child_graph=dict();   
    for i in BTDD_graph['FXY']:
        if ('X' in i):
            if ('0' in i) and not('01' in i):
				#X0 row minimzation
                #print ('X0')
                Child_graph=LeastCost1('X0',map_dict) #Rule 2
                BTDD_graph.update(Child_graph)
            if ('12' in i):
                #print ('X12')
                Child_graph=LeastCost2('X12',map_dict)
                #print (Child_graph)#Rule 3
                BTDD_graph.update(Child_graph)
                #print(BTDD_graph)
            if ('2' in i) and not('12' in i):
				#print ('X2')
                Child_graph=LeastCost1('X2',map_dict) #Rule 2
                BTDD_graph.update(Child_graph)
            if ('01' in i):
				#print ('X01')
                Child_graph=LeastCost2('X01',map_dict) #Rule 3
                BTDD_graph.update(Child_graph)
        if ('Y' in i):
            if ('0' in i) and not('01' in i):
				#print ('0Y')
                Child_graph=LeastCost1('0Y',map_dict) #Rule 2
                BTDD_graph.update(Child_graph)
            if ('12' in i):
				#print ('12Y')
                Child_graph=LeastCost2('12Y',map_dict) #Rule 3
                BTDD_graph.update(Child_graph)
            if ('2' in i) and not('12' in i):
				#print ('2Y')
                Child_graph=LeastCost1('2Y',map_dict) #Rule 2
                BTDD_graph.update(Child_graph)
            if ('01' in i):
				#print ('01Y')
                Child_graph=LeastCost2('01Y',map_dict) #Rule 3
                BTDD_graph.update(Child_graph)
    equal=0;
    for i in range(len(listout)-1):
        if(listout[i]==listout[i+1]):
            equal=1;
        else:
            equal=0;
            break
    if (equal==1):
        #print('Test1')
        BTDD_graph.clear()
        BTDD_graph={'FXY':[listout[0]]}
    return BTDD_graph    

def get_Cost(Graph):
    No_Mux=0
    list_nod_w2E=[]
    for i in Graph:
        if (len(Graph[i])==2):
            No_Mux=No_Mux+1;
            list_nod_w2E.append(i)
    for i in list_nod_w2E:
        if((Graph[Graph[i][0]]==[0]) and (Graph[Graph[i][1]]==[2])) or ((Graph[Graph[i][0]]==[2]) and (Graph[Graph[i][1]]==[0])):
            No_Mux=No_Mux-1
    return No_Mux


def Check_Equal(listx):
    return len(set(listx)) <= 1
    
def Minimize2(listout,node):
    listin1=[0,1,2]
    map_dict1=dict();
    for k in range(len(listout)):
        map_dict1["F"+str(listin1[k])]=listout[k]
    Child_Graph1 = { 'F'+node : []}
    #Minimation = 0;
    if((map_dict1['F0']==map_dict1['F1']) and (map_dict1['F1']==map_dict1['F2'])):
        Child_Graph1['F'+node]=[map_dict1['F0']]
        #Child_Graph1.update({'F0':[map_dict1['F0']]})
    elif((map_dict1['F0'] == 0) and (map_dict1['F1'] == 1) and (map_dict1['F2'] == 2)):
        Child_Graph1.update({'F'+node:[node]})
    elif((map_dict1['F0'] == 2) and (map_dict1['F1'] == 2) and (map_dict1['F2'] == 0)):
        Child_Graph1.update({'F'+node:['PTI'+node]})
    elif((map_dict1['F0'] == 2) and (map_dict1['F1'] == 0) and (map_dict1['F2'] == 0)):
        Child_Graph1.update({'F'+node:['NTI'+node]})
    elif((map_dict1['F0'] == 0) and (map_dict1['F1'] == 0) and (map_dict1['F2'] == 2)):
        Child_Graph1.update({'F'+node:['PTI'+node+'B']})
    elif((map_dict1['F0'] == 0) and (map_dict1['F1'] == 2) and (map_dict1['F2'] == 2)):
        Child_Graph1.update({'F'+node:['NTI'+node+'B']})
    elif((map_dict1['F0'] == 2) and (map_dict1['F1'] == 0)):
        Child_Graph1.update({'F'+node:['F01','F2']})
        Child_Graph1.update({'F01':['NTI'+node]})
        Child_Graph1.update({'F2':[map_dict1['F2']]})
    elif((map_dict1['F1'] == 2) and (map_dict1['F2'] == 0)):
        Child_Graph1.update({'F'+node:['F0','F12']})
        Child_Graph1.update({'F12':['PTI'+node]})
        Child_Graph1.update({'F0':[map_dict1['F0']]})
    elif((map_dict1['F0'] == 0) and (map_dict1['F1'] == 2)):
        Child_Graph1.update({'F'+node:['F01','F2']})
        Child_Graph1.update({'F01':['NTI'+node+'B']})
        Child_Graph1.update({'F2':[map_dict1['F2']]})
    elif((map_dict1['F1'] == 0) and (map_dict1['F2'] == 2)):
        Child_Graph1.update({'F'+node:['F0','F12']})
        Child_Graph1.update({'F12':['PTI'+node+'B']})
        Child_Graph1.update({'F0':[map_dict1['F0']]})
    elif(map_dict1['F0']==map_dict1['F1']):
        Child_Graph1['F'+node]=['F01','F2']
        Child_Graph1.update({'F01':[map_dict1['F0']]})
        Child_Graph1.update({'F2':[map_dict1['F2']]})
                    #Minimation = 1
    elif(map_dict1['F1']==map_dict1['F2']):
        Child_Graph1['F'+node]=['F0','F12']
        Child_Graph1.update({'F12':[map_dict1['F1']]})
        Child_Graph1.update({'F0':[map_dict1['F0']]})
                    #Minimation = 1
    else:
        Child_Graph1['F'+node]=['F0','F12']
        Child_Graph1.update({'F12':['F1','F2']})
        Child_Graph1.update({'F0':[map_dict1['F0']]})
        Child_Graph1.update({'F1':[map_dict1['F1']]})
        Child_Graph1.update({'F2':[map_dict1['F2']]})
    return Child_Graph1

def get_Cost2(Graph):
    No_Mux=0
    list_nod_w2E=[]
    for i in Graph:
        if (len(Graph[i])==2):
            No_Mux=No_Mux+1;
            list_nod_w2E.append(i)
            
    for i in list_nod_w2E:
        if((Graph[Graph[i][0]]==[0]) and (Graph[Graph[i][1]]==[2])) or ((Graph[Graph[i][0]]==[2]) and (Graph[Graph[i][1]]==[0])):
            No_Mux=No_Mux-1
    return No_Mux

#inputs and outputs   

fun = input("Enter the Function code ( 0-->Sum, 1-->Product, 2-->Avg, 3-->Count, 4-->Cyclic): ")
#fun=0  #[Fun 0-->Sum, 1-->Product, 2-->Avg, 3-->Count, 4-->Cyclic]
fun=int(fun)
inputs = input("Enter the number of inputs:")
inputs=int(inputs)

if(fun!=4):
    outputs = input("Enter the number of outputs:")
    outputs=int(outputs)

if(fun==4):
    outputs=1
    terms = input("Enter the number of terms in each product of cyclic function:")
    terms = int(terms)
#inputs =3;
#outputs=2;
#terms=5;
outputsh=(int(outputs/2))

#Generate Combinations
comb = int(pow(3,inputs));
in_dict=dict();
out_dict=dict();
listin=[];
#Generate Outputs
for i in range(comb):
    Sum1=0;
    prod=1
    templistout=[];
    templistin=[]
    for j in range (inputs):
        templistin.append((int(i/(pow(3,(inputs-1-j))))%3))
        Sum1=Sum1+(int(i/(pow(3,(inputs-1-j))))%3);
        prod=prod*(int(i/(pow(3,(inputs-1-j))))%3);
    listin.append(templistin)
    Count1=CountV(1,templistin)
    Count2=CountV(2,templistin)
    avg=(int(Sum1/inputs))
    if(fun==0):
        for k in range (outputs):
            templistout.append((int(Sum1/(pow(3,(outputs-1-k))))%3))
    elif(fun==1):
        for k in range (outputs):
            templistout.append((int(prod/(pow(3,(outputs-1-k))))%3))
    elif(fun==2):
        for k in range (outputs):
            templistout.append((int(avg/(pow(3,(outputs-1-k))))%3))
    elif(fun==3):
        for k in range (outputsh):
            templistout.append((int(Count1/(pow(3,(outputsh-1-k))))%3))
            templistout.append((int(Count2/(pow(3,(outputsh-1-k))))%3))
    elif(fun==4):
        templistout=[Gen_CyclicFun(inputs,terms,templistin)]
    out_dict[i]=templistout

#Make a List of outputs
out = [[] for x in range(outputs)]
for i in out_dict:
    for k in range(outputs):
        out[k].append(out_dict[i][k])

#This is required for 1 input Minimization         
listin1=[0,1,2]
listin2=[];
for i in range(int(pow(3,2))):
    templistin=[];
    for j in range (2):
        templistin.append((int(i/(pow(3,(2-1-j))))%3))
    listin2.append(templistin)

#Initialization
In_Cost3=0
In_Cost2x=0
#Testing for Single output Case
#outx=[out[1]]
Final_out=[]
#Graph Creation
#num=0
BTDD_In_Graph=dict()
Fun_map=dict()
Fun_map_Inv=dict()
#Testing for all outputs
#Input Mux-Mapping
#for k in [2]:
for k in range(len(out)):
    outx=[out[k]]
    In_Cost3temp=0
    In_Cost2temp=0
    inputx=inputs
    Fun_map.update({'F'+str(k)+'_'+str(inputx)+'_'+str(0):outx})
#Divide the ouput list in to 3 functions along MSB
    while (len(outx[0])>9):
        outy=[]

        for i in range(len(outx)):
            l=int(len(outx[i])/3)
            outy.append(outx[i][:l])
            outy.append(outx[i][l:2*l])
            outy.append(outx[i][2*l:])
        outx=[]
        
        m=0
        for i in outy:
            if i not in outx:
                outx.append(i)                #inputs-2
                Fun_map.update({'F'+str(k)+'_'+str(inputx-1)+'_'+str(m):i})
                m=m+1
        m=0
        for i in range(int(len(outy)/3)):
#        for i in range(int(len(outy)/9)):
            outz=[]
            outzF=[]
            for j in range(3):
#            for j in range(9):
                outz.append(outy[j+m])
                for key in Fun_map:
                    if(Fun_map[key]==outy[j+m]) and ('F'+str(k) in key):
                        outzF.append(key)
#            m=m+9
            m=m+3
            Graph_In=Minimize2(outzF,'In'+str(inputx))
            In_Cost2temp=In_Cost2temp+get_Cost2(Graph_In)
            BTDD_In_Graph.update({'F'+str(k)+'_'+str(inputx)+'_'+str(i):Graph_In})
                
#        for i in outx:
#            if(Check_Equal(i)):
#                outx.remove(i)
        inputx=inputx-1
#        inputx=inputx-2
                
    In_Cost2x=In_Cost2x+In_Cost2temp
    for m in range(len(outx)):
        Final_out.append(outx[m])
        

#Funcation Mux-Mapping
if(len(Final_out[0])==3):
    Cost=0
    BTDD_2_Graph=dict()
    for i in range (len(Final_out)):
        Graph1=Minimize2(Final_out[i]);
        Cost=Cost+get_Cost2(Graph1)
        for key in Fun_map:
            if(Fun_map[key]==Final_out[i]):
                BTDD_2_Graph.update({key:Graph1})
                
if((len(Final_out[0])==9)):
    Cost=0
    BTDD_2_Graph=dict()
    for i in range (len(Final_out)):
        map_dictx=dict();
        for k in range(len(Final_out[i])):
            map_dictx["F"+str(listin2[k][0])+str(listin2[k][1])]=Final_out[i][k]
        Graph1=Minimize(Final_out[i],map_dictx);
        Cost=Cost+get_Cost(Graph1)
        for key in Fun_map:
            if(Fun_map[key]==Final_out[i]):
                BTDD_2_Graph.update({key:Graph1})

BTDD_Total_Graph=BTDD_In_Graph.copy()   
BTDD_Total_Graph.update(BTDD_2_Graph)
        

Final_Mux2=Cost+In_Cost2x
print('No. 2:1 Muxes for other inputs',In_Cost2x)
print('No. 2:1 Muxes for 2-input Fun.',Cost)
print('No. of Total 2:1 Muxes',Final_Mux2)
print('Transistor Count:', Final_Mux2*4+inputs*8)    
        