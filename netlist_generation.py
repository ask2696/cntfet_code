import re
import ast

x = re.compile("([a-zA-Z]+)([0-9]+)")
module_no = 1
sub_modules_num = 1
check_submodule = ['F12','F12','F12','F12','F12','F12','F12','F12','F12','F12','F12']
signals_gen = []
replace_val = {}


def NTI_module(net,I0,I2,Out,Sel):
        #XU1 I0 I2 Out S Mux_NTI
        #print ""
        global module_no

        """
        if(len(I0) < 6):
          I0 = str(sub_modules_num)+I0
        if(len(I2)< 6):
          I2 = str(sub_modules_num)+I2
        if(len(Out)< 6):
          Out = str(sub_modules_num)+Out
          """

        #out_net = "XU"+str(module_no)+" "+I0+" "+I2+" "+Out+" "+Sel+" "+ "Mux_NTI"
        

                  
        out_net = "XU"+str(module_no)+" "+I0+" "+I2+" "+Out+" "+Sel+" "+"NTI_"+Sel+" "+ "Mux_N"
        net = net + out_net + "\n"
        module_no = module_no +1

        if ("NTI_"+Sel) not in signals_gen:
          #XU5 S S1 nti_gate
          out_net = "XU"+str(module_no)+" "+Sel+" "+"NTI_"+Sel+" "+"nti_gate"
          net = net + out_net + "\n"

          module_no = module_no +1
          signals_gen.append("NTI_"+Sel)


        return net

def PTI_module(net,I0,I2,Out,Sel):
        #XU1 I0 I2 Out S Mux_PTI
        #print ""
        global module_no
        
        """
        if(len(I0) < 6):
          I0 = str(sub_modules_num)+I0
        if(len(I2)< 6):
          I2 = str(sub_modules_num)+I2
        if(len(Out)< 6):
          Out = str(sub_modules_num)+Out
          """

        #out_net = "XU"+str(module_no)+" "+I0+" "+I2+" "+Out+" "+Sel+" "+ "Mux_PTI"
        out_net = "XU"+str(module_no)+" "+I0+" "+I2+" "+Out+" "+Sel+" "+"PTI_"+Sel+" "+ "Mux_P"
        net = net + out_net + "\n"
        module_no = module_no +1

        if ("PTI_"+Sel) not in signals_gen:
          #XU5 S S1 pti_gate
          out_net = "XU"+str(module_no)+" "+Sel+" "+"PTI_"+Sel+" "+"pti_gate"
          net = net + out_net + "\n"
          module_no = module_no +1
          signals_gen.append("PTI_"+Sel)

        return net

