from Synthesis_Algorithm_Final_lib import *
import netlist_generation
import re
import os

benchmark_circuits = ["8_3_sum",
					"9_3_sum",
					"10_3_sum",
					"11_3_sum",
					"12_3_sum",
					"13_3_sum",
					"8_6_prod",
					"9_6_prod",
					"10_7_prod",
					"11_7_prod",
					"12_8_prod",
					"13_9_prod",
					"8_1_avg",
					"9_1_avg",
					"10_1_avg",
					"11_1_avg",
					"12_1_avg",
					"13_1_avg"
					]
n_outputs = 0
n_inputs = 0
n_terms = 0

f_type = {"sum":0,"prod":1,"avg":2,"count":3,"cyclic":4}
dir_loc = "./benchmark_circuits/"
for i in range(len(benchmark_circuits)):
	print benchmark_circuits[i]
	args = re.split("_",benchmark_circuits[i])
	n_inputs =  int(args[0])
	n_outputs = int(args[1])
	f_inp = f_type[args[2]]

	print n_inputs,n_outputs,f_inp



	BTDD_Total_Graph,In_Cost2x,Cost,Final_Mux2,Tc = in_args(f_inp,n_outputs,n_inputs,n_terms);

	#print type(BTDD_Total_Graph)

	output_netlist = netlist_generation.main(BTDD_Total_Graph)
	#print output_netlist

	print('No. 2:1 Muxes for other inputs',In_Cost2x)
	print('No. 2:1 Muxes for 2-input Fun.',Cost)
	print('No. of Total 2:1 Muxes',Final_Mux2)
	print('Transistor Count:', Tc)

	file = open(dir_loc+args[2]+"_"+args[0]+"_"+args[1]+".txt","w")
	file.write(str(BTDD_Total_Graph))
	file.close()

	file_w = open(dir_loc+"net_"+args[2]+"_"+args[0]+"_"+args[1]+".txt","w")
	file_w.write(str(output_netlist))
	file_w.close()
