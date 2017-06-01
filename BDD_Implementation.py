import numpy as np



"""

Author:
Description:
0. Definitions:

    node: represents the most basic unit of the TDD with following def

        select_line
        left_branch
        right_branch
        left_value
        right_value


1. BDD_Implementation: Takes in a truth table of the form 3x3 and returns all possible
combinations of last node (smaller 2x2 matrices) in a complete TDD.

     Eg:
     Truth Table
       0  1  2
    ------------                 
    0| 2  1  0
    1| 1  2  1
    2| 0  2  1

    Below is one of the 8 smaller sub divisions of the above truth table towards the end of TDD
       0  1  2
    ------------
    0| 2  1  
    1| 1  2

2. stage_1_2_BDD_Implementation

"""

class node:
    def __init__(self,select_line,left_branch,right_branch,left_value,right_value):
        self.select_line = select_line
        self.left_branch = left_branch
        self.right_branch = right_branch
        self.left_value = left_value
        self.right_value = right_value


"""
Truth-table Input and 2x2 selections
"""

def BDD_Implementation(truth_table):
    selection_4 = np.empty((2,8),dtype=int)
    #selection_4 = np.array([[0,0],[0,0]])
    r_c ={}
    nodes = []
    k=0
    l=0
    for i in np.arange(2):
        
        for j in np.arange(2):
            
            selection_4[:,l:l+2] = truth_table[i:i+2,j:j+2]
            r_c[k]=((i,i+1),(j,j+1))
            l=l+2
            k = k +1

    # print the selections
    print selection_4
    #print np.shape(selection_4[:,2:])
    count = np.shape(selection_4)[1]/2
    for i in np.arange(count):
        table_4 = selection_4[:,(2*i):(2*i)+2]
        print table_4
        #print r_c
        
        for j in np.arange(2):
            left_value = {}
            right_value = {}
            if(j ==0):
                select_line = 'A' #Row
                select_num = 0
                input_num = 1
                
                left_value[0] = 'B'
                left_value[1] = r_c[i][input_num]
                
                right_value[0] = 'B'
                right_value[1] = r_c[i][input_num]
                
            elif(j ==1):
                select_line = 'B' #Column
                select_num = 1
                input_num = 0
                
                left_value[0] = 'A'
                left_value[1] = r_c[i][input_num]
                
                right_value[0] = 'A'
                right_value[1] = r_c[i][input_num]

            select_tuple = r_c[i][select_num]
            
            if select_tuple == (0,1):

                left_branch = (0)
                right_branch = (1,2,'2')
                left_val = 0
                right_val = 1

            elif select_tuple == (1,2):

                left_branch = (2)
                right_branch = (0,1,'0')
                left_val = 1
                right_val = 0
             
            if(select_line =='A'):#row
                
                left_value[2] = (table_4[left_val,0],table_4[left_val,1])
                right_value[2] = (table_4[right_val,0],table_4[right_val,1])

            elif(select_line == 'B'):#column

                left_value[2] = (table_4[0,left_val],table_4[1,left_val])
                right_value[2] = (table_4[0,right_val],table_4[1,right_val])

            nodes.append(node(select_line,left_branch,right_branch,left_value,right_value))

    return nodes

