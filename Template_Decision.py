from Template_BDD import Template_BDD,node
import numpy as np
from Mappings import *


def remnant(inp_tup):

    if inp_tup == (0):
        return (1,2)
    elif inp_tup == (1):
        return (0,2)
    elif inp_tup == (2):
        return (0,1)
    
def PTI_logic(inp_1):

    out = {(0):(2),(1):(2),(2):(0),(0,1,2):(2,2,0)}
    return out.get(inp_1)

def NTI_logic(inp_1):

    out = {(0):(2),(1):(0),(2):(0),(0,1,2):(0,0,2)}
    return out.get(inp_1)

def INV_logic(inp_1):

    out = {(0):(2),(2):(0)}
    return out.get(inp_1)
    
def decision_template(truth_table):
    
    row_0 = (truth_table[0,0],truth_table[0,1],truth_table[0,2]) 
    row_1 = (truth_table[1,0],truth_table[1,1],truth_table[1,2])
    row_2 = (truth_table[2,0],truth_table[2,1],truth_table[2,2])

    col_0 = (truth_table[0,0],truth_table[1,0],truth_table[2,0]) 
    col_1 = (truth_table[0,1],truth_table[1,1],truth_table[2,1])
    col_2 = (truth_table[0,2],truth_table[1,2],truth_table[2,2])

    rows =np.array([row_0,row_1,row_2])
    cols =np.array([col_0,col_1,col_2])
    #print rows    
    #print cols
    
                        # (0=True,row_number in tt 1 = PTI 2 =NTI ) # Reduction from 2 muxes to 1 mux
    row_2mux = {0:np.array([False,None,None]),1:np.array([False,None,None]),2:np.array([False,None,None])}
    col_2mux = {0:np.array([False,None,None]),1:np.array([False,None,None]),2:np.array([False,None,None])}
                        # PTI no 0,1    NTI no 0,1  # Reduction from 1 muxes to 0 mux thru nti or pti
    row_PN = {0:np.array([None,None,None,None]),1:np.array([None,None,None,None]),2:np.array([None,None,None,None])}
    col_PN = {0:np.array([None,None,None,None]),1:np.array([None,None,None,None]),2:np.array([None,None,None,None])}

    new_mapping_row_case1 ={0:np.array([False,None]),1:np.array([False,None]),2:np.array([False,None])}
    new_mapping_col_case1 ={0:np.array([False,None]),1:np.array([False,None]),2:np.array([False,None])}

    new_mapping_row_case2 ={0:np.array([False,None]),1:np.array([False,None]),2:np.array([False,None])}
    new_mapping_col_case2 ={0:np.array([False,None]),1:np.array([False,None]),2:np.array([False,None])}
    
    #Need to implement for combinations of PTI.NTI,INV
    
    cost_row =np.array([(0,0,0,0),(0,0,0,0),(0,0,0,0)])
    cost_col =np.array([(0,0,0,0),(0,0,0,0),(0,0,0,0)])

    cost_row_init =np.array([(0,0,0,0),(0,0,0,0),(0,0,0,0)])
    cost_col_init =np.array([(0,0,0,0),(0,0,0,0),(0,0,0,0)])
    
    for i in np.arange(3):
        
        for j in np.arange(27):
                    if (rows[i] == combinations_3_3[j]['Output']).all():
                        cost_row_init[i] =combinations_3_3[j]['Implementation']
                    
                    if (cols[i] == combinations_3_3[j]['Output']).all():
                        cost_col_init[i] =combinations_3_3[j]['Implementation']

    for i in np.arange(3):

        for k in np.arange(2): # NTI or PTI of the given row gives another row for case 1

            row_NTI =np.array([NTI_logic(rows[i][0]),NTI_logic(rows[i][1]),NTI_logic(rows[i][2])])
            row_PTI =np.array([PTI_logic(rows[i][0]),PTI_logic(rows[i][1]),PTI_logic(rows[i][2])])

            rows_check = remnant(i)
            #NTI or PTI of the index number is equal to the row number given in the value
            if(rows[rows_check[0]] == row_PTI).all():
               row_PN[i][0] = rows_check[0]
               new_mapping_row_case1[rows_check[0]][0] = True
               new_mapping_row_case1[rows_check[0]][1] = "PTI(ROW"+str(i)+")" 
               
            if(rows[rows_check[1]] == row_PTI).all():
               row_PN[i][1] = rows_check[1]
               new_mapping_row_case1[rows_check[1]][0] = True
               new_mapping_row_case1[rows_check[1]][1] = "PTI(ROW"+str(i)+")" 
               
            if(rows[rows_check[0]] == row_NTI).all():
               row_PN[i][2] = rows_check[0]
               new_mapping_row_case1[rows_check[0]][0] = True
               new_mapping_row_case1[rows_check[0]][1] = "NTI(ROW"+str(i)+")" 
               
            if(rows[rows_check[1]] == row_NTI).all():
               row_PN[i][3] = rows_check[1]
               new_mapping_row_case1[rows_check[1]][0] = True
               new_mapping_row_case1[rows_check[1]][1] = "NTI(ROW"+str(i)+")" 
               
        for j in np.arange(len(mux_2_1_red)): # PTI reduction or NTI reduction from an extra mux to use the existing logic from the truth table

            if (rows[i] == mux_2_1_red[j]['Output']).all():
                

                row_2mux[i][0] = True
                #print "*"

                PTI_out = remnant(rows[i][2])
                PTI_map1 =np.array([rows[i][0],rows[i][1],PTI_out[0]])
                PTI_map2 = np.array([rows[i][0],rows[i][1],PTI_out[1]])

                NTI_out = remnant(rows[i][0])
                NTI_map1 = np.array([NTI_out[0],rows[i][1],rows[i][2]])
                NTI_map2 = np.array([NTI_out[1],rows[i][1],rows[i][2]])

                remnant_rows = remnant(i)
                """
                print rows[i]
                print rows[remnant_rows[0]],rows[remnant_rows[1]]
                print PTI_map1
                print PTI_map2
                print NTI_map1
                print NTI_map2
                """
                #Put the mux accordingly and source the other inputs i.e 0,1 for PTI from the given row

                if (((rows[remnant_rows[0]] == PTI_map1).all()) or ((rows[remnant_rows[0]] == PTI_map2).all())):
                    
                    row_2mux[i][1] = remnant_rows[0]
                    cost_row[i] = (1,1,0,0)
                    new_mapping_row_case2[i][0] = True
                    new_mapping_row_case2[i][1] = node('X',(2),(0,1),rows[i][2],"ROW"+str(remnant_rows[0]))
                    
                    

                if (((rows[remnant_rows[1]] == PTI_map1).all()) or ((rows[remnant_rows[1]] == PTI_map2).all())):
                    
                    row_2mux[i][1] = remnant_rows[1]
                    cost_row[i] = (1,1,0,0)
                    new_mapping_row_case2[i][0] = True
                    new_mapping_row_case2[i][1] = node('X',(2),(0,1),row[si][2],"ROW"+str(remnant_rows[1]))


                if (((rows[remnant_rows[0]] == NTI_map1).all()) or ((rows[remnant_rows[0]] == NTI_map2).all())):
                    
                    row_2mux[i][2] = remnant_rows[0]
                    cost_row[i] = (1,0,1,0)
                    new_mapping_row_case2[i][0] = True
                    new_mapping_row_case2[i][1] = node('X',(0),(1,2),rows[i][2],"ROW"+str(remnant_rows[0]))

                if (((rows[remnant_rows[1]] == NTI_map1).all()) or ((rows[remnant_rows[1]] == NTI_map2).all())):
                    
                    row_2mux[i][2] = remnant_rows[1]
                    cost_row[i] = (1,0,1,0)
                    new_mapping_row_case2[i][0] = True
                    new_mapping_row_case2[i][1] = node('X',(0),(1,2),rows[i][2],"ROW"+str(remnant_rows[1]))
                    

                else:
                    cost_row[i] = cost_row_init[i]
            

        if (row_2mux[i][0] == False):
            cost_row[i] = cost_row_init[i]
            
                    

    for i in np.arange(3):

        for k in np.arange(2):

            col_NTI =np.array([NTI_logic(cols[i][0]),NTI_logic(cols[i][1]),NTI_logic(cols[i][2])])
            col_PTI =np.array([PTI_logic(cols[i][0]),PTI_logic(cols[i][1]),PTI_logic(cols[i][2])])

            cols_check = remnant(i)

            if(cols[cols_check[0]] == col_PTI).all():
               col_PN[i][0] = cols_check[0]
               new_mapping_col_case1[cols_check[0]][0] = True
               new_mapping_col_case1[cols_check[0]][1] = "PTI(COL"+str(i)+")"
               
            if(cols[cols_check[1]] == col_PTI).all():
               col_PN[i][1] = cols_check[1]
               new_mapping_col_case1[cols_check[1]][0] = True
               new_mapping_col_case1[cols_check[1]][1] = "PTI(COL"+str(i)+")"
               
            if(cols[cols_check[0]] == col_NTI).all():
               col_PN[i][2] = cols_check[0]
               new_mapping_col_case1[cols_check[0]][0] = True
               new_mapping_col_case1[cols_check[0]][1] = "NTI(COL"+str(i)+")"
               
            if(cols[cols_check[1]] == col_NTI).all():
               print i,cols_check
               col_PN[i][3] = cols_check[1]
               new_mapping_col_case1[cols_check[1]][0] = True
               new_mapping_col_case1[cols_check[1]][1] = "NTI(COL"+str(i)+")"

        for j in np.arange(len(mux_2_1_red)):

            if (cols[i] == mux_2_1_red[j]).all():

                col_2mux[i][0] = True

                PTI_out = remnant(cols[i][2])
                PTI_map1 =(cols[i][0],cols[i][1],PTI_out[0])
                PTI_map2 = (cols[i][0],cols[i][1],PTI_out[1])

                NTI_out = remnant(cols[i][0])
                NTI_map1 = (NTI_out[0],cols[i][1],cols[i][2])
                NTI_map2 = (NTI_out[1],cols[i][1],cols[i][2])

                remnant_cols = remnant(i)

                if ((cols[remnant_cols[0]] == PTI_map1).all() or (cols[remnant_cols[0]] == PTI_map2).all()):
                    col_2mux[i][1] = remnant_cols[0]
                    cost_col[i] = (1,1,0,0) #modified mapping ckts

                    new_mapping_col_case2[i][0] = True
                    new_mapping_col_case2[i][1] = node('X',(2),(0,1),cols[i][2],"COL"+str(remnant_cols[0]))

                if ((cols[remnant_cols[1]] == PTI_map1).all() or (cols[remnant_cols[1]] == PTI_map2).all()):
                    col_2mux[i][1] = remnant_cols[0]
                    cost_col[i] = (1,1,0,0)

                    new_mapping_col_case2[i][0] = True
                    new_mapping_col_case2[i][1] = node('X',(2),(0,1),cols[i][2],"COL"+str(remnant_cols[1]))


                if ((cols[remnant_cols[0]] == NTI_map1).all() or (cols[remnant_cols[0]] == NTI_map2).all()):
                    row_2mux[i][2] = remnant_cols[0]
                    cost_col[i] = (1,0,1,0)

                    new_mapping_col_case2[i][0] = True
                    new_mapping_col_case2[i][1] = node('X',(0),(1,2),cols[i][2],"COL"+str(remnant_rows[0]))

                if ((cols[remnant_cols[1]] == NTI_map1).all() or (cols[remnant_cols[1]] == NTI_map2).all()):
                    row_2mux[i][2] = remnant_cols[0]
                    cost_col[i] = (1,0,1,0)

                    new_mapping_col_case2[i][0] = True
                    new_mapping_col_case2[i][1] = node('X',(0),(1,2),cols[i][2],"COL"+str(remnant_rows[1]))

                else:
                    cost_col[i] = cost_col_init[i]#original mapping ckts

        if (col_2mux[i][0] == False):
            cost_col[i] = cost_col_init[i]

    for i in np.arange(3): # attributing cost for case 1

        for j in np.arange(4):

            if row_PN[i][j] != None:

                cost_current_row = cost_row[row_PN[i][j]]

                if(cost_current_row[0] >0):
                    if(sum(cost_current_row[1:4])> 1):
                        if(j<2):
                            cost_row[row_PN[i][j]] = (0,1,0,0)
                        if(j>2):
                            cost_row[row_PN[i][j]] = (0,0,1,0)
                            
                            
            if col_PN[i][j] != None:

                if col_PN[i][j] != None:
                    

                    cost_current_col = cost_col[col_PN[i][j]]

                    if(cost_current_col[0] >0):
                        if(sum(cost_current_col[1:4])> 1):
                            if(j<2):
                                cost_col[col_PN[i][j]] = (0,1,0,0)
                            if(j>2):
                                cost_col[col_PN[i][j]] = (0,0,1,0)
                    
                

    equal_row = {(0,1):False,(0,2):False,(1,2):False,(0,1,2):False}
    equal_col = {(0,1):False,(0,2):False,(1,2):False,(0,1,2):False}

    if(row_0 == row_1):
        equal_row[(0,1)] = True
        cost_row[1] = (0,0,0,0)
        
    if(row_0 == row_2):
        equal_row[(0,2)] = True
        cost_row[2] = (0,0,0,0)
        
    if(row_1 == row_2):
        equal_row[(1,2)] = True
        cost_row[2] = (0,0,0,0)
        
    if(equal_row[(0,1)] and equal_row[(1,2)] and equal_row[(0,2)]):
        equal_row[(0,1,2)] = True
        cost_row[1] = (0,0,0,0)
        cost_row[2] = (0,0,0,0)
        
    if(col_0 == col_1):
        equal_col[(0,1)] = True
        cost_col[1] = (0,0,0,0)
        
    if(col_0 == col_2):
        equal_col[(0,2)] = True
        cost_col[2] = (0,0,0,0)
        
    if(col_1 == col_2):
        equal_col[(1,2)] = True
        cost_col[2] = (0,0,0,0)
        
    if(equal_col[(0,1)] and equal_col[(1,2)] and equal_col[(0,2)]):
        equal_col[(0,1,2)] = True
        cost_col[1] = (0,0,0,0)
        cost_col[2] = (0,0,0,0)
                
    #print row_2mux
    #print col_2mux
    print "************"

    #print row_PN
    #print col_PN

    for i in np.arange(3):

        print "Row %d" %(i)
        print cost_row[i]
    for i in np.arange(3):

        print "Col %d" %(i)
        print cost_col[i]

    total_column_cost = (sum(cost_col[:,0]),sum(cost_col[:,1]),sum(cost_col[:,2]),sum(cost_col[:,3]))
    total_row_cost = (sum(cost_row[:,0]),sum(cost_row[:,1]),sum(cost_row[:,2]),sum(cost_row[:,3]))

    print total_row_cost
    print total_column_cost
    
    ###### Flowgraph Contruction #######
    stage_2_left_value = {}
    stage_1_left_value = {}
    stage_1_right_value = {}
    stage_2_right_value = {}
    fg_stages = 0

    if(total_row_cost[0] <= total_column_cost[0]):

        cost_final_out = total_row_cost
        
        stage_1_select_line = 'A'
        stage_2_select_line = 'A'

        stage_1_left_value[0] =  'B'
        stage_1_left_value[1] = (0,1,2)

        stage_2_left_value[0] =  'B'
        stage_2_left_value[1] = (0,1,2)
        
        print equal_row
        if(equal_row[(0,1,2)]== True):
            final_out = combinations_3_3_bdd(row_2,'B')
            
        elif(equal_row[(0,1)]== True):#PTI #combinations_3_3_bdd(inp,sl)
            stage_1_left_branch = (2)
            stage_1_left_value[2] = combinations_3_3_bdd(row_2,'B')
            
            stage_1_right_branch = (0,1)
                        
            stage_1_right_value[2] = combinations_3_3_bdd(row_0,'B') # call mapping circuits
            fg_stages = 1
            final_out = node(stage_1_select_line,stage_1_left_branch,stage_1_right_branch,stage_1_left_value[2],stage_1_right_value[2])
            
        elif(equal_row[(1,2)]== True):#NTI
            stage_1_left_branch = (0)
            stage_1_left_value[2] = combinations_3_3_bdd(row_0,'B')
            
            stage_1_right_branch = (1,2)

            stage_1_right_value[2] = combinations_3_3_bdd(row_2,'B')
            fg_stages = 1
            final_out = node(stage_1_select_line,stage_1_left_branch,stage_1_right_branch,stage_1_left_value[2],stage_1_right_value[2])
            
        else:#Manipulations using case 1 and 2
            stage_1_left_branch = (0)
            stage_1_right_branch = (1,2)
            if(new_mapping_row_case2[0][0]):
                new_mapping_row_case2[0][1].select_line = 'B'
                stage_1_left_value[2] = new_mapping_row_case2[0][1]

            elif(new_mapping_row_case1[0][0]):
                stage_1_left_value[2] = new_mapping_row_case1[0][1]

            else:
                stage_1_left_value[2] = combinations_3_3_bdd(row_0,'B')
                new_out = combinations_3_3_bdd((1,0,2),'B')
                #print new_out.right_value
                #print "+"+stage_1_left_value[2].right_value
                          
            
            #print "!"+stage_1_left_value[2].right_value
            stage_2_left_branch = (2)
            stage_2_right_branch = (0,1,'0')
            #print "!"+stage_1_left_value[2].right_value
            if(new_mapping_row_case2[2][0]):
                new_mapping_row_case2[0][1].select_line = 'B'
                stage_2_left_value[2] = new_mapping_row_case2[0][1]

            elif(new_mapping_row_case1[2][0]):
                stage_2_left_value[2] = new_mapping_row_case1[0][1]

            else:
                stage_2_left_value[2] = combinations_3_3_bdd(row_2,'B')
                                       
            if(equal_row[(0,2)]):
                stage_2_left_value[2]="ROW0"
                
                
            #stage_2_left_value[2] = combinations_3_3_bdd(row_2,'B')
            #newg = combinations_3_3_bdd(row_2,'B')
            #print "y",newg.right_value
            #print "&"+stage_1_left_value[2].right_value
            if(new_mapping_row_case2[1][0]):
                new_mapping_row_case2[0][1].select_line = 'B'
                stage_2_right_value[2] = new_mapping_row_case2[0][1]

            elif(new_mapping_row_case1[1][0]):
                stage_2_right_value[2] = new_mapping_row_case1[0][1]

            else:
                stage_2_right_value[2] = combinations_3_3_bdd(row_1,'B')
            #stage_2_right_value[2] = combinations_3_3_bdd(row_1,'B')
            
            fg_stages = 2
            #print "#@"+stage_1_left_value[2].right_value
            final_out = node(stage_1_select_line,stage_1_left_branch,stage_1_right_branch,stage_1_left_value[2],node(stage_2_select_line,stage_2_left_branch,stage_2_right_branch,stage_2_left_value[2],stage_2_right_value[2]))
            #print "#",final_out.left_value[2].right_value
    elif(total_row_cost[0] > total_column_cost[0]):

        cost_final_out = total_column_cost
        
        stage_1_select_line = 'B'
        stage_2_select_line = 'B'

        stage_1_left_value[0] =  'A'
        stage_1_right_value[0] =  'A'
        stage_1_left_value[1] = (0,1,2)
        stage_1_right_value[1] = (0,1,2)
        
        if(equal_col[(0,1,2)]== True):
            final_out = combinations_3_3_bdd(col_2,'B')
            
        elif(equal_col[(0,1)]== True):
            stage_1_left_branch = (2)
            stage_1_left_value[2] = combinations_3_3_bdd(col_2,'B')
            
            stage_1_right_branch = (0,1)
                        
            stage_1_right_value[2] = combinations_3_3_bdd(col_0,'B')
            final_out = node(stage_1_select_line,stage_1_left_branch,stage_1_right_branch,stage_1_left_value[2],stage_1_right_value[2])
            fg_stages = 1
            
        elif(equal_col[(1,2)]== True):
            stage_1_left_branch = (0)
            stage_1_left_value[2] = combinations_3_3_bdd(col_0,'B')
            
            stage_1_right_branch = (1,2)

            stage_1_right_value[2] = combinations_3_3_bdd(col_2,'B')
            final_out = node(stage_1_select_line,stage_1_left_branch,stage_1_right_branch,stage_1_left_value[2],stage_1_right_value[2])
            fg_stages = 1
            
        else:
            stage_1_left_branch = (0)
            stage_1_right_branch = (1,2)
            stage_1_left_branch = (0)
            stage_1_right_branch = (1,2)
            
            if(new_mapping_col_case2[0][0]):
                new_mapping_col_case2[0][1].select_line = 'A'
                stage_1_left_value[2] = new_mapping_col_case2[0][1]

            elif(new_mapping_col_case1[0][0]):
                stage_1_left_value[2] = new_mapping_col_case1[0][1]

            else:
                stage_1_left_value[2] = combinations_3_3_bdd(col_0,'A')
            
            stage_2_left_branch = (2)
            stage_2_right_branch = (0,1,'0')
            #stage_2_left_value[2] = combinations_3_3_bdd(col_2,'A')
            
            if(new_mapping_col_case2[2][0]):
                new_mapping_col_case2[0][1].select_line = 'A'
                stage_2_left_value[2] = new_mapping_col_case2[0][1]

            elif(new_mapping_col_case1[2][0]):
                stage_2_left_value[2] = new_mapping_col_case1[0][1]

            else:
                stage_2_left_value[2] = combinations_3_3_bdd(col_2,'A')

            if(equal_col[(0,2)]):
                stage_2_left_value[2]="ROW0"

            if(new_mapping_col_case2[1][0]):
                new_mapping_col_case2[0][1].select_line = 'A'
                stage_2_right_value[2] = new_mapping_col_case2[0][1]

            elif(new_mapping_col_case1[1][0]):
                stage_2_right_value[2] = new_mapping_col_case1[0][1]

            else:
                stage_2_right_value[2] = combinations_3_3_bdd(col_1,'A')
            #stage_2_right_value[2] = combinations_3_3_bdd(col_1,'A')

            fg_stages = 2
            final_out = node(stage_1_select_line,stage_1_left_branch,stage_1_right_branch,stage_1_left_value[2],node(stage_2_select_line,stage_2_left_branch,stage_2_right_branch,stage_2_left_value[2],stage_2_right_value[2]))

    #####else: # cost after mux
    #print "#",final_out.left_value[2].right_value
    return final_out,fg_stages
            

    
            
            







         
