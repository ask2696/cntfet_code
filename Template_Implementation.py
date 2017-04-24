import numpy as np

        
#                          Output paralell to (0,1,2) Cost behaviour (Mux,PTI,NTI,B_INV)
combinations = np.array([{'Output':(0,0,0),'Implementation':(0,0,0,0)},
                         {'Output':(0,0,1),'Implementation':(1,1,0,0)},
                         {'Output':(0,0,2),'Implementation':(0,1,0,1)},
                         {'Output':(0,1,0),'Implementation':(1,1,0,0)},
                         {'Output':(0,1,1),'Implementation':(1,0,1,0)},
                         {'Output':(0,1,2),'Implementation':(0,0,0,0)},
                         {'Output':(0,2,0),'Implementation':(1,1,1,0)},
                         {'Output':(0,2,1),'Implementation':(1,0,1,1)},
                         {'Output':(0,2,2),'Implementation':(0,0,1,1)},
                         {'Output':(1,0,0),'Implementation':(1,0,1,0)},
                         {'Output':(1,0,1),'Implementation':(2,1,1,0)},
                         {'Output':(1,0,2),'Implementation':(1,1,1,1)},
                         {'Output':(1,1,0),'Implementation':(1,1,0,0)},
                         {'Output':(1,1,1),'Implementation':(0,0,0,0)},
                         {'Output':(1,1,2),'Implementation':(1,1,0,0)},
                         {'Output':(1,2,0),'Implementation':(1,1,1,0)},
                         {'Output':(1,2,1),'Implementation':(2,1,1,0)},
                         {'Output':(1,2,2),'Implementation':(1,0,1,0)},
                         {'Output':(2,0,0),'Implementation':(0,0,1,0)},
                         {'Output':(2,0,1),'Implementation':(1,1,1,0)},
                         {'Output':(2,0,2),'Implementation':(1,1,1,0)},
                         {'Output':(2,1,0),'Implementation':(2,1,1,0)},
                         {'Output':(2,1,1),'Implementation':(1,0,1,0)},
                         {'Output':(2,1,2),'Implementation':(1,1,1,0)},
                         {'Output':(2,2,0),'Implementation':(0,1,0,0)},
                         {'Output':(2,2,1),'Implementation':(1,1,0,0)},
                         {'Output':(2,2,2),'Implementation':(0,0,0,0)}])