def stage_1_2_BDD_Implementation(possible_node,truth_table):
    
    print '-----------------'
    print possible_node.select_line
    print possible_node.left_branch
    print possible_node.right_branch
    print possible_node.left_value
    print possible_node.right_value
    print '-----------------'
    
    if (possible_node.select_line == 'A'):
        stage_1_select_line = 'A'
        stage_2_select_line = 'B'

        stage_1_select_line_aux = 'B'
        stage_2_select_line_aux = 'A'
        
        stage_2_left_value ={}
        stage_2_left_value[0] = 'A'

        stage_2_left_value_aux ={}
        stage_2_left_value_aux[0] = 'B'        

        stage_1_left_value ={}
        stage_1_left_value[0] = 'B'
        stage_1_left_value[1] = (0,1,2)

        stage_1_left_value_aux ={}
        stage_1_left_value_aux[0] = 'A'
        stage_1_left_value_aux[1] = (0,1,2)
        
    elif(possible_node.select_line == 'B'):
        stage_1_select_line = 'B'
        stage_2_select_line = 'A'

        stage_1_select_line_aux = 'A'
        stage_2_select_line_aux = 'B'
        
        stage_2_left_value ={}
        stage_2_left_value[0] = 'B'

        stage_2_left_value_aux ={}
        stage_2_left_value_aux[0] = 'A'
        
        stage_1_left_value ={}
        stage_1_left_value[0] = 'A'
        stage_1_left_value[1] = (0,1,2)

        stage_1_left_value_aux ={}
        stage_1_left_value_aux[0] = 'B'
        stage_1_left_value_aux[1] = (0,1,2)
        """
        stage_2_left_branch_aux = (int(possible_node.right_branch[2]))
        if( possible_node.right_branch[2] =='2'):
            
            stage_2_right_branch_aux = (0,1)
            
        elif(possible_node.right_branch[2] =='0'):

            stage_2_right_branch_aux = (1,2)
        """
        
    if(possible_node.left_value[1] == (0,1) and possible_node.right_value[1] == (0,1)):
        stage_2_right_branch = (0,1)
        stage_2_left_branch = (2)

        stage_2_left_value_aux[1] = (0,1)

        stage_1_right_branch_aux = (0,1)
        stage_1_left_branch_aux = (2)
        

    elif(possible_node.left_value[1] == (1,2) and possible_node.right_value[1] == (1,2)):
        stage_2_right_branch = (1,2)
        stage_2_left_branch = (0)
        
        stage_2_left_value_aux[1] = (1,2)

        stage_1_right_branch_aux = (1,2)
        stage_1_left_branch_aux = (0)

    stage_1_left_branch = (int(possible_node.right_branch[2]))
    
    stage_2_left_branch_aux = (int(possible_node.right_branch[2]))
                
    if(possible_node.right_branch[2] == '0'):
        stage_2_left_value[1] = (1,2)

        #stage_1_left_branch = (0)
        stage_1_right_branch = (1,2)

        stage_2_right_branch_aux = (1,2)
        
        
    elif(possible_node.right_branch[2] == '2'):
        stage_2_left_value[1] = (0,1)

        #stage_1_left_branch = (2)
        stage_1_right_branch = (0,1)

        stage_2_right_branch_aux = (0,1)

    if (possible_node.select_line == 'A'):

        stage_2_left_value[2] = (truth_table[stage_2_left_value[1][0],stage_2_left_branch],
                                truth_table[stage_2_left_value[1][1],stage_2_left_branch])
        stage_1_left_value[2] = (truth_table[int(possible_node.right_branch[2]),0],truth_table[int(possible_node.right_branch[2]),1],
                                 truth_table[int(possible_node.right_branch[2]),2])

        stage_2_left_value_aux[2] = (truth_table[stage_2_left_branch_aux,stage_2_left_value_aux[1][0]],
                                truth_table[stage_2_left_branch_aux,stage_2_left_value_aux[1][1]])

        stage_1_left_value_aux[2] = (truth_table[0,stage_1_left_branch_aux],truth_table[1,stage_1_left_branch_aux],truth_table[2,stage_1_left_branch_aux]) 
        
        
    elif(possible_node.select_line == 'B'):

        stage_2_left_value[2] = (truth_table[stage_2_left_branch,stage_2_left_value[1][0]],
                                truth_table[stage_2_left_branch,stage_2_left_value[1][1]])
        stage_1_left_value[2] = (truth_table[0,int(possible_node.right_branch[2])],truth_table[1,int(possible_node.right_branch[2])],
                                 truth_table[2,int(possible_node.right_branch[2])])

        stage_2_left_value_aux[2] = (truth_table[stage_2_left_value_aux[1][0],stage_2_left_branch_aux],
                                truth_table[stage_2_left_value_aux[1][1],stage_2_left_branch_aux])

        stage_1_left_value_aux[2] = (truth_table[stage_1_left_branch_aux,0],truth_table[stage_1_left_branch_aux,1],truth_table[stage_1_left_branch_aux,2])
        
        
    stage_2_right_value = possible_node
    stage_2_node = node(stage_2_select_line,stage_2_left_branch,stage_2_right_branch,stage_2_left_value,stage_2_right_value)
    
    
    stage_1_right_value = stage_2_node
    stage_1_node = node(stage_1_select_line,stage_1_left_branch,stage_1_right_branch,stage_1_left_value,stage_1_right_value)

    stage_2_right_value_aux = possible_node
    stage_2_node_aux = node(stage_2_select_line_aux,stage_2_left_branch_aux,stage_2_right_branch_aux,stage_2_left_value_aux,stage_2_right_value_aux)
    
    
    stage_1_right_value_aux = stage_2_node_aux
    stage_1_node_aux = node(stage_1_select_line_aux,stage_1_left_branch_aux,stage_1_right_branch_aux,stage_1_left_value_aux,stage_1_right_value_aux)

    

    return (stage_1_node,stage_2_node,stage_1_node_aux)
     
              
   
