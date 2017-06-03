import numpy as np
from Mappings import combinations_3_3

"""
Author:

Description:

"""

class node:
    def __init__(self,select_line,left_branch,right_branch,left_value,right_value):
        self.select_line = select_line
        self.left_branch = left_branch
        self.right_branch = right_branch
        self.left_value = left_value
        self.right_value = right_value

def Template_BDD(truth_table):

    possible_imp = []

    i = 0
    while i<4:
        stage_2_left_value = {}
        stage_1_left_value = {}
        stage_2_right_value = {}
        if (i== 0):
            stage_2_select_line = 'A'
            stage_2_left_branch = (2)
            stage_2_right_branch = (0,1,'0')
            stage_2_right_val_ind = 1
            
            stage_2_left_value[0] =  'B'
            stage_2_left_value[1] = (0,1,2)
            
            stage_2_right_value[0] =  'B'
            stage_2_right_value[1] = (0,1,2)

            stage_1_select_line = 'A'
            stage_1_left_branch = (0)
            stage_1_right_branch = (1,2)
            
            stage_1_left_value[0] =  'B'
            stage_1_left_value[1] = (0,1,2)

        elif (i == 1):
            stage_2_select_line = 'A'
            stage_2_left_branch = (0)
            stage_2_right_branch = (1,2,'2')
            stage_2_right_val_ind = 1
            
            stage_2_left_value[0] =  'B'
            stage_2_left_value[1] = (0,1,2)
            
            stage_2_right_value[0] =  'B'
            stage_2_right_value[1] = (0,1,2)

            stage_1_select_line = 'A'
            stage_1_left_branch = (2)
            stage_1_right_branch = (0,1)
            
            stage_1_left_value[0] =  'B'
            stage_1_left_value[1] = (0,1,2)

        elif (i == 2):

            stage_2_select_line = 'B'
            stage_2_left_branch = (2)
            stage_2_right_branch = (0,1,'0')
            stage_2_right_val_ind = 1
            
            stage_2_left_value[0] =  'A'
            stage_2_left_value[1] = (0,1,2)
            
            stage_2_right_value[0] =  'A'
            stage_2_right_value[1] = (0,1,2)

            stage_1_select_line = 'B'
            stage_1_left_branch = (0)
            stage_1_right_branch = (1,2)
            
            stage_1_left_value[0] =  'A'
            stage_1_left_value[1] = (0,1,2)
            
        elif(i==3):

            stage_2_select_line = 'B'
            stage_2_left_branch = (0)
            stage_2_right_branch = (1,2,'2')
            stage_2_right_val_ind = 1
            
            stage_2_left_value[0] =  'A'
            stage_2_left_value[1] = (0,1,2)
            
            stage_2_right_value[0] =  'A'
            stage_2_right_value[1] = (0,1,2)

            stage_1_select_line = 'B'
            stage_1_left_branch = (2)
            stage_1_right_branch = (0,1)
            
            stage_1_left_value[0] =  'A'
            stage_1_left_value[1] = (0,1,2)
            
            
        if stage_2_select_line == 'A' and stage_1_select_line == 'A':
            
            stage_2_left_value[2] = (truth_table[stage_2_left_branch,0],truth_table[stage_2_left_branch,1],truth_table[stage_2_left_branch,2])
            stage_2_right_value[2] = (truth_table[stage_2_right_val_ind,0],truth_table[stage_2_right_val_ind,1],truth_table[stage_2_right_val_ind,2])
            stage_1_left_value[2] = (truth_table[stage_1_left_branch,0],truth_table[stage_1_left_branch,1],truth_table[stage_1_left_branch,2])

        elif stage_2_select_line == 'B' and stage_1_select_line == 'B':

            stage_2_left_value[2] = (truth_table[0,stage_2_left_branch],truth_table[1,stage_2_left_branch],truth_table[2,stage_2_left_branch])
            stage_2_right_value[2] = (truth_table[0,stage_2_right_val_ind],truth_table[1,stage_2_right_val_ind],truth_table[2,stage_2_right_val_ind])
            stage_1_left_value[2] = (truth_table[0,stage_1_left_branch],truth_table[1,stage_1_left_branch],truth_table[2,stage_1_left_branch])

        stage_2_node = node(stage_2_select_line,stage_2_left_branch,stage_2_right_branch,stage_2_left_value,stage_2_right_value)

        stage_1_right_value = stage_2_node
        stage_1_node = node(stage_1_select_line,stage_1_left_branch,stage_1_right_branch,stage_1_left_value,stage_1_right_value)

        possible_imp.append(stage_1_node)

        i = i+1
    return possible_imp


            
