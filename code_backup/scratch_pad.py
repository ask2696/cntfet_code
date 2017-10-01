import numpy as np
from Template_BDD import Template_BDD


truth_table = np.array([[1,0,1],[1,1,0],[1,2,1]])

print "Truth Table"
print "   0  1  2"
print "------------"
print "0| %d  %d  %d" %(truth_table[0,0],truth_table[0,1],truth_table[0,2])
print "1| %d  %d  %d" %(truth_table[1,0],truth_table[1,1],truth_table[1,2])
print "2| %d  %d  %d\n" %(truth_table[2,0],truth_table[2,1],truth_table[2,2])

#decision_template(truth_table)


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

