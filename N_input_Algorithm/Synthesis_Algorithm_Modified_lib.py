# -*- coding: utf-8 -*-
"""
Created on Thu Oct  5 15:56:41 2017

@author: chetan and M.B.Srinivas

"""
def IsConstant(out):
    return len(set(out)) <= 1
        
def Decompose_Fun(Fun_map,k,inputsx,node,m):
    BTDD_Graph=dict()
    in_List1=[]
    outlist1=[]
    Fun_mapx=dict()
    Fun_mapx=Fun_map.copy()
    outlist1=Fun_mapx[node][1].copy()
    #print(outlist1)
    in_List1=Fun_mapx[node][0].copy()
    #print(in_List1)
    listin1=[]
    Fun_map1=dict()
    for i in range(int(pow(3,len(in_List1)))):
        templistin=[];
        for j in range (len(in_List1)):
            templistin.append((int(i/(pow(3,(len(in_List1)-1-j))))%3))
        listin1.append(templistin)
    #print(listin1)
    Decompose=0
    for i in range(len(in_List1)):
        out0=[]
        out1=[]
        out2=[]
        
        #print('input',i)
        for j in range(len(listin1)):
            #print(j)
            if((listin1[j][i])==0):
                out0.append((outlist1[j]))
            elif ((listin1[j][i])==1):
                out1.append((outlist1[j]))
            elif ((listin1[j][i])==2):
                out2.append((outlist1[j]))
        #print(out0)
        #print(out1)
        #print(out2)
        node012='F'+str(k)+'_L'+str(inputsx)+'_'+str(m)+'_In'+str(in_List1[i])+'_'+str(0)+str(1)+str(2)
        node01='F'+str(k)+'_L'+str(inputsx)+'_'+str(m)+'_In'+str(in_List1[i])+'_'+str(0)+str(1)
        node12='F'+str(k)+'_L'+str(inputsx)+'_'+str(m)+'_In'+str(in_List1[i])+'_'+str(1)+str(2)
        node0='F'+str(k)+'_L'+str(inputsx)+'_'+str(m)+'_In'+str(in_List1[i])+'_'+str(0)
        node1='F'+str(k)+'_L'+str(inputsx)+'_'+str(m)+'_In'+str(in_List1[i])+'_'+str(1)
        node2='F'+str(k)+'_L'+str(inputsx)+'_'+str(m)+'_In'+str(in_List1[i])+'_'+str(2)
        if(out0==out1)or(out1==out2) or (IsConstant(out2)) or (IsConstant(out0)):
            #print("Decompose with respect to input", 'In'+str(in_List1[i]))
            in_List1.remove(in_List1[i])
            if(out0==out1==out2):
                out=[out0]
                Fun_map1.update({node0:[in_List1,out0]})
                BTDD_Graph.update({node:[node012]})

            elif(out0==out1):
                out=[out0,out2]
                Fun_map1.update({node0:[in_List1,out0]})
                Fun_map1.update({node2:[in_List1,out2]})
                BTDD_Graph.update({node:[node01,node2]})
                BTDD_Graph.update({node01:[node0]})


            elif(out1==out2):
                out=[out0,out2]
                Fun_map1.update({node0:[in_List1,out0]})
                Fun_map1.update({node2:[in_List1,out2]})
                BTDD_Graph.update({node:[node0,node12]})
                BTDD_Graph.update({node12:[node2]})
            
            elif(IsConstant(out2)):
                out=[out0,out1,out2]
                Fun_map1.update({node0:[in_List1,out0]})
                Fun_map1.update({node1:[in_List1,out1]})
                Fun_map1.update({node2:[in_List1,out2]})
                BTDD_Graph.update({node:[node01,node2]})
                BTDD_Graph.update({node01:[node0,node1]})
                
            elif(IsConstant(out0)):
                out=[out0,out1,out2]
                Fun_map1.update({node0:[in_List1,out0]})
                Fun_map1.update({node1:[in_List1,out1]})
                Fun_map1.update({node2:[in_List1,out2]})
                BTDD_Graph.update({node:[node0,node12]})
                BTDD_Graph.update({node12:[node1,node2]})


            Decompose=1
            #print(BTDD_Graph)
            break
    if(Decompose==0):
        out0=[]
        out1=[]
        out2=[]
        for j in range(len(listin1)):
            if((listin1[j][0])==0):
                out0.append((outlist1[j]))
            elif ((listin1[j][0])==1):
                out1.append((outlist1[j]))
            elif ((listin1[j][0])==2):
                out2.append((outlist1[j]))
        out=[out0,out1,out2]
        #print("Decompose with respect to input", 'In'+str(in_List1[0]))
        node012='F'+str(k)+'_L'+str(inputsx)+'_'+str(m)+'_In'+str(in_List1[0])+'_'+str(0)+str(1)+str(2)
        node01='F'+str(k)+'_L'+str(inputsx)+'_'+str(m)+'_In'+str(in_List1[0])+'_'+str(0)+str(1)
        node12='F'+str(k)+'_L'+str(inputsx)+'_'+str(m)+'_In'+str(in_List1[0])+'_'+str(1)+str(2)
        node0='F'+str(k)+'_L'+str(inputsx)+'_'+str(m)+'_In'+str(in_List1[0])+'_'+str(0)
        node1='F'+str(k)+'_L'+str(inputsx)+'_'+str(m)+'_In'+str(in_List1[0])+'_'+str(1)
        node2='F'+str(k)+'_L'+str(inputsx)+'_'+str(m)+'_In'+str(in_List1[0])+'_'+str(2)
        in_List1.remove(in_List1[0])
        Fun_map1.update({node0:[in_List1,out0]})
        Fun_map1.update({node1:[in_List1,out1]})
        Fun_map1.update({node2:[in_List1,out2]})
        BTDD_Graph.update({node:[node01,node2]})
        BTDD_Graph.update({node01:[node0,node1]})
    
    #print(Fun_map1)
    maxlength=0
    for p in range(len(out)):
        if(len(out[p])>maxlength):
            maxlength=len(out[p])
    Size1=maxlength
    return (out,Fun_map1,BTDD_Graph,Size1)

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

    return No_Mux


    

