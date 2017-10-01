import numpy as np
import copy

"""
Author:

Description:
1. node: represents the most basic unit of the TDD with following def

        select_line
        left_branch
        right_branch
        left_value
        right_value
        
2. remnant: takes the input of a either 0,1 or 2 and returns the remaining tuple from {0,1,2}
            For eg: Input of 0 gives (1,2)

3. PTI_logic: returns the PTI output of the input

4. NTI_logic: returns the NTI output of the input

5. INV_logic: returns the Binary Inverter output of the input.

6. combinations_3_3: An array of dictionaries with the dictionary structure as follows:
                    {'Output':       ,'Implementation':      ,'BDD':   }
                    Output represents the tuple that is expected when (0,1,2) is the input
                    Implementation gives the implementation cost in terms of a tuple (Mux,PTI,NTI,B_INV)
                    BDD/TDD : gives the TDD structure for the mapping
    
        
"""

class node:
    def __init__(self,select_line,left_branch,right_branch,left_value,right_value):
        self.select_line = select_line
        self.left_branch = left_branch
        self.right_branch = right_branch
        self.left_value = left_value
        self.right_value = right_value


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


#                          Output paralell to (0,1,2) Cost behaviour (Mux,PTI,NTI,B_INV)
combinations_3_3 = np.array([{'Output':(0,0,0),'Implementation':(0,0,0,0),'BDD':(0)},
                         {'Output':(0,0,1),'Implementation':(1,1,0,0),'BDD':node('X',(2),(0,1),(1),(0))},
                         {'Output':(0,0,2),'Implementation':(0,1,0,1),'BDD':'INV(PTI(X))'},
                         {'Output':(0,1,0),'Implementation':(1,1,0,0),'BDD':node('X',(2),(0,1),(0),'X')},
                         {'Output':(0,1,1),'Implementation':(1,0,1,0),'BDD':node('X',(0),(1,2),(0),(1))},
                         {'Output':(0,1,2),'Implementation':(0,0,0,0),'BDD':" X "},
                         {'Output':(0,2,0),'Implementation':(1,1,1,0),'BDD':node('X',(0),(1,2),(0),'PTI(X)')},
                         {'Output':(0,2,1),'Implementation':(1,1,0,1),'BDD':node('X',(2),(0,1),(1),'INV(NTI(X))')},
                         {'Output':(0,2,2),'Implementation':(0,0,1,1),'BDD':'INV(NTI(X))'},
                         {'Output':(1,0,0),'Implementation':(1,0,1,0),'BDD':node('X',(0),(1,2),(1),(0))},
                         {'Output':(1,0,1),'Implementation':(2,1,1,0),'BDD':node('X',(0),(1,2),(1),node('X',(2),(0,1),(1),(0)))},
                         {'Output':(1,0,2),'Implementation':(1,1,1,1),'BDD':node('X',(0),(1,2),(1),'INV(PTI(X))')},
                         {'Output':(1,1,0),'Implementation':(1,1,0,0),'BDD':node('X',(2),(0,1),(0),(1))},
                         {'Output':(1,1,1),'Implementation':(0,0,0,0),'BDD':(1)},
                         {'Output':(1,1,2),'Implementation':(1,1,0,0),'BDD':node('X',(2),(0,1),(2),(1))},
                         {'Output':(1,2,0),'Implementation':(1,1,1,0),'BDD':node('X',(0),(1,2),(1),'PTI(X)')},
                         {'Output':(1,2,1),'Implementation':(2,1,1,0),'BDD':node('X',(0),(1,2),(1),node('X',(2),(0,1),(2),(1)))},
                         {'Output':(1,2,2),'Implementation':(1,0,1,0),'BDD':node('X',(0),(1,2),(1),(2))},
                         {'Output':(2,0,0),'Implementation':(0,0,1,0),'BDD':"NTI(X)"},
                         {'Output':(2,0,1),'Implementation':(1,1,1,0),'BDD':node('X',(2),(0,1),(1),'NTI(X)')},
                         {'Output':(2,0,2),'Implementation':(1,1,1,0),'BDD':node('X',(2),(0,1),(2),'NTI(X)')},
                         {'Output':(2,1,0),'Implementation':(2,1,1,0),'BDD':node('X',(0),(1,2),(2),node('X',(2),(0,1),(0),(1)))},
                         {'Output':(2,1,1),'Implementation':(1,0,1,0),'BDD':node('X',(0),(1,2),(2),(1))},
                         {'Output':(2,1,2),'Implementation':(1,0,1,0),'BDD':node('X',(0),(1,2),(2),'X')},
                         {'Output':(2,2,0),'Implementation':(0,1,0,0),'BDD':"PTI(X)"},
                         {'Output':(2,2,1),'Implementation':(1,1,0,0),'BDD':node('X',(2),(0,1),(1),(2))},
                         {'Output':(2,2,2),'Implementation':(0,0,0,0),'BDD':(2)}])


#                    Output paralell to (x,y)    Ouput (x',y')    Cost behaviour (Mux,PTI,NTI,B_INV)
"""
combinations_2_2 = np.array([{'Mapping':(0,0),'Output':(0,0),'Implementation':(0,0,0,0)},
                             {'Mapping':(0,0),'Output':(0,0),'Implementation':(0,0,0,0)}])
"""