def len_2(netlist_sub,key,element,out_sel):
        #determine if NTI or PTI
        ele_1 = element[0]
        ele_2 = element[1]
        #$#print "$$"
        #$#print key,element
        out_ele_1 = x.match(ele_1)
        out_ele_2 = x.match(ele_2)
        #$#print ele_1,ele_2

        if(out_ele_1.group(2) == '0' and out_ele_2.group(2) == '12'):
                #$#print "NTI"
                if str.find(ele_1,'X')>=0:
                        sel_line = "In1"
                elif str.find(ele_1,'Y')>=0:
                        sel_line = "In2"
                #elif str.find(key,'F') >=0:
                #        index = str.find(key,'F')
                #        sel_line = key[index+1:len(key)]
                else:
                        sel_line = out_sel

                netlist_sub = NTI_module(netlist_sub,ele_2,ele_1,key,sel_line)

        elif(out_ele_1.group(2) == '12' and out_ele_2.group(2) == '0'):
                #$#print "NTI"
                if str.find(ele_1,'X')>=0:
                        sel_line = "In1"
                elif str.find(ele_1,'Y')>=0:
                        sel_line = "In2"
                #elif str.find(key,'F') >=0:
                #        index = str.find(key,'F')
                #        sel_line = key[index+1:len(key)]
                else:
                        sel_line = out_sel

                netlist_sub = NTI_module(netlist_sub,ele_1,ele_2,key,sel_line)



        elif(out_ele_1.group(2) == '2' and out_ele_2.group(2) =='01'):
                #$#print "PTI"
                if str.find(ele_1,'X')>=0:
                        sel_line = "In1"
                elif str.find(ele_1,'Y')>=0:
                        sel_line = "In2"
                #elif str.find(key,'F') >=0:
                #        index = str.find(key,'F')
                #        sel_line = key[index+1:len(key)]
                else:
                        sel_line = out_sel

                netlist_sub = PTI_module(netlist_sub,ele_1,ele_2,key,sel_line)

        elif(out_ele_1.group(2) == '01' and out_ele_2.group(2) =='2'):
                #$#print "PTI"
                if str.find(ele_1,'X')>=0:
                        sel_line = "In1"
                elif str.find(ele_1,'Y')>=0:
                        sel_line = "In2"
                #elif str.find(key,'F') >=0:
                #        index = str.find(key,'F')
                #        sel_line = key[index+1:len(key)]
                else:
                        sel_line = out_sel

                netlist_sub = PTI_module(netlist_sub,ele_2,ele_1,key,sel_line)

        elif(out_ele_1.group(2) == '1' and out_ele_2.group(2) =='2'):
                #$#print "PTI"
                if str.find(ele_1,'X')>=0:
                        sel_line = "In1"
                elif str.find(ele_1,'Y')>=0:
                        sel_line = "In2"
                #elif str.find(key,'F') >=0:
                #        index = str.find(key,'F')
                #        sel_line = key[index+1:len(key)]
                else:
                        sel_line = out_sel

                netlist_sub = PTI_module(netlist_sub,ele_2,ele_1,key,sel_line)

        elif(out_ele_1.group(2) == '2' and out_ele_2.group(2) =='1'):
                #$#print "PTI"
                if str.find(ele_1,'X')>=0:
                        sel_line = "In1"
                elif str.find(ele_1,'Y')>=0:
                        sel_line = "In2"
                #elif str.find(key,'F') >=0:
                #        index = str.find(key,'F')
                #        sel_line = key[index+1:len(key)]
                else:
                        sel_line = out_sel

                netlist_sub = PTI_module(netlist_sub,ele_1,ele_2,key,sel_line)

        elif(out_ele_1.group(2) == '0' and out_ele_2.group(2) =='1'):
                #$#print "NTI"
                if str.find(ele_1,'X')>=0:
                        sel_line = "In1"
                elif str.find(ele_1,'Y')>=0:
                        sel_line = "In2"
                #elif str.find(key,'F') >=0:
                #        index = str.find(key,'F')
                #        sel_line = key[index+1:len(key)]
                else:
                        sel_line = out_sel

                netlist_sub = NTI_module(netlist_sub,ele_2,ele_1,key,sel_line)

        elif(out_ele_1.group(2) == '1' and out_ele_2.group(2) =='0'):
                #$#print "NTI"
                if str.find(ele_1,'X')>=0:
                        sel_line = "In1"
                elif str.find(ele_1,'Y')>=0:
                        sel_line = "In2"
                #elif str.find(key,'F') >=0:
                #        index = str.find(key,'F')
                #        sel_line = key[index+1:len(key)]
                else:
                        sel_line = out_sel

                netlist_sub = NTI_module(netlist_sub,ele_1,ele_2,key,sel_line)

        elif str.find(key,'Y')>=0:
                #$#print "%%%%%%"
                start = str.find(key,'Y')
                #print start
                sel_line = "In1"
                if (ele_1[start:len(ele_1)] == '0' and ele_2[start:len(ele_2)] == '12') :
                        #$#print "NTI"
                        netlist_sub = NTI_module(netlist_sub,ele_2,ele_1,key,sel_line)

                if (ele_1[start:len(ele_1)] == '01' and ele_2[start:len(ele_2)] == '2') :
                        #$#print "PTI"
                        netlist_sub = PTI_module(netlist_sub,ele_2,ele_1,key,sel_line)

                if (ele_1[start:len(ele_1)] == '2' and ele_2[start:len(ele_2)] == '01') :
                        #$#print "PTI"
                        netlist_sub = PTI_module(netlist_sub,ele_1,ele_2,key,sel_line)

                if (ele_1[start:len(ele_1)] == '12' and ele_2[start:len(ele_2)] == '0') :
                        #$#print "NTI"
                        netlist_sub = NTI_module(netlist_sub,ele_1,ele_2,key,sel_line)

        elif str.find(key,'X')>=0:
                #$#print "^^^^^^^"
                start = str.find(key,'X')
                #print start
                sel_line = "In2"
                if (ele_1[start:start+1] == '0' and ele_2[start:start+2] == '12') :
                        #$#print "NTI"
                        netlist_sub = NTI_module(netlist_sub,ele_2,ele_1,key,sel_line)

                if (ele_1[start:start+2] == '01' and ele_2[start:start+1] == '2') :
                        #$#print "PTI"
                        netlist_sub = PTI_module(netlist_sub,ele_2,ele_1,key,sel_line)

                if (ele_1[start:start+1] == '2' and ele_2[start:start+2] == '01') :
                        #$#print "PTI"
                        netlist_sub = PTI_module(netlist_sub,ele_1,ele_2,key,sel_line)

                if (ele_1[start:start+2] == '12' and ele_2[start:start+1] == '0') :
                        #$#print "NTI"
                        netlist_sub = NTI_module(netlist_sub,ele_1,ele_2,key,sel_line)
        else:
                first_val = key[1]
                last_val = key[len(key)-1]

                if ((out_ele_1.group(2)[0] == first_val) and (out_ele_2.group(2)[0] == first_val)) :
                        sel_line = "In1"
                        el1 =  out_ele_1.group(2)[len(out_ele_1.group(2))-1]
                        el2 =  out_ele_2.group(2)[len(out_ele_2.group(2))-1]

                elif (((out_ele_1.group(2)[len(out_ele_1.group(2))-1]) == last_val) and ((out_ele_2.group(2)[len(out_ele_2.group(2))-1]) == last_val) ):
                        sel_line = "In2"
                        el1 =  out_ele_1.group(2)[0]
                        el2 =  out_ele_2.group(2)[0]

                #$#else:
                        #$#print "****()"

                if el1 == '0' and el2 == '1':
                        netlist_sub = NTI_module(netlist_sub,ele_2,ele_1,key,sel_line)
                if el1 == '1' and el2 == '0':
                        netlist_sub = NTI_module(netlist_sub,ele_1,ele_2,key,sel_line)
                if el1 == '1' and el2 == '2':
                        netlist_sub = PTI_module(netlist_sub,ele_2,ele_1,key,sel_line)
                if el1 == '2' and el2 == '1':
                        netlist_sub = PTI_module(netlist_sub,ele_1,ele_2,key,sel_line)

        #print netlist_sub
        return netlist_sub        
 