#truth_table = np.array([[1,1,1],[0,2,1],[0,1,2]])
#truth_table = np.array([[0,2,1],[1,1,1],[0,2,1]])
#truth_table = np.array([[0,1,1],[0,1,1],[0,1,1]])
truth_table = np.array([[0,1,2],[1,2,0],[2,0,1]]) #HA

print "Truth Table"
print "   0  1  2"
print "------------"
print "0| %d  %d  %d" %(truth_table[0,0],truth_table[0,1],truth_table[0,2])
print "1| %d  %d  %d" %(truth_table[1,0],truth_table[1,1],truth_table[1,2])
print "2| %d  %d  %d\n" %(truth_table[2,0],truth_table[2,1],truth_table[2,2])

out,nos = decision_template(truth_table)
"""
if nos==2:
    #print '--------Stage 1---------'
    print '              %s                 '%(out.select_line)
    print '      %d            (%d,%d)      '%(out.left_branch,out.right_branch[0],out.right_branch[1])
    print '     %d                 %s       '%(out.left_value[2],out.right_value.select_line) 
    print '                   %d        (%d,%d)  '%(out.right_value.left_branch,out.right_value.right_branch[0],out.right_value.right_branch[1])
    #print '                  %d            %d     '%(out.right_value.right_value[0],out.right_value.right_value.select_line)
    print "      ",out.right_value.left_value,"     ",out.right_value.right_value
    #print 
    #print out.right_value
    #print '------------------------'
    #print '--------Stage 2---------'
    
    print 
    print out.right_value.left_branch
    print out.right_value.right_branch
    print out.right_value.left_value
    print out.right_value.right_value
    print '------------------------'
    
    
elif nos == 1:
    print '--------Stage 1---------'
    print out.select_line
    print out.left_branch
    print out.right_branch
    print out.left_value
    print out.right_value
    
    

out_temp = Template_BDD(truth_table)

for i in np.arange(4):
    
    print '--------Stage 1---------'
    print out_temp[i].select_line
    print out_temp[i].left_branch
    print out_temp[i].right_branch
    print out_temp[i].left_value
    print out_temp[i].right_value
    print '------------------------'
    print '--------Stage 2---------'
    print out_temp[i].right_value.select_line
    print out_temp[i].right_value.left_branch
    print out_temp[i].right_value.right_branch
    print out_temp[i].right_value.left_value
    print out_temp[i].right_value.right_value
    print '------------------------'

print out.left_value[2].right_value
print "                         ",out.select_line,"               "
print "                ",out.left_branch,"    ",out.right_branch,"       "
if(str(type(out.left_value[2])) == "<type 'instance'>"):
    print "      ",out.left_value[2].select_line,"    "
    print "   ",out.left_value[2].left_branch,"     ",out.left_value[2].right_branch
    if str(type(out.left_value[2].right_value)) == "<type 'instance'>":
        print "  ",out.left_value[2].left_value," ",out.left_value[2].right_value.select_line
        print "                  #",out.left_value[2].right_value.left_branch,"    ",out.left_value[2].right_value.right_branch
        print "                               ",out.left_value[2].right_value.left_value,"     ",out.left_value[2].right_value.right_value
    else:
        print "",out.left_value[2].left_value,"          ",out.left_value[2].right_value
else:
    print "  ",out.left_value[2]

#print out.right_value

if(str(type(out.right_value)) == "<type 'instance'>"):
    print "                                 ",out.right_value.select_line,"    "
    print "                        ",out.right_value.left_branch,"     ",out.right_value.right_branch

    if(str(type(out.right_value.left_value)) == "<type 'instance'>"):
        print "            ",out.right_value.left_value.select_line,"                                          "
        print "          ",out.right_value.left_value.left_branch,"    ",out.right_value.left_value.right_branch
        print "        ",out.right_value.left_value.left_value,"             ",out.right_value.left_value.right_value
        
    else:
        print "       ",out.right_value.left_value
        
    if str(type(out.right_value.right_value)) == "<type 'instance'>":
        print "                                                           ",out.right_value.right_value.select_line
        print "                                                  ",out.right_value.right_value.left_branch,"    ",out.right_value.right_value.right_branch
        print "                                                ",out.right_value.right_value.left_value,"     ",out.right_value.right_value.right_value
    else:
        print "                                              ",out.right_value.right_value
        
    
else:
    print "          ",out.right_value[2]

"""
#print out.left_value.right_value
print "                         ",out.select_line,"               "
print "                ",out.left_branch,"    ",out.right_branch,"       "
if(str(type(out.left_value)) == "<type 'instance'>"):
    print "      ",out.left_value.select_line,"    "
    print "   ",out.left_value.left_branch,"     ",out.left_value.right_branch
    if str(type(out.left_value.right_value)) == "<type 'instance'>":
        print "  ",out.left_value.left_value," ",out.left_value.right_value.select_line
        print "                  #",out.left_value.right_value.left_branch,"    ",out.left_value.right_value.right_branch
        print "                               ",out.left_value.right_value.left_value,"     ",out.left_value.right_value.right_value
    else:
        print "",out.left_value.left_value,"          ",out.left_value.right_value
else:
    print "  ",out.left_value

#print out.right_value

if(str(type(out.right_value)) == "<type 'instance'>"):
    print "                                 ",out.right_value.select_line,"    "
    print "                        ",out.right_value.left_branch,"     ",out.right_value.right_branch

    if(str(type(out.right_value.left_value)) == "<type 'instance'>"):
        print "            ",out.right_value.left_value.select_line,"                                          "
        print "          ",out.right_value.left_value.left_branch,"    ",out.right_value.left_value.right_branch
        print "        ",out.right_value.left_value.left_value,"             ",out.right_value.left_value.right_value
        
    else:
        print "       ",out.right_value.left_value
        
    if str(type(out.right_value.right_value)) == "<type 'instance'>":
        print "                                                           ",out.right_value.right_value.select_line
        print "                                                  ",out.right_value.right_value.left_branch,"    ",out.right_value.right_value.right_branch
        print "                                                ",out.right_value.right_value.left_value,"     ",out.right_value.right_value.right_value
    else:
        print "                                              ",out.right_value.right_value
        
    
else:
    print "                                    ",out.right_value
     

 