# Isolates the cases of 2 deg complexity and the NTI and PTI flexibity opportunities

mux_2_1_red =np.array([{'Output':(2,1,0),0:(2,1,1),1:(2,1,2),2:(0,1,0),3:(1,1,0)},
                   {'Output':(1,0,1),0:(1,0,2),1:(1,0,0),2:(0,0,1),3:(2,0,1)},
                   {'Output':(1,2,1),0:(1,2,0),1:(1,2,2),2:(0,2,1),3:(2,2,1)}])
                             


def combinations_3_3_bdd(inp,sl):
    out = None
    for i in np.arange(27):
        if (inp == combinations_3_3[i]['Output']):
            out = copy.copy(combinations_3_3[i]['BDD'])
            #print "pliss",out.right_value
            if(str(type(out)) == "<type 'instance'>"):
                out.select_line = sl
                #print "             %s               "%(out.select_line)
                #print "       (%d)/     \(%d,%d)          "%(out.left_branch,out.right_branch[0],out.right_branch[1])
                
                if(str(type(out.right_value)) == "<type 'instance'>"):
                    out.right_value.select_line = sl
                    #print "     %d            %s          "%(out.left_value,out.right_value.select_line)
                    #print "               %d/            \(%d,%d)          "%(out.right_value.left_branch,out.right_value.right_branch[0],out.right_value.right_branch[1])
                    #print "             %d                 %d        "%(out.right_value.left_value,out.right_value.right_value)
                else:
                    if(str(type(out.right_value)) == "<type 'str'>"):
                        #out.right_value[out.right_value.find('X')] = sl
                        #print "#",out.right_value
                        new = list(out.right_value)
                        new[out.right_value.find('X')] = sl
                        #print new
                        out.right_value =''.join(new)
                        #print "     %d            %s          "%(out.left_value,out.right_value)
                    #else:
                        #print "     %d            %d          "%(out.left_value,out.right_value)
            else:
                if str(type(out)) == "<type 'str'>":
                    if out.find('X'):
                        #out[out.find('X')] =sl
                        new = list(out)
                        new[out.find('X')] = sl
                        out =''.join(new)
                        #print out,sl
                    
                #print out
            

    return out

def print_combinations_3_3_bdd(inp,sl):
    for i in np.arange(27):
        if (combinations_3_3[i]['Output'] == inp ):
            out = combinations_3_3[i]['BDD']
            if(str(type(out)) == "<type 'instance'>"):
                out.select_line = sl
                print "             %s               "%(out.select_line)
                print "       (%d)/     \(%d,%d)          "%(out.left_branch,out.right_branch[0],out.right_branch[1])
                
                if(str(type(out.right_value)) == "<type 'instance'>"):
                    out.right_value.select_line = sl
                    print "     %d            %s          "%(out.left_value,out.right_value.select_line)
                    print "               %d/            \(%d,%d)          "%(out.right_value.left_branch,out.right_value.right_branch[0],out.right_value.right_branch[1])
                    print "             %d                 %d        "%(out.right_value.left_value,out.right_value.right_value)
                else:
                    if(str(type(out.right_value)) == "<type 'str'>"):
                        #out.right_value[out.right_value.find('X')] = sl
                        
                        new = list(out.right_value)
                        new[out.right_value.find('X')] = sl
                        out.right_value =''.join(new)
                        print "     %d            %s          "%(out.left_value,out.right_value)
                    else:
                        print "     %d            %d          "%(out.left_value,out.right_value)
            else:
                if str(type(out)) == "<type 'str'>":
                    if out.find('X'):
                        out[out.find('X')] =sl
                        new = list(out)
                        new[out.find('X')] = sl
                        out =''.join(new)
                        #print out,sl

def print_btTDD(node_graph):

    try:
        print "                         ",node_graph.select_line,"               "
        print "                ",node_graph.left_branch,"    ",node_graph.right_branch,"       "
        if(str(type(node_graph.left_value)) == "<type 'instance'>"):
            print "      ",node_graph.left_value.select_line,"    "
            print "   ",node_graph.left_value.left_branch,"     ",node_graph.left_value.right_branch
            if str(type(node_graph.left_value.right_value)) == "<type 'instance'>":
                print "  ",node_graph.left_value.left_value," ",node_graph.left_value.right_value.select_line
                print "                  #",node_graph.left_value.right_value.left_branch,"    ",node_graph.left_value.right_value.right_branch
                print "                               ",node_graph.left_value.right_value.left_value,"     ",node_graph.left_value.right_value.right_value
            else:
                print "",node_graph.left_value.left_value,"          ",node_graph.left_value.right_value
        else:
            print "  ",node_graph.left_value

        #print node_graph.right_value

        if(str(type(node_graph.right_value)) == "<type 'instance'>"):
            print "                                 ",node_graph.right_value.select_line,"    "
            print "                        ",node_graph.right_value.left_branch,"     ",node_graph.right_value.right_branch

            if(str(type(node_graph.right_value.left_value)) == "<type 'instance'>"):
                print "            ",node_graph.right_value.left_value.select_line,"                                          "
                print "          ",node_graph.right_value.left_value.left_branch,"    ",node_graph.right_value.left_value.right_branch
                print "        ",node_graph.right_value.left_value.left_value,"             ",node_graph.right_value.left_value.right_value
                
            else:
                print "       ",node_graph.right_value.left_value
                
            if str(type(node_graph.right_value.right_value)) == "<type 'instance'>":
                print "                                                           ",node_graph.right_value.right_value.select_line
                print "                                                  ",node_graph.right_value.right_value.left_branch,"    ",node_graph.right_value.right_value.right_branch
                print "                                                ",node_graph.right_value.right_value.left_value,"     ",node_graph.right_value.right_value.right_value
            else:
                print "                                              ",node_graph.right_value.right_value
                
            
        else:
            print "                                    ",node_graph.right_value

    except:
        print node_graph