#$#def len_1():
        #$#print ""

def list_recursion(netlist_sub,key,element,inp_sub,out_sel):
        """
        #def
        #netlist_sub = string of the netlist subsection to be given as output of this def
        #key = the key of the section in subsection i.e netlist_sub
        #element = the value of the key i.e the subsection of subsection 
        #inp_sub = the whole subsection
        #out_sel = the select line for the subsection
        """

        #$#print "##"
        #$#print key,element

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
                        #print type(element[0])

                        if (temp_list[i] == key):
                                if str(type(element[0])) == "<type 'int'>":
                                        temp_list[i] = str(element[0])
                                else:
                                        temp_list[i] = element[0]


                #print "####"
                netlist_sub =  " ".join(temp_list)

                check_keys = inp_sub.keys()

                if element[0] in check_keys :
                  new_key = element[0]
                  new_element = inp_sub[new_key]
                  netlist_sub  = list_recursion(netlist_sub,new_key,new_element,inp_sub,out_sel)
                  print inp_sub

                #print temp_list
                #print "$$$$"
                #netlist_sub = netlist_sub.replace(key,element[0]) 

        return netlist_sub

def sub_module(out_sub,inp_sub):

        out_var = re.split('_',out_sub)
        out_sel = 'In'+out_var[1]
        #$#print out_sel
        key_vals = ['FXY','F'+out_sel]
        no_lines = len(inp_sub)
        netlist_sub = ""
       # print inp_sub
        global sub_modules_num
        for key in inp_sub:

                if key in key_vals:
                        #start recursion
                        #$#print key
                        element = inp_sub[key]
                        netlist_sub = list_recursion(netlist_sub,key,element,inp_sub,out_sel)
                        netlist_sub = netlist_sub.replace(key,out_sub)
                        #$#print netlist_sub
                        break
        
        return netlist_sub
 
def final_val(in_dict):
    for key in in_dict:
      if(str(type(in_dict[key]))== "<type 'dict'>"):
        out = final_val(in_dict[key])
      else:
        return in_dict[key]
    return out

        
