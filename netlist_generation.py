import re

x = re.compile("([a-zA-Z]+)([0-9]+)")
module_no = 1

def NTI_module(net,I0,I2,Out,Sel):
        #XU1 I0 I2 Out S Mux_NTI
        #print ""
        global module_no
        out_net = "XU"+str(module_no)+" "+I0+" "+I2+" "+Out+" "+Sel+" "+ "Mux_NTI"
        net = net + out_net + "\n"
        module_no = module_no +1
        return net

def PTI_module(net,I0,I2,Out,Sel):
        #XU1 I0 I2 Out S Mux_PTI
        #print ""
        global module_no
        out_net = "XU"+str(module_no)+" "+I0+" "+I2+" "+Out+" "+Sel+" "+ "Mux_PTI"
        net = net + out_net + "\n"
        module_no = module_no +1
        return net

def len_2(netlist_sub,key,element,out_sel):
        #determine if NTI or PTI
        ele_1 = element[0]
        ele_2 = element[1]
        #print key,element
        out_ele_1 = x.match(ele_1)
        out_ele_2 = x.match(ele_2)
        print ele_1,ele_2

        if(out_ele_1.group(2) == '0' and out_ele_2.group(2) == '12'):
                print "NTI"
                if str.find(ele_1,'X')>=0:
                        sel_line = "In_1"
                elif str.find(ele_1,'Y')>=0:
                        sel_line = "In_2"
                #elif str.find(key,'F') >=0:
                #        index = str.find(key,'F')
                #        sel_line = key[index+1:len(key)]
                else:
                        sel_line = out_sel

                netlist_sub = NTI_module(netlist_sub,ele_2,ele_1,key,sel_line)



        elif(out_ele_1.group(2) == '2' and out_ele_2.group(2) =='01'):
                print "PTI"
                if str.find(ele_1,'X')>=0:
                        sel_line = "In_1"
                elif str.find(ele_1,'Y')>=0:
                        sel_line = "In_2"
                #elif str.find(key,'F') >=0:
                #        index = str.find(key,'F')
                #        sel_line = key[index+1:len(key)]
                else:
                        sel_line = out_sel

                netlist_sub = PTI_module(netlist_sub,ele_1,ele_2,key,sel_line)

        elif(out_ele_1.group(2) == '1' and out_ele_2.group(2) =='2'):
                print "PTI"
                if str.find(ele_1,'X')>=0:
                        sel_line = "In_1"
                elif str.find(ele_1,'Y')>=0:
                        sel_line = "In_2"
                #elif str.find(key,'F') >=0:
                #        index = str.find(key,'F')
                #        sel_line = key[index+1:len(key)]
                else:
                        sel_line = out_sel

                netlist_sub = PTI_module(netlist_sub,ele_1,ele_2,key,sel_line)

        #print netlist_sub
        return netlist_sub        
 


def len_1():
        print ""

def list_recursion(netlist_sub,key,element,inp_sub,out_sel):

        print key,element

        if(len(element) == 2):
                netlist_sub = len_2(netlist_sub,key,element,out_sel)
                for a in range(0,2):
                        new_key = element[a]
                        new_element = inp_sub[new_key]
                        netlist_sub  = list_recursion(netlist_sub,new_key,new_element,inp_sub,out_sel)


        elif (len(element) == 1):
                #netlist_sub = len_1(netlist_sub,key,element)
                temp_list = re.split(" ",netlist_sub)
                #netlist_sub = netlist_sub + key + " " + element[0] + "\n" 
                
                #print "####"
                for i in range(len(temp_list)):
                        if (temp_list[i] == key):
                                temp_list[i] = element[0]

                #print "####"
                netlist_sub =  " ".join(temp_list)
                #print temp_list
                #print "$$$$"
                #netlist_sub = netlist_sub.replace(key,element[0]) 

        return netlist_sub

def sub_module(out_sub,inp_sub):

        out_var = re.split('_',out_sub)
        out_sel = 'In'+out_var[1]
        print out_sel
        key_vals = ['FXY','F'+out_sel]
        no_lines = len(inp_sub)
        netlist_sub = ""

        for key in inp_sub:
                if key in key_vals:
                        #start recursion
                        print key
                        element = inp_sub[key]
                        netlist_sub = list_recursion(netlist_sub,key,element,inp_sub,out_sel)
                        netlist_sub = netlist_sub.replace(key,out_sub)
                        print netlist_sub
                        break;
                        





        
def main(inp):
        

        #print inp

        #print len(inp)
        
        sub_modules = []

        for key in inp:
                #print key
                sub_module(key,inp[key])
                break








if __name__ == "__main__":
        inp = {'F0_2_0': {'F00': [0],
  'F0Y': ['F00'],
  'F101': [0],
  'F12': [1],
  'F12Y': ['F1Y', 'F2Y'],
  'F1Y': ['F101', 'F12'],
  'F20': [0],
  'F212': [1],
  'F2Y': ['F20', 'F212'],
  'FXY': ['F0Y', 'F12Y']},
 'F0_2_1': {'F001': [0],
  'F01Y': ['F0Y', 'F1Y'],
  'F02': [1],
  'F0Y': ['F001', 'F02'],
  'F10': [0],
  'F112': [1],
  'F12': [1],
  'F1Y': ['F10', 'F112'],
  'F22': [1],
  'F2Y': ['F22'],
  'FXY': ['F01Y', 'F2Y']},
 'F0_2_2': {'F00': [0],
  'F0112': [1],
  'F120': [1],
  'F21': [1],
  'F212': ['F21', 'F22'],
  'F22': [2],
  'FX0': ['F00', 'F120'],
  'FX12': ['F0112', 'F212'],
  'FXY': ['FX0', 'FX12']},
 'F0_3_0': {'F0': ['F0_2_0'],
  'F1': ['F0_2_1'],
  'F12': ['F1', 'F2'],
  'F2': ['F0_2_2'],
  'FIn3': ['F0', 'F12']},
 'F1_2_0': {'F0Y': ['Y'],
  'F10': [1],
  'F112': ['PTIY'],
  'F12Y': ['F1Y', 'F2Y'],
  'F1Y': ['F10', 'F112'],
  'F201': ['NTIY'],
  'F22': [1],
  'F2Y': ['F201', 'F22'],
  'FXY': ['F0Y', 'F12Y']},
 'F1_2_1': {'F00': [1],
  'F012': ['PTIY'],
  'F01Y': ['F0Y', 'F1Y'],
  'F0Y': ['F00', 'F012'],
  'F101': ['NTIY'],
  'F12': [1],
  'F1Y': ['F101', 'F12'],
  'F2Y': ['Y'],
  'FXY': ['F01Y', 'F2Y']},
 'F1_2_2': {'F010': ['NTIX'],
  'F02': [1],
  'F122': ['PTIX'],
  'F20': [1],
  'FX0': ['F010', 'F20'],
  'FX1': ['X'],
  'FX12': ['FX1', 'FX2'],
  'FX2': ['F02', 'F122'],
  'FXY': ['FX0', 'FX12']},
 'F1_3_0': {'F0': ['F1_2_0'],
  'F1': ['F1_2_1'],
  'F12': ['F1', 'F2'],
  'F2': ['F1_2_2'],
  'FIn3': ['F0', 'F12']}}
        main(inp)
