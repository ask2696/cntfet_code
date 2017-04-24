import numpy as np
from Template_Decision import decision_template
from Mappings import node

def mux_translate(stage_num,left_branch,path,select_line,_I0,_I2):
    if left_branch == "0":
        ans = "NTI"
    elif left_branch == "2":
        ans = "PTI"
    line = "XMUX_Stage"+stage_num+"_"+"path" + _I0 +" "+ _I2+" "+ select_line +" "+ans
    return line
def netlist_gen(inp):
    
    print "                         ",out.select_line,"               "
    print "                ",out.left_branch,"    ",out.right_branch,"       "
    if(str(type(out.left_value)) == "<type 'instance'>"):
        print "      ",out.left_value.select_line,"    "
        print "   ",out.left_value.left_branch,"     ",out.left_value.right_branch
        if str(type(out.left_value.right_value)) == "<type 'instance'>":
            print "  ",out.left_value.left_value," ",out.left_value.right_value.select_line
            print "                  ",out.left_value.right_value.left_branch,"    ",out.left_value.right_value.right_branch
            print "                               ",out.left_value.right_value.left_value,"     ",out.left_value.right_value.right_value
        else:
            print "",out.left_value.left_value,"          ",out.left_value.right_value
    else:
        print "  ",out.left_value

    #print out.right_value

    if(str(type(out.right_value)) == "<type 'instance'>"):
        print "                                 ",out.right_value.select_line,"    "
        print "                        ",out.right_value.left_branch,"     ",out.right_value.right_branch

        if(str(type(out.right_value.left_value)) == "<type 'instance'>"):
            print "            ",out.right_value.left_value.select_line,"                                          "
            print "          ",out.right_value.left_value.left_branch,"    ",out.right_value.left_value.right_branch
            print "        ",out.right_value.left_value.left_value,"             ",out.right_value.left_value.right_value
            
        else:
            print "       ",out.right_value.left_value
            
        if str(type(out.right_value.right_value)) == "<type 'instance'>":
            print "                                                           ",out.right_value.right_value.select_line
            print "                                                  ",out.right_value.right_value.left_branch,"    ",out.right_value.right_value.right_branch
            print "                                                ",out.right_value.right_value.left_value,"     ",out.right_value.right_value.right_value
        else:
            print "                                              ",out.right_value.right_value
            
        
    else:
        print "                                    ",out.right_value
    
    lines = []
    inputs_netlist = []
    end = {"0":"PTI","2":"NTI"}
    _var = {"0":"2","2":"0"}
    line1,liner2,linerl2,linerr3,linerl3,line2,line3 ="","","","","","",""
    linerll4 =""
    if (str(type(inp)) == "<type 'instance'>"): #Stage 1
        
        if(inp.left_branch == (0)):
            NTI_PTI_1 = "NTI"
            var1 = "2"
        elif (inp.left_branch == (2)):
            NTI_PTI_1 = "PTI"
            var1 = "0"
        
        line1 =  "XMUX_Stage1_OUT "
        
        #print type(inp.left_value)
        if(str(type(inp.left_value)) == "<type 'int'>"):
            if(NTI_PTI_1 == "NTI"):
                _2I21 = "Cons_Stage2_I2"
            elif(NTI_PTI_1 == "PTI"):
                _2I01 = "Cons_Stage2_I0"
        elif(str(type(inp.left_value)) == "<type 'instance'>"):

            # Further Down instances and then build upto constants and strings 
            if(NTI_PTI_1 == "NTI"):
                _2I21 = "2I21"
                #line2 = mux_translate("2",inp.left_value.left_branch,"I2",inp.left_value.select_line,
                                      
            elif(NTI_PTI_1 == "PTI"):
                _2I01 = "2I01"
            #Line1 Stage1 taken care above
            if(inp.left_value.left_branch == 0):
                varl2 = "2"
            elif(inp.left_value.left_branch == 2):
                varl2 = "0"
            
            if(str(type(inp.left_value.left_value)) == "<type 'instance'>"):
                if(inp.left_value.left_value.left_branch == 0):
                    varl3 = "2"
                elif(inp.left_value.left_value.left_branch == 2):
                    varl3 = "0"
                    
                _4I03 = "Cons_Stage4_I0"+"_I"+_var[varl2]+"_I"+var1
                _4I23 = "Cons_Stage4_I2"+"_I"+_var[varl2]+"_I"+var1
                line3 = "XMUX_Stage3_I"+_var[varl2]+"_I"+var1+" "+_4I03+" "+_4I23+" "+"3I"+_var[varl2]+"2 "+inp.left_value.left_value.select_line+" Mux_"+end[varl3]
                print "#"
                #inp.left_value.right_value has to be a const or string
                if(str(type(inp.left_value.right_value)) == "<type 'int'>"):
                    if(inp.left_value.left_branch == 0):
                        _3I02 = "Cons_Stage3_I0_I2"
                        _3I22 = "3I22"
                        line2 = "XMUX_Stage2_I"+var1+" "+_3I02+" "+ _3I22+" " + inp.left_value.select_line+" Mux_"+"NTI"        
                            
                    elif(inp.left_value.left_branch == 2):
                        _3I22 = "Cons_Stage3_I2_I2" 
                        _3I02 = "3I02"
                        line2 = "XMUX_Stage2_I"+var1+" "+_3I02+" "+ _3I22+" " + inp.left_value.select_line+" Mux_"+"PTI"
                
                    
                    
                    
                    
            elif(str(type(inp.left_value.right_value)) == "<type 'instance'>"):
                if(inp.left_value.right_value.left_branch == 0):
                    varl3 = "2"
                elif(inp.left_value.right_value.left_branch == 2):
                    varl3 = "0"
                
                print "$"
                _4I03 = "Cons_Stage4_I0"+"_I"+_var[varl2]+"_I"+var1
                _4I23 = "Cons_Stage4_I2"+"_I"+_var[varl2]+"_I"+var1
                line3 = "XMUX_Stage3_I"+_var[varl2]+"_I"+var1+" "+_4I03+" "+_4I23+" "+"3I"+_var[varl2]+"2 "+inp.left_value.right_value.select_line+" Mux_"+end[varl3]
                #inp.left_value.left_value has to be a const or string
                if(str(type(inp.left_value.left_value)) == "<type 'int'>"):
                    if(inp.left_value.left_branch == 0):
                        _3I22 = "Cons_Stage3_I2_I2"
                        _3I02 = "3I02"
                        line2 = "XMUX_Stage2_I"+var1+" "+_3I02+" "+ _3I22+" "+ "2I21" + " " + inp.left_value.select_line+" Mux_"+"NTI"        
                            
                    elif(inp.left_value.left_branch == 2):
                        _3I22 = "3I22" 
                        _3I02 = "Cons_Stage3_I0_I2"
                        line2 = "XMUX_Stage2_I"+var1+" "+_3I02+" "+ _3I22+" " + "2I21" + " " + inp.left_value.select_line+" Mux_"+"PTI"

            #else:
                #Both Integers Case or String need to differentiate
                
                    
                    
                
                
            #line2 = mux_translate("2",inp.left_value.left_branch,"")

            if(str(type(inp.left_value.left_value)) == "<type 'int'>"):
                              
                if(NTI_PTI_1 == "NTI"):
                    _3I22 = "Cons_Stage2_I2"
                    
                elif(NTI_PTI_1 == "PTI"):
                    _3I02 = "Cons_Stage2_I0"
            
            
        elif(str(type(inp.left_value)) == "<type 'str'>"):
            print"#"

        else:
            print "To be Defined"
            
        #print type(inp.right_value)
        if(str(type(inp.right_value)) == "<type 'int'>"):
            if(NTI_PTI_1 == "NTI"):
                _2I01 = "Cons_Stage2_I0"
            elif(NTI_PTI_1 == "PTI"):
                _2I21 = "Cons_Stage2_I2"
        elif(str(type(inp.right_value)) == "<type 'instance'>"):
            if(NTI_PTI_1 == "NTI"):
                _2I01 = "2I01"
            elif(NTI_PTI_1 == "PTI"):
                _2I21 = "2I21"
            #Line1 Stage1 taken care above
            if(inp.right_value.left_branch == 0):
                varr2 = "2"
            elif(inp.right_value.left_branch == 2):
                varr2 = "0"
            
            if(str(type(inp.right_value.left_value)) == "<type 'instance'>"):
                if(inp.right_value.left_value.left_branch == 0):
                    varrl3 = "2"
                elif(inp.right_value.left_value.left_branch == 2):
                    varrl3 = "0"
                    
                #Stage 3
                print "#"
                #!!!!!!inp.left_value.right_value has to be a const or string
                if(str(type(inp.right_value.right_value)) == "<type 'int'>"):
                    if(inp.right_value.left_branch == 0):
                        _3I02 = "Cons_Stage3_I0_I2"
                        _3I22 = "3I22"
                        liner2 = "XMUX_Stage2_I"+_var[var1]+" "+_3I02+" "+ _3I22+" " + inp.right_value.select_line+" Mux_"+"NTI"        
                            
                    elif(inp.right_value.left_branch == 2):
                        _3I22 = "Cons_Stage3_I2_I2" 
                        _3I02 = "3I02"
                        liner2 = "XMUX_Stage2_I"+_var[var1]+" "+_3I02+" "+ _3I22+" " + inp.right_value.select_line+" Mux_"+"PTI"
                
                #elif(str(type(inp.right_value.right_value)) == "<type 'instance'>"):   
                #Repliicate the above for lower cases


                if(str(type(inp.right_value.left_value.right_value)) == "<type 'instance'>"):
                    
                    #left.value has to be a int  or string
                    if(varrl3 == "2"):
                        _4I03 = "4I03"
                        _4I23 = "Cons_Stage4_I2"+"_I"+varr2+"_I"+_var[var1]
                    elif(varrl3 == "0"):
                        _4I23 = "4I23"
                        _4I03 = "Cons_Stage4_I0"+"_I"+varr2+"_I"+_var[var1]
                    linerl3 = "XMUX_Stage3_I"+varr2+"_I"+_var[var1]+" "+_4I03+" "+_4I23+" "+"3I"+varr2+"2 "+inp.right_value.left_value.select_line+" Mux_"+end[varrl3]
                    print "$$$$$"
                    if(str(type(inp.right_value.left_value.left_value)) == "<type 'int'>"):
                        #Stage 5 Contants to Stage 4 Mux
                        if(inp.right_value.right_value.right_value.left_branch == 0):
                            varrlr4= "2"
                        elif (inp.right_value.right_value.right_value.left_branch == 2):
                            varrlr4= "0"

                        ###########################################################################################
                        #Start Here.... Verify this Case and replicate for inp.right.left cases above
                        #Look for similarity 
                        _5I04 = "Cons_Stage5_I0"+"_I"+_var[varrl3]+"_I"+varr2+"_I"+_var[var1] #No negation in stage 2
                        _5I24 = "Cons_Stage5_I2"+"_I"+_var[varrl3]+"_I"+varr2+"_I"+_var[var1]
                        linerlr4 = "XMUX_Stage4_I"+_var[varrl3]+"_I"+varr2+"_I"+_var[var1]+" "+_5I04+" "+_5I24+" "+"4I"+_var[varrl3]+"3 "+inp.right_value.left_value.select_line+" Mux_"+end[varrlr4]
                        """
                        if(inp.right_value.left_value.left_branch == 0):
                            _3I22 = "Cons_Stage4_I2_I2_I0"
                            _3I02 = "3I02"
                            linerr3 = "XMUX_Stage3_I"+_var[varr2]+"_I"+_var[var1]+" "+_3I02+" "+ _3I22+" "+ "2I21" + " " + inp.right_value.left_value.select_line+" Mux_"+"NTI"        
                                
                        elif(inp.right_value.left_value.left_branch == 2):
                            _3I22 = "3I22" 
                            _3I02 = "Cons_Stage4_I0_I2_I0"
                            linerr3 = "XMUX_Stage3_I"+_var[varr2]+"_I"+_var[var1]+" "+_3I02+" "+ _3I22+" "+ "2I01" + " " + inp.right_value.left_value.select_line+" Mux_"+"PTI"
                        """
                elif(str(type(inp.right_value.left_value.left_value)) == "<type 'instance'>"):
                    #right.value has to be a int  or string

                    if(varrl3 == "2"):
                        _4I03 = "4I03"
                        _4I23 = "Cons_Stage4_I2"+"_I"+varr2+"_I"+_var[var1]
                    elif(varrl3 == "0"):
                        _4I23 = "4I23"
                        _4I03 = "Cons_Stage4_I0"+"_I"+varr2+"_I"+_var[var1]
                    linerl3 = "XMUX_Stage3_I"+varr2+"_I"+_var[var1]+" "+_4I03+" "+_4I23+" "+"3I"+varr2+"2 "+inp.right_value.left_value.select_line+" Mux_"+end[varrl3]
                    
                    if(str(type(inp.right_value.left_value.left_value)) == "<type 'int'>"):
                        #Stage 5 Contants to Stage 4 Mux
                        if(inp.right_value.right_value.right_value.left_branch == 0):
                            varrll4= "2"
                        elif (inp.right_value.right_value.right_value.left_branch == 2):
                            varrll4= "0"

                        _5I04 = "Cons_Stage5_I0"+"_I"+_var[varrl3]+"_I"+varr2+"_I"+_var[var1] #No negation in stage 2
                        _5I24 = "Cons_Stage5_I2"+"_I"+_var[varrl3]+"_I"+varr2+"_I"+_var[var1]
                        linerll4 = "XMUX_Stage4_I"+_var[varrl3]+"_I"+varr2+"_I"+_var[var1]+" "+_5I04+" "+_5I24+" "+"4I"+_var[varrl3]+"3 "+inp.right_value.left_value.select_line+" Mux_"+end[varrll4]
                    
                #Repliicate the above for lower cases
                else:
                    print "%%%%%"
                    #Two constants case
                    _4I03 = "Cons_Stage4_I0"+"_I"+varr2+"_I"+_var[var1]
                    _4I23 = "Cons_Stage4_I2"+"_I"+varr2+"_I"+_var[var1]
                    linerl3 = "XMUX_Stage3_I"+varr2+"_I"+_var[var1]+" "+_4I03+" "+_4I23+" "+"3I"+varr2+"2 "+inp.right_value.left_value.select_line+" Mux_"+end[varrl3]
                    #check neg of varr2
            if(str(type(inp.right_value.right_value)) == "<type 'instance'>"):
                if(inp.right_value.right_value.left_branch == 0):
                    varrr3 = "2"
                elif(inp.right_value.right_value.left_branch == 2):
                    varrr3 = "0"
                
                print "$"
                
                #inp.left_value.left_value has to be a const or string
                if(str(type(inp.right_value.left_value)) == "<type 'int'>"):
                    if(inp.right_value.left_branch == 0):
                        _3I22 = "Cons_Stage3_I2_I"+_var[var1]
                        _3I02 = "3I02"
                        liner2 = "XMUX_Stage2_I"+_var[var1]+" "+_3I02+" "+ _3I22+" "+ "2I21" + " " + inp.right_value.select_line+" Mux_"+"NTI"        
                            
                    elif(inp.right_value.left_branch == 2):
                        _3I22 = "3I22" 
                        _3I02 = "Cons_Stage3_I0_I"+_var[var1]
                        liner2 = "XMUX_Stage2_I"+_var[var1]+" "+_3I02+" "+ _3I22+" " + "2I01" + " " + inp.right_value.select_line+" Mux_"+"PTI"

                """
                    if(str(type(inp.left_value.right_value)) == "<type 'instance'>"):
                if(inp.left_value.right_value.left_branch == 0):
                    varl3 = "2"
                elif(inp.left_value.right_value.left_branch == 2):
                    varl3 = "0"
                
                print "$"
                _4I03 = "Cons_Stage4_I0"+"_I"+_var[varl2]+"_I"+var1
                _4I23 = "Cons_Stage4_I2"+"_I"+_var[varl2]+"_I"+var1
                line3 = "XMUX_Stage3_I"+_var[varl2]+"_I"+var1+" "+_4I03+" "+_4I23+" "+"3I"+_var[varl2]+"2 "+inp.left_value.right_value.select_line+" Mux_"+end[varl3]
                #inp.left_value.left_value has to be a const or string
                """
                #Going Lower, for the row distribution case
                if(str(type(inp.right_value.right_value.right_value)) == "<type 'instance'>"):

                    #Stage 3
                    #left.value has to be a int  or string
                    if(varrr3 == "2"):
                        _4I03 = "4I03"
                        _4I23 = "Cons_Stage4_I2"+"_I"+_var[varr2]+"_I"+_var[var1]
                    elif(varrr3 == "0"):
                        _4I23 = "4I23"
                        _4I03 = "Cons_Stage4_I0"+"_I"+_var[varr2]+"_I"+_var[var1]
                    linerr3 = "XMUX_Stage3_I"+_var[varr2]+"_I"+_var[var1]+" "+_4I03+" "+_4I23+" "+"3I"+_var[varr2]+"2 "+inp.right_value.right_value.select_line+" Mux_"+end[varrr3]

                    #Stage 4
                    
                    if(str(type(inp.right_value.right_value.left_value)) == "<type 'int'>"):
                        #Stage 5 Contants to Stage 4 Mux
                        if(inp.right_value.right_value.right_value.left_branch == 0):
                            varrrr4= "2"
                        elif (inp.right_value.right_value.right_value.left_branch == 2):
                            varrrr4= "0"
                            
                        _5I04 = "Cons_Stage5_I0"+"_I"+_var[varrr3]+"_I"+_var[varr2]+"_I"+_var[var1]
                        _5I24 = "Cons_Stage5_I2"+"_I"+_var[varrr3]+"_I"+_var[varr2]+"_I"+_var[var1]
                        linerrr4 = "XMUX_Stage4_I"+_var[varrr3]+"_I"+_var[varr2]+"_I"+_var[var1]+" "+_5I04+" "+_5I24+" "+"4I"+_var[varrr3]+"3 "+inp.right_value.right_value.select_line+" Mux_"+end[varrrr4]
                        """
                        if(inp.right_value.right_value.left_branch == 0):
                            _3I22 = "Cons_Stage4_I2_I2_I0"
                            _3I02 = "3I02"
                            linerr3 = "XMUX_Stage3_I"+_var[varr2]+"_I"+_var[var1]+" "+_3I02+" "+ _3I22+" "+ "2I21" + " " + inp.right_value.right_value.select_line+" Mux_"+"NTI"        
                                
                        elif(inp.right_value.right_value.left_branch == 2):
                            _3I22 = "3I22" 
                            _3I02 = "Cons_Stage4_I0_I2_I0"
                            linerr3 = "XMUX_Stage3_I"+_var[varr2]+"_I"+_var[var1]+" "+_3I02+" "+ _3I22+" "+ "2I01" + " " + inp.right_value.right_value.select_line+" Mux_"+"PTI"
                        """
                #Repliicate the above for lower cases
                elif(str(type(inp.right_value.right_value.left_value)) == "<type 'instance'>"):
                    
                    #Stage 3
                    #right.value has to be a int  or string
                    if(varrr3 == "2"):
                        _4I03 = "4I03"
                        _4I23 = "Cons_Stage4_I2"+"_I"+_var[varr2]+"_I"+_var[var1]
                    elif(varrr3 == "0"):
                        _4I23 = "4I23"
                        _4I03 = "Cons_Stage4_I0"+"_I"+_var[varr2]+"_I"+_var[var1]
                    linerr3 = "XMUX_Stage3_I"+_var[varr2]+"_I"+_var[var1]+" "+_4I03+" "+_4I23+" "+"3I"+_var[varr2]+"2 "+inp.right_value.right_value.select_line+" Mux_"+end[varrr3]

                    #Stage 4
                    
                    if(str(type(inp.right_value.right_value.right_value)) == "<type 'int'>"):
                        #Stage 5 Contants to Stage 4 Mux
                        if(inp.right_value.right_value.right_value.left_branch == 0):
                            varrrr4= "2"
                        elif (inp.right_value.right_value.right_value.left_branch == 2):
                            varrrr4= "0"
                            
                        _5I04 = "Cons_Stage5_I0"+"_I"+_var[varrr3]+"_I"+_var[varr2]+"_I"+_var[var1]
                        _5I24 = "Cons_Stage5_I2"+"_I"+_var[varrr3]+"_I"+_var[varr2]+"_I"+_var[var1]
                        linerrr4 = "XMUX_Stage4_I"+_var[varrr3]+"_I"+_var[varr2]+"_I"+_var[var1]+" "+_5I04+" "+_5I24+" "+"4I"+_var[varr3]+"3 "+inp.right_value.right_value.select_line+" Mux_"+end[varrrr4]

                    
                else:#Two constants case
                    _4I03 = "Cons_Stage4_I0"+"_I"+_var[varr2]+"_I"+_var[var1]
                    _4I23 = "Cons_Stage4_I2"+"_I"+_var[varr2]+"_I"+_var[var1]
                    linerr3 = "XMUX_Stage3_I"+_var[varr2]+"_I"+_var[var1]+" "+_4I03+" "+_4I23+" "+"3I"+_var[varr2]+"2 "+inp.right_value.right_value.select_line+" Mux_"+end[varr3]
            if(str(type(inp.right_value.right_value)) == "<type 'instance'>" and str(type(inp.right_value.left_value)) == "<type 'instance'>"):
                _3I02 ="3I02"
                _3I22 ="3I22"
                print "*"
                liner2 = "XMUX_Stage2_I"+_var[var1]+" "+_3I02+" "+ _3I22+" "+ "2I"+_var[var1]+"1" + " " + inp.right_value.select_line+" Mux_"+end[varr2]
                


                
        elif(str(type(inp.right_value)) == "<type 'str'>"):
            print"#"

        else:
            print "To be Defined"

        S_MUX_Stage1_OUT = inp.select_line
        inputs_netlist = inputs_netlist.append(S_MUX_Stage1_OUT) 
        
        line1 = line1 + _2I01+ " " +_2I21+" " + "Out " +S_MUX_Stage1_OUT + " " + "MUX_" + NTI_PTI_1      
        lines.append(line1)
        lines.append(line2)
        lines.append(line3)
        lines.append(liner2)

        lines.append(linerr3)
        lines.append(linerl3)
                
        lines.append(linerlr4)
        lines.append(linerrr4)
        
            
        








        print ("\n").join(lines)
        














#truth_table = np.array([[1,1,1],[0,2,1],[0,1,2]])
#truth_table = np.array([[0,2,1],[1,1,1],[0,2,1]])
#truth_table = np.array([[0,1,1],[0,1,1],[0,1,1]])
"""
print "Truth Table"
print "   0  1  2"
print "------------"
print "0| %d  %d  %d" %(truth_table[0,0],truth_table[0,1],truth_table[0,2])
print "1| %d  %d  %d" %(truth_table[1,0],truth_table[1,1],truth_table[1,2])
print "2| %d  %d  %d\n" %(truth_table[2,0],truth_table[2,1],truth_table[2,2])
"""

#out,nos = decision_template(truth_table)
#input the new BDD
#out = node("A",(0),(1,2),node("B",(0),(1,2),1,node("B",(2),(0,1),1,0)),node("A",(2),(0,1),node("B",(0),(1,2),0,2),node("B",(0),(1,2),3,4)))
out = node("A",(0),(1,2),node("B",(0),(1,2),1,node("B",(2),(0,1),1,0)),node("A",(2),(0,1),node("B",(0),(1,2),0,node("B",(2),(0,1),1,0)),node("B",(0),(1,2),3,node("B",(2),(0,1),1,0))))
netlist_gen(out)