def main(inp):
        

        #print inp

        #print len(inp)
        master_netlist = ""
        sub_modules = {}
        map_signal = {'0':'V_0','1':'V_1','2':'V_2'}

        
        global sub_modules_num
        global replace_val

        for key in inp:
                print key
                out_net_submodule = sub_module(key,inp[key])

               #print sub_modules_num
                #print "$$$$$$$$$$$"
                #print out_net_submodule
                temp_out = re.split(' ',out_net_submodule)
                #print temp_out
                for i in range(len(temp_out)):
                  """
                  if (str.find(temp_out[i],'Mux')>=0):
                    sig = temp_out[i-2]
                    if(temp_out[i]== "Mux_N"):
                      if "NTI_"+sig not in signals_gen:
                  """
                  if(str.find(temp_out[i],'XU')>=0) or (str.find(temp_out[i],'_')>=0) or (str.find(temp_out[i],'In')>=0) or (str.find(temp_out[i],'Mux')>=0):
                    i = i
                  elif(temp_out[i] in ['0','1','2']):
                    temp_out[i] = map_signal[temp_out[i]]
                  elif(temp_out[i] == 'X'):
                    temp_out[i] = 'In_2'
                  elif(temp_out[i] == 'Y'):
                    temp_out[i] = 'In1'
                  
                  elif(temp_out[i] == 'NTIX') or (temp_out[i] == 'PTIX'):
                    #print type(temp_out[i])
                    temp_out[i] = temp_out[i].replace('X','_In2')
                    #print temp_out[i]
                  elif(temp_out[i] == 'NTIY') or (temp_out[i] == 'PTIY'):
                    temp_out[i] = temp_out[i].replace('Y','_In1')
                  elif(temp_out[i] == 'NTIYB') or (temp_out[i] == 'PTIYB'):
                    temp_out[i] = temp_out[i].replace('Y','_In1')
                  elif(temp_out[i] == 'NTIYB') or (temp_out[i] == 'PTIYB'):
                    temp_out[i] = temp_out[i].replace('Y','_In1')
                    temp_out[i] = temp_out[i].replace('N','B_N')
                    temp_out[i] = temp_out[i].replace('P','B_P')
                    temp_out[i] = temp_out[i].replace('B','')

                  elif(temp_out[i] == 'NTIXB') or (temp_out[i] == 'PTIXB'):
                    temp_out[i] = temp_out[i].replace('X','_In2')
                    temp_out[i] = temp_out[i].replace('N','B_N')
                    temp_out[i] = temp_out[i].replace('P','B_P')
                    temp_out[i] = temp_out[i].replace('B','')

                  else:
                    temp_out[i] = str(sub_modules_num) + temp_out[i]
                if len(temp_out) == 1:
                  #print final_val(inp[key])
                  replace_item = final_val(inp[key])[0]
                  #print replace_item 
                  if replace_item in [0,1,2]:
                    #print '$'
                    replace_val[key] = map_signal[str(replace_item)]
                  else:
                    replace_val[key] = replace_item

                  #print '#'
                else:
                  out_net_submodule = " ".join(temp_out)
                #print temp_out
                #print "$$$$$$$$$$$"
                sub_modules_num = sub_modules_num +1
                sub_modules[key] = out_net_submodule 
                master_netlist = master_netlist + out_net_submodule
        
        #replace_values

        temp_master = re.split(" ",master_netlist)
        keys = replace_val.keys()
        #####################
        #print replace_val
        for key in keys:
          try:
            if replace_val[key] in keys:
              if replace_val[replace_val[key]] in keys:
                replace_val[key] = replace_val[replace_val[replace_val[key]]]
              else:
                replace_val[key] = replace_val[replace_val[key]]
          except:
            print ""

        keys = replace_val.keys()
        #print keys
        #print replace_val

        for i in range(len(temp_master)):
          if(temp_master[i] in keys):
            #print "*"
            temp_master[i] = replace_val[temp_master[i]]
            #print temp_master[i]

        master_netlist = " ".join(temp_master)
        #print sub_modules
        print "#############"
        print master_netlist
        print "#############"

        #print replace_val

        return master_netlist







if __name__ == "__main__":
  dir_loc = "./netlist/"
  files = ["Test_3_2_In.txt","Test_5_3_withIn.txt"]
  file_read = open(dir_loc+files[1],'r')
  inp = file_read.read()
  inp = ast.literal_eval(inp)
  #print type(inp)
  out_netlist = main(inp)
  filename = "./netlist/net_5_3.txt"
  file = open(filename,"w")
  file.write(out_netlist)
