from Template_BDD import Template_BDD
import numpy as np
from Mappings import *

def decision_Template(truth_table):
    
    row_0 = (truth_table[0,0],truth_table[0,1],truth_table[0,2]) 
    row_1 = (truth_table[1,0],truth_table[1,1],truth_table[1,2])
    row_2 = (truth_table[2,0],truth_table[2,1],truth_table[2,2])

    col_0 = (truth_table[0,0],truth_table[1,0],truth_table[2,0]) 
    col_1 = (truth_table[0,1],truth_table[1,1],truth_table[2,1])
    col_2 = (truth_table[0,2],truth_table[1,2],truth_table[2,2])

    rows =np.array([row_0,row_1,row_2])
    print rows
    cols =np.array([col_0,col_1,col_2])
    print cols
    
    equal = {'0=1_row':False,'0=2_row':False,'1=2_row':False,'all_rows':False,
             '0=1_col':False,'0=2_col':False,'1=2_col':False,'all_cols':False}

    if(row_0 == row_1):
        equal['0=1_row'] = True
    if(row_0 == row_2):
        equal['0=2_row'] = True
    if(row_1 == row_2):
        equal['1=2_row'] = True
    if(equal['0=1_row'] and equal['1=2_row'] and equal['0=2_row']):
        equal['all_rows'] = True
        
    if(col_0 == col_1):
        equal['0=1_col'] = True
    if(col_0 == col_2):
        equal['0=2_col'] = True
    if(col_1 == col_2):
        equal['1=2_col'] = True
    if(equal['0=1_col'] and equal['1=2_col'] and equal['0=2_col']):
        equal['all_cols'] = True

    row_2mux = {0:np.array([False,None,None]),1:np.array([False,None,None]),2:np.array([False,None,None])}
    col_2mux = {0:np.array([False,None,None]),1:np.array([False,None,None]),2:np.array([False,None,None])}

    for i in np.arange(3):

        for j in np.arange(3):
            
            if((rows[i] == mux_2_1_red[j]['Output']).all()):
                row_2mux[i][0] = True

                if(i == 0):
                    for k in np.arange(4):
                        if(rows[1] == mux_2_1_red[j][k]).all():
                            
                            row_2mux[i][1] = (1,j,k)
                        if(rows[2] == mux_2_1_red[j][k]).all():
                            print j,k
                            row_2mux[i][2] = (2,j,k)

                elif(i == 1):

                    for k in np.arange(4):
                        if(rows[0] == mux_2_1_red[j][k]).all():
                            row_2mux[i][0] = (0,j,k)
                        if(rows[2] == mux_2_1_red[j][k]).all():
                            row_2mux[i][1] = (2,j,k)
                            
                elif(i == 2):

                    for k in np.arange(4):
                        if(rows[0] == mux_2_1_red[j][k]).all():
                            row_2mux[i][1] = (0,j,k)
                        if(rows[1] == mux_2_1_red[j][k]).all():
                            row_2mux[i][1] = (1,j,k)
                            
                
            if((cols[i] == mux_2_1_red[j]['Output']).all()):
                col_2mux[i][0] = True
                
                if(i == 0):

                    for k in np.arange(4):
                        if(cols[1] == mux_2_1_red[j][k]).all():
                            col_2mux[i][1] = (1,j,k)
                        if(rows[2] == mux_2_1_red[j][k]).all():
                            col_2mux[i][2] = (2,j,k)

                elif(i == 1):

                    for k in np.arange(4):
                        if(cols[0] == mux_2_1_red[j][k]).all():
                            col_2mux[i][0] = (0,j,k)
                        if(rows[2] == mux_2_1_red[j][k]).all():
                            col_2mux[i][1] = (2,j,k)
                            
                elif(i == 2):

                    for k in np.arange(4):
                        if(cols[0] == mux_2_1_red[j][k]).all():
                            col_2mux[i][1] = (0,j,k)
                        if(cols[1] == mux_2_1_red[j][k]).all():
                            col_2mux[i][1] = (1,j,k)

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

        if row_2mux[i][0] == True:
            #other rows equality
            if(row_2mux[i][1] != None):
                if row_2mux[i][1][2] <2:
                    cost_row[i] = (1,1,0,0)
                    cost_row[row_2mux[i][1][0]] = cost_row_init[row_2mux[i][1][0]]
                elif row_2mux[i][1][2] >=2:
                    cost_row[i] = (1,0,1,0)
                    cost_row[row_2mux[i][1][0]] = cost_row_init[row_2mux[i][1][0]]
            elif(row_2mux[i][2] != None):
                if row_2mux[i][2][2] <2:
                    cost_row[i] = (1,1,0,0)
                    cost_row[row_2mux[i][2][0]] = cost_row_init[row_2mux[i][2][0]]
                elif row_2mux[i][2][2] >=2:
                    cost_row[i] = (1,0,1,0)
                    cost_row[row_2mux[i][2][0]] = cost_row_init[row_2mux[i][2][0]]
            else:
                cost_row[i] = cost_row_init[i]
                
        else: #Add the second condition
            cost_row[i] = cost_row_init[i]

        if col_2mux[i][0] == True:
            #other rows equality
            if(col_2mux[i][1] != None):
                if col_2mux[i][1][2] <2:
                    cost_col[i] = (1,1,0,0)
                    cost_col[col_2mux[i][1][0]] = cost_col_init[col_2mux[i][1][0]]
                elif col_2mux[i][1][2] >=2:
                    cost_col[i] = (1,0,1,0)
                    cost_col[col_2mux[i][1][0]] = cost_col_init[col_2mux[i][1][0]]
            elif(col_2mux[i][2] != None):
                if col_2mux[i][2][2] <2:
                    cost_col[i] = (1,1,0,0)
                    cost_col[col_2mux[i][2][0]] = cost_col_init[col_2mux[i][2][0]]
                elif row_2mux[i][2][2] >=2:
                    cost_col[i] = (1,0,1,0)
                    cost_col[col_2mux[i][2][0]] = cost_col_init[col_2mux[i][2][0]]
            else:
                cost_row[i] = cost_row_init[i]
                
        else: #Add the second condition
            cost_col[i] = cost_col_init[i]
    print row_2mux
    print col_2mux

    for i in np.arange(3):

        print "Row %d" %(i)
        print cost_row[i]
    for i in np.arange(3):

        print "Col %d" %(i)
        print cost_col[i]
                
                

            
    


    """
    if(row_0 == row_1):
        equal['0=1_row'] = True
    if(row_0 == row_2):
        equal['0=2_row'] = True
    if(row_1 == row_2):
        equal['1=2_row'] = True
    if(equal['0=1_row'] and equal['1=2_row'] and equal['0=2_row']):
        equal['all_rows'] = True
        
    if(col_0 == col_1):
        equal['0=1_col'] = True
    if(col_0 == col_2):
        equal['0=2_col'] = True
    if(col_1 == col_2):
        equal['1=2_col'] = True
    if(equal['0=1_col'] and equal['1=2_col'] and equal['0=2_col']):
        equal['all_cols'] = True
    """
    """
    #if any true cal cost for those cases and keep it
    for key,value in equal.iteritems():

        if value == 'True':
    
    #proceed to two pair comparisons
    """

    

truth_table = np.array([[2,1,0],[1,2,1],[0,2,1]])

print "Truth Table"
print "   0  1  2"
print "------------"
print "0| %d  %d  %d" %(truth_table[0,0],truth_table[0,1],truth_table[0,2])
print "1| %d  %d  %d" %(truth_table[1,0],truth_table[1,1],truth_table[1,2])
print "2| %d  %d  %d\n" %(truth_table[2,0],truth_table[1,1],truth_table[2,2])

decision_Template(truth_table)
"""
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
"""