def is_instance(sub_node,cost_matrix):

    if sub_node.select_line == 'A':
        i_cost_matrix = 0
        #print "#"
    elif sub_node.select_line == 'B':
        i_cost_matrix = 1
        #print "$"

    if sub_node.left_branch == (0):#NTI
        cost_matrix[i_cost_matrix][0] = cost_matrix[i_cost_matrix][0] + 1
        cost_matrix[i_cost_matrix][2] = cost_matrix[i_cost_matrix][2] + 1

    elif sub_node.left_branch == (2):#PTI
        cost_matrix[i_cost_matrix][1] = cost_matrix[i_cost_matrix][1] + 1
        cost_matrix[i_cost_matrix][3] = cost_matrix[i_cost_matrix][3] + 1

    return cost_matrix



def is_string(str_inp,cost_matrix):

    if str_inp.find('A') > 0:
        i_cost_matrix= 0
        #print "#"
    elif str_inp.find('B') >0:
        i_cost_matrix= 1
        #print "$"

    if str_inp.find('NTI'):
        cost_matrix[i_cost_matrix][2] = cost_matrix[i_cost_matrix][2]+1
    elif str_inp.find('PTI'):
        cost_matrix[i_cost_matrix][3] = cost_matrix[i_cost_matrix][3]+1
    elif str_inp.find('INV'):
        cost_matrix[i_cost_matrix][4] = cost_matrix[i_cost_matrix][4]+1
    
    return cost_matrix

def node_recursive(node_element,cost_matrix):

    if str(type(node_element.left_value)) == "<type 'instance'>":
        cost_matrix = is_instance(node_element.left_value,cost_matrix)
        cost_matrix = node_recursive(node_element.left_value,cost_matrix)

    elif str(type(node_element.left_value)) == "<type 'str'>":
        cost_matrix = is_string(node_element.left_value,cost_matrix) 

    if str(type(node_element.right_value)) == "<type 'instance'>":
        cost_matrix = is_instance(node_element.right_value,cost_matrix)
        cost_matrix = node_recursive(node_element.right_value,cost_matrix)

    elif str(type(node_element.right_value)) == "<type 'str'>":
        cost_matrix = is_string(node_element.right_value,cost_matrix)

    return cost_matrix


def transistor_count(node_graph):

            #Acc to tex section, (NTI_Mux,PTI_Mux,NTI,PTI,B_INV)
    cost_vector = [0,0,0,0,0]

    cost_vector_A = [0,0,0,0,0]
    cost_vector_B = [0,0,0,0,0]

    cost_table = [[0,0,0,0,0],[0,0,0,0,0]] 
    
    trans_count_val = [0,0,0,0,0]
    total_transistor_count = 0

    if str(type(node_graph)) == "<type 'str'>" or str(type(node_graph)) == "<type 'int'>":
        cost_table = is_string(node_graph,cost_table)

    elif str(type(node_graph)) == "<type 'instance'>":

        cost_table = is_instance(node_graph,cost_table)
        #print cost_table

        cost_table = node_recursive(node_graph,cost_table)

        """
        if node_graph.select_line == 'A':
            if node_graph.left_branch == 0:
                cost_vector_A[0] = cost_vector_A[0]+1
                cost_vector_A[2] = cost_vector_A[2]+1 
            elif node_graph.left_branch == 2:
                cost_vector_A[1] = cost_vector_A[1]+1
                cost_vector_A[3] = cost_vector_A[3]+1
        """        
        """
            if str(type(node_graph.left_value)) == "<type 'str'>":
                if str(type(node_graph.left_value)) == 'PTI(B)':
        """
         
    

    return cost_table
        










#print type(str())
#outp = combinations_3_3_bdd((0,2,1),'B')
#outp = combinations_3_3_bdd((0,2,1),'B')
#outpe = combinations_3_3_bdd((0,2,1),'B')
#print outpe.right_value
#print type(str())
#print str(type(outp.right_value)) == "<type 'instance'>"
"""
outp = combinations_3_3_bdd((0,0,1),'A')
print outp.select_line
print outp.left_branch
print outp.right_branch
print outp.left_value
print outp.right_value
"""

#print len(mux_2_1_red)