truth_table = np.array([[2,1,0],[1,2,1],[0,2,1]])

print "Truth Table"
print "   0  1  2"
print "------------"
print "0| %d  %d  %d" %(truth_table[0,0],truth_table[0,1],truth_table[0,2])
print "1| %d  %d  %d" %(truth_table[1,0],truth_table[1,1],truth_table[1,2])
print "2| %d  %d  %d\n" %(truth_table[2,0],truth_table[1,1],truth_table[2,2])

out = BDD_Implementation(truth_table)

for i in np.arange(len(out)):
    print '-----------------'
    print out[i].select_line
    print out[i].left_branch
    print out[i].right_branch
    print out[i].left_value
    print out[i].right_value
    print '-----------------'


print '-----------------'
print '--------3---------'
print out[3].select_line
print out[3].left_branch
print out[3].right_branch
print out[3].left_value
print out[3].right_value
print '-----------------'

(out1,out2,auxi) = stage_1_2_BDD_Implementation(out[3],truth_table)
out3 =out[3]
print '--------Stage 1---------'
print out1.select_line
print out1.left_branch
print out1.right_branch
print out1.left_value
print out1.right_value
print '------------------------'
print '--------Stage 2---------'
print out1.right_value.select_line
print out1.right_value.left_branch
print out1.right_value.right_branch
print out1.right_value.left_value
print out1.right_value.right_value
print '------------------------'
"""
print '--------Stage 2---------'
print out2.select_line
print out2.left_branch
print out2.right_branch
print out2.left_value
print out2.right_value
print '------------------------'
"""
print '--------Stage 3---------'
print out1.right_value.right_value.select_line
print out1.right_value.right_value.left_branch
print out1.right_value.right_value.right_branch
print out1.right_value.right_value.left_value
print out1.right_value.right_value.right_value
print '-----------------------'
print '-----Auxillary Case-----'
print '--------Stage 1---------'
print auxi.select_line
print auxi.left_branch
print auxi.right_branch
print auxi.left_value
print auxi.right_value
print '------------------------'
print '--------Stage 2---------'
print auxi.right_value.select_line
print auxi.right_value.left_branch
print auxi.right_value.right_branch
print auxi.right_value.left_value
print auxi.right_value.right_value
print '------------------------'
"""
print '--------Stage 2---------'
print out2.select_line
print out2.left_branch
print out2.right_branch
print out2.left_value
print out2.right_value
print '------------------------'
"""
print '--------Stage 3---------'
print auxi.right_value.right_value.select_line
print auxi.right_value.right_value.left_branch
print auxi.right_value.right_value.right_branch
print auxi.right_value.right_value.left_value
print auxi.right_value.right_value.right_value
print '-----------------------'
 

            

        
            

        