def Template(input_logic):

    """
    """

    Selection_row_0 = (input_logic[0,0],input_logic[0,1],input_logic[0,2]) #A Row wise NTI
    Selection_row_1 = (input_logic[1,0],input_logic[1,1],input_logic[1,2])
    Selection_row_2 = (input_logic[2,0],input_logic[2,1],input_logic[2,2]) #A Row wise PTI #Reduntant but useful for future renditions
    
    Selection_column_0 = (input_logic[0,0],input_logic[1,0],input_logic[2,0]) #B Column wise NTI
    Selection_column_1 = (input_logic[0,1],input_logic[1,1],input_logic[2,1])
    #print Selection_column_1
    Selection_column_2 = (input_logic[0,2],input_logic[1,2],input_logic[2,2]) #B Column wise PTI #Reduntant but useful for future renditions

    # Analysis Of the Truth Table
    Output_options = np.array([0,0,0,0,0,0,0])

    for i in np.arange(27):
        #print "*"

        if Selection_row_0 == combinations[i]['Output']:
            Output_options[0] = i
            #print "1"

        if Selection_row_0 == combinations[i]['Output']:
            Output_options[1] = i
            #print "1"

        if Selection_row_2 == combinations[i]['Output']:
            Output_options[2] = i
            #print "2"

        if Selection_column_0 == combinations[i]['Output']:
            Output_options[3] = i
            #print "3"

        if Selection_column_1 == combinations[i]['Output']:
            Output_options[4] = i
            
        if Selection_column_2 == combinations[i]['Output']:
            Output_options[5] = i
            #print "4"

    additional_INV_A =0
    additional_PTI_A =1
    additional_NTI_A =1
    additional_MUX_A =2

    additional_INV_B =0
    additional_PTI_B =1
    additional_NTI_B =1
    additional_MUX_B =2

    print "Cost Requirements for the truth table"
    print "If A is selected as the Select line"
    print "       ROW 1    "
    print "Number of Mux %d" %(combinations[Output_options[0]]['Implementation'][0])
    print "Number of PTI %d" %(combinations[Output_options[0]]['Implementation'][1])
    print "Number of NTI %d" %(combinations[Output_options[0]]['Implementation'][2])
    print "Number of BINV %d" %(combinations[Output_options[0]]['Implementation'][3])

    print "       ROW 2    "
    print "Number of Mux %d" %(combinations[Output_options[1]]['Implementation'][0])
    print "Number of PTI %d" %(combinations[Output_options[1]]['Implementation'][1])
    print "Number of NTI %d" %(combinations[Output_options[1]]['Implementation'][2])
    print "Number of BINV %d" %(combinations[Output_options[1]]['Implementation'][3])

    print "       ROW 3    "
    print "Number of Mux %d" %(combinations[Output_options[2]]['Implementation'][0])
    print "Number of PTI %d" %(combinations[Output_options[2]]['Implementation'][1])
    print "Number of NTI %d" %(combinations[Output_options[2]]['Implementation'][2])
    print "Number of BINV %d" %(combinations[Output_options[2]]['Implementation'][3])

    Total_Cost_A = (combinations[Output_options[0]]['Implementation'][0]+combinations[Output_options[1]]['Implementation'][0]+combinations[Output_options[2]]['Implementation'][0],
                    combinations[Output_options[0]]['Implementation'][1]+combinations[Output_options[1]]['Implementation'][1]+combinations[Output_options[2]]['Implementation'][1],
                    combinations[Output_options[0]]['Implementation'][2]+combinations[Output_options[1]]['Implementation'][2]+combinations[Output_options[2]]['Implementation'][2],
                    combinations[Output_options[0]]['Implementation'][3]+combinations[Output_options[1]]['Implementation'][3]+combinations[Output_options[2]]['Implementation'][3]
                    )
    print "\nIf B is selected as the Select line"
    print "    Column 1    "
    print "Number of Mux %d" %(combinations[Output_options[3]]['Implementation'][0])
    print "Number of PTI %d" %(combinations[Output_options[3]]['Implementation'][1])
    print "Number of NTI %d" %(combinations[Output_options[3]]['Implementation'][2])
    print "Number of BINV %d" %(combinations[Output_options[3]]['Implementation'][3])

    print "    Column 2    "
    print "Number of Mux %d" %(combinations[Output_options[4]]['Implementation'][0])
    print "Number of PTI %d" %(combinations[Output_options[4]]['Implementation'][1])
    print "Number of NTI %d" %(combinations[Output_options[4]]['Implementation'][2])
    print "Number of BINV %d" %(combinations[Output_options[4]]['Implementation'][3])

    print "     Column 3    "
    print "Number of Mux %d" %(combinations[Output_options[5]]['Implementation'][0])
    print "Number of PTI %d" %(combinations[Output_options[5]]['Implementation'][1])
    print "Number of NTI %d" %(combinations[Output_options[5]]['Implementation'][2])
    print "Number of BINV %d" %(combinations[Output_options[5]]['Implementation'][3])

    Total_Cost_B = (combinations[Output_options[3]]['Implementation'][0]+combinations[Output_options[4]]['Implementation'][0]+combinations[Output_options[5]]['Implementation'][0],
                    combinations[Output_options[3]]['Implementation'][1]+combinations[Output_options[4]]['Implementation'][1]+combinations[Output_options[5]]['Implementation'][1],
                    combinations[Output_options[3]]['Implementation'][2]+combinations[Output_options[4]]['Implementation'][2]+combinations[Output_options[5]]['Implementation'][2],
                    combinations[Output_options[3]]['Implementation'][3]+combinations[Output_options[4]]['Implementation'][3]+combinations[Output_options[5]]['Implementation'][3]
                    )
    print "Total_Cost_A"
    print Total_Cost_A
    print "Total_Cost_A"
    print Total_Cost_B
    #Implementation
            
truth_table = np.array([[2,1,0],[1,2,1],[0,2,1]])

print "Truth Table"
print "   0  1  2"
print "------------"
print "0| %d  %d  %d" %(truth_table[0,0],truth_table[0,1],truth_table[0,2])
print "1| %d  %d  %d" %(truth_table[1,0],truth_table[1,1],truth_table[1,2])
print "2| %d  %d  %d\n" %(truth_table[2,0],truth_table[1,1],truth_table[2,2])

Template(truth_table)
                        