def in_args():#(fun,outputs,inputs,terms):
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
    Cost=0
    #Testing for Single output Case
    #outx=[out[1]]
    Final_out=[]
    #Graph Creation
    #num=0
    BTDD_In_Graph=dict()
    BTDD_Graph=dict()
    Fun_map=dict()
    Fun_mapy=dict()
    BTDD_Graphx=dict()
    BTDD_2_Graph=dict()
    in_List=[]
    for i in range(inputs):
        in_List.append(inputs-i)
    #Testing for all outputs
    #Input Mux-Mapping
    #for k in [2]:
    for k in range(len(out)):
        Outx=[out[k]]
        #print('For output','OUT'+str(len(out)-k-1))
        In_Cost3temp=0
        In_Cost2temp=0
        inputsx=inputs
        Fun_map=dict()
        node='FOUT_'+str(len(out)-k-1)
        Fun_map.update({node:[in_List,Outx[0]]})
        Size=len(Outx[0])

    #Divide the ouput list in to 3 functions along MSB
        while (Size>3):
            m=0
            Fun_mapy=dict()
            for key in Fun_map:
                (Outx,Fun_map1x,BTDD_Graph1,Size)=Decompose_Fun(Fun_map,len(out)-k-1,inputsx,key,m)
                Fun_mapy.update(Fun_map1x)
                BTDD_Graphx.update(BTDD_Graph1)
                m=m+1
            Fun_map=dict()
            outy=[]
            for key in Fun_mapy:
                outy.append(Fun_mapy[key])
            outx=[]
            for l in outy:
                if l not in outx:
                    outx.append(l) 
            Fun_mapy_temp=Fun_mapy.copy()
            for lis in outx:
                count=0
                for key in Fun_mapy_temp:
                    if(count==0 and Fun_mapy_temp[key]==lis):
                        count=1
                        key1=key
                        #print("original",key1)
                    elif(count==1 and Fun_mapy_temp[key]==lis):
                        del Fun_mapy[key]
                        #print("copy",key)
                        BTDD_Graphx.update({key:[key1]})    
            Fun_map=Fun_mapy.copy()
            #print(Fun_map)
            inputsx=inputsx-1
        #print(outx)
        #print(Fun_map)
        #print(BTDD_Graphx)
        #Funcation Mux-Mapping
        In_Cost2temp=get_Cost2(BTDD_Graphx)
        In_Cost2x=In_Cost2x+In_Cost2temp
                    
        
        
        for key in Fun_map:
            Graph1=Minimize2(Fun_map[key][1],'In'+str(Fun_map[key][0][0]));
            Cost=Cost+get_Cost2(Graph1)
            BTDD_2_Graph.update({key:Graph1})
            #print(key,Graph1)0

    Final_Mux2=Cost+In_Cost2temp            
    BTDD_Total_Graph=BTDD_Graphx.copy()   
    BTDD_Total_Graph.update(BTDD_2_Graph)
            


    print('No. 2:1 Muxes for other inputs',In_Cost2temp)
    print('No. 2:1 Muxes for 1-input Fun.',Cost)
    print('No. of Total 2:1 Muxes',Final_Mux2)

    #Final_Mux2--> Total Number of 2:1 multiplexers without inverters 4 transistors each
    #inputs*4 --> generate PTI (2), NTI (2) of each input required for multiplexers
    #Binary NOT of PTI (2) and Binary NOT of NTI for last level input for templates

    print('Transistor Count:', Final_Mux2*4+inputs*4+4)  
    #print(BTDD_Total_Graph)
    return BTDD_Total_Graph,In_Cost2x,Cost,Final_Mux2,Final_Mux2*4+inputs*8     


if __name__ == "__main__":
    BTDD_Total_Graph,In_Cost2x,Cost,Final_Mux2,Tc = in_args()
    file = open("test_prod_9_6.txt","w")
    file.write(str(BTDD_Total_Graph))
    file.close()