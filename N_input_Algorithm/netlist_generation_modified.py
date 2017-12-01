import re
import ast

module_no =0
replace_labels ={}

def NTI_module(net,I0,I2,Out,Sel):
        #XU1 I0 I2 Out S Mux_NTI
        print "NTI Module"
        net_module = ""
        global module_no

        net_module = "XU"+str(module_no)+" "+I0+" "+I2+" "+Out+" "+Sel+" "+"NTI_"+Sel+" "+ "Mux_N"+"\n"
        module_no = module_no +1

        return net_module


def PTI_module(net,I0,I2,Out,Sel):
        #XU1 I0 I2 Out S Mux_PTI
        print "PTI Module"
        net_module = ""
        global module_no

        net_module = "XU"+str(module_no)+" "+I0+" "+I2+" "+Out+" "+Sel+" "+"PTI_"+Sel+" "+ "Mux_P"+"\n"
        module_no = module_no +1

        return net_module

def decode_len2(key,inp_module):
	element1 = inp_module[0]
	element2 = inp_module[1]

	print element1,element2

	index_in1 = str.find(element1,"In")
	index_in2 = str.find(element2,"In")

	#!Limitation#
	if(index_in1 >= 0):
		sel_line = "In"+element1[index_in1+2]
	elif (index_in2 >= 0):
		sel_line = "In"+element2[index_in2+2]

	#print index_in1,index_in2,,element2[index_in2+2]
	print sel_line
	split_element1 = re.split('_',element1)
	split_element2 = re.split('_',element2)

	mux_label1 =  split_element1[-1]
	mux_label2 = split_element2[-1]
	print "Labels"
	print mux_label1,mux_label2
	net_decode2 =""

	if(mux_label1 == "01" and mux_label2 == "2"):
		print "PTI"
		net_decode2 = PTI_module("",element2,element1,key,sel_line)

	elif(mux_label1 == "2" and mux_label2 == "01"):
		print "PTI"
		net_decode2 = PTI_module("",element1,element2,key,sel_line)

	elif(mux_label1 == "2" and mux_label2 == "1"):
		print "PTI"
		net_decode2 = PTI_module("",element1,element2,key,sel_line)
	
	elif(mux_label1 == "1" and mux_label2 == "2"):
		print "PTI"
		net_decode2 = PTI_module("",element2,element1,key,sel_line)

	elif(mux_label1 == "0" and mux_label2 == "12"):
		print "NTI"

		net_decode2 = NTI_module("",element2,element1,key,sel_line)

	elif(mux_label1 == "12" and mux_label2 == "0"):
		print "NTI"

		net_decode2 = NTI_module("",element1,element2,key,sel_line)

	elif(mux_label1 == "1" and mux_label2 == "0"):
		print "NTI"

		net_decode2 = NTI_module("",element1,element2,key,sel_line)

	elif(mux_label1 == "0" and mux_label2 == "1"):
		print "NTI"

		net_decode2 = NTI_module("",element2,element1,key,sel_line)
	else:
		print "                                   New Case 2"
	return net_decode2

def list_recursion(key,inp_module,net_out,init_inp):

	global replace_labels
	
	if len(inp_module)== 2:
		net_temp = decode_len2(key,inp_module)
		net_out = net_out + net_temp

		for a in range(2):
			net_out = list_recursion(inp_module[a],init_inp[inp_module[a]],net_out,init_inp)
			

	elif len(inp_module)== 1: 
		print "#"
		print key,inp_module

		print type(init_inp[key])
		#collect replace val
		if len(init_inp[key]) ==1:
			if(str(type(init_inp[key])) == "<type 'dict'>"):
				print "2"
				find_final_val =""
				temp_dic = init_inp[key]
				for i in temp_dic:
					find_final_val = temp_dic[i]

				replace_labels[key] = find_final_val
			elif(str(type(init_inp[key])) == "<type 'list'>"):
				replace_labels[key] = init_inp[key]

		else:
			print "New Case 1"
	else:
		print "                                       New Case 3"
		print key,len(inp_module)
		print inp_module
		

	return net_out

def main(inp):
	num_out = 0
	for key in inp:
		print key,inp[key]
		if(re.split('_',key)[0] == "FOUT"):
			num_out = num_out +1

	print "$$$$$$$$$$$$$$$$$$$$"
	print num_out

	final_net = ""
	for i in range(num_out):
		print "FOUT_"+str(i)
		key = "FOUT_"+str(i)
		net_out = ""
		net_out = list_recursion(key,inp["FOUT_"+str(i)],net_out,inp)
		print net_out
		final_net = final_net + net_out
		print "############"
		#print inp["FOUT_"+str(i)]

	
	print final_net
	print "********"
	#print replace_labels
	for item in replace_labels:
		print item,replace_labels[item]

	return final_net

if __name__ == "__main__":
	filename = "test.txt"
	fd = open(filename)
	read = fd.read()
	inp = ast.literal_eval(read)

	data_out = main(inp)
	fd2 = open("out_test.txt","w")
	fd2.write(data_out)
