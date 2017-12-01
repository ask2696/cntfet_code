

class Node:
    def __init__(self,left_branch_in,right_branch_in,left_val,right_val):
        self.left_branch = left_branch_in
        self.right_branch = right_branch_in
        self.left_value = left_val
        self.right_value = right_val
        #self.value = val

class Tree:
    def __init__(self,left_branch_in,right_branch_in,left_val,right_val):
        self.left_branch = left_branch_in
        self.right_branch = right_branch_in
        self.left_value = left_val
        self.right_value = right_val

Node1 = Node((2),(0,1),0,1)        
stage_1 = Tree(0,(1,2),(2),Node1)

input_tree = 2

if(input_tree == stage_1.left_branch):
    print stage_1.left_value

elif(input_tree == stage_1.right_branch[0] or input_tree == stage_1.right_branch[1]):
    #Process Node to see how it is structured
    if(input_tree == Node1.left_branch):
        print Node1.left_value

    elif(input_tree == Node1.right_branch[0] or input_tree == Node1.right_branch[1]):
        print Node1.right_value
    

        
