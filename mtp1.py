# Importing libraries
import math
from math import *         #for eval() functio
import re
from tkinter import *
from dialogs import *
from tkinter import simpledialog
from tkinter import messagebox

# to use hashmap
from collections import defaultdict

# for integer max value 
import sys
# from numbers import Integral, Real
# from extended_int import int_inf, ExtendedIntegral, Infinite


# import networkx
# import pydot
#from pydot import Dot, Edge, Node

# from dfa import DFA
#impoert other files
import automata

#import input
# m=sys.maxsize
# print(sys.maxsize)
# print(m)

#from PIL import Image
#creating tkinter window
window=Tk()


# Title
window.title("Timed Automata")
#window['bg'] = 'blue'
# Geometry          (width * height)
# root.geometry("800 * 700 ")                # error correct it

# Window minimum Dimention
window.minsize(733,434)
# Window maximum Dimention
window.maxsize(1600,1200)



alphabet_list=[]
state_list=[]
initial_state_list=[]
final_state_list=[]
clock_list=[]


transition_dict={}

transition=[]

# Add photo
#photo=PhotoImage(file="heart.png")
#hayat_label=Label(image=photo)
#hayat_label.pack()
def show_diagram(self, path=None):  # pragma: no cover
        """
            Creates the graph associated with this DFA
        """
        # Nodes are set of states

 

        graph = Dot(graph_type='digraph', rankdir='LR')
        nodes = {}
        for state in self.states:
            if state == self.initial_state:
                # color start state with green
                if state in self.final_states:
                    initial_state_node = Node(
                        state,
                        style='filled',
                        peripheries=2,
                        fillcolor='#66cc33')
                else:
                    initial_state_node = Node(
                        state, style='filled', fillcolor='#66cc33')
                nodes[state] = initial_state_node
                graph.add_node(initial_state_node)
            else:
                if state in self.final_states:
                    state_node = Node(state, peripheries=2)
                else:
                    state_node = Node(state)
                nodes[state] = state_node
                graph.add_node(state_node)
        # adding edges
        print(self.transitions.items())    #{0: {0: 'q0', 1: 'a', 2: 'x>8', 3: 'q1', 4: 'x=0'}} etc
        for ss, lookup in self.transitions.items():
            #print(ss)#0
            print(lookup[0])#{0: 'q0', 1: 'a', 2: 'x>8', 3: 'q1', 4: 'x=0'}
            symbolGuard=[lookup[1],lookup[2],lookup[4]]
            graph.add_edge(Edge(
                    nodes[lookup[0]],
                    nodes[lookup[3]],
                    label=str(';'.join(symbolGuard))#'-'.join(sentence)
                ))
            
        if path:
            graph.write_png(path)
        return graph

def getvals():
    TA = automata.DFA(
    alphabet_list,
    state_list,
    initial_state_list,
    final_state_list,
    transition_dict,
    clock_list)
    #TA definition ends
    print("automata")
    print(TA.S)
    print(TA.Q)
    print(TA.q0)
    print(TA.F)
    print(TA.c)
    print(TA.d)

    dfa = DFA(
    states=set(TA.Q),#{​​​​​"q0","q1"}​​​​​,
    input_symbols=set(TA.S),#{​​​​​"a"}​​​​​,
    transitions=set(TA.d),
    
    initial_state=next(iter(set(TA.q0))),#"q0",
    final_states=set(TA.F),#{​​​​​"q0"}​​​​​,
    )
    #a=dfa.show_diagram().render(format='png')
    a='C:\\\\Users\\shubham\\Desktop\\projectmtp\\Timed.png'
    show_diagram(dfa, a)


    """
   
    print(f"The symboles are: {Alphabet.get()}")
    print(f"States are: {States.get()}")
    print(f"Inital State is: {Initial_state.get()}")
    print(f"Final states  are: {Final_state.get()}")


    """







#--------------------------functions--------------------------------



def printAlphabet():
    alphabet_label.config(text=alphabet_list)

def printState():
     state_label.config(text=state_list)

def printInitialState():
    initial_state_label.config(text=initial_state_list)

def printFinalState():
    final_state_label.config(text=final_state_list)


def printClock():
    clock_label.config(text=clock_list)


def addChar():
    char = simpledialog.askstring("Add New Alphabet", "Should be in small letters a-z")
    b=True
    if  char==None:
        return
    
    elif   len(char)==0 :
        b=False
        messagebox.showinfo("Error ", "If you wants to add alphabet, Please Enter again")
    elif len(char)==1 and char.isalpha() and char.islower() :
            for i in range(len(alphabet_list)):
                if char==alphabet_list[i] :
                    b=False
                    messagebox.showinfo("Error ", "2. Alphabet Already added, Please enter again")
                    break   
    else :
        messagebox.showinfo("Error ", "Please Enter an  Alphabet of size 1.")

    if b==True and len(char)==1 and char.isalpha() and char.islower():     
        alphabet_list.append(char)

    printAlphabet()
    

def deleteChar():
    char = simpledialog.askstring("Delete Alphabet", "Should be  added already into the alphabet list")
    
    if char==None  :
        return
    if (len(char)==0):
        messagebox.showinfo("Error ", "Please enter an Alphabet of size 1")
        return
    if len(alphabet_list)==0:
        messagebox.showinfo("Error ", "Alphabet list is empty, first add alphabet")
        return

    b=True
    if len(char)==1 and char.isalpha() and char.islower() :
        for i in range(len(alphabet_list)):
            if char==alphabet_list[i] :
                b=False
                alphabet_list.remove(char)
                break
        if(b==True):
            messagebox.showinfo("Error ", "Alphabet not found, Please Enter again")
    
    else:    
        messagebox.showinfo("Error ", "Alphabet not found, Please Enter again")
    
    printAlphabet()
  
def addState():
    char = simpledialog.askstring("Add New State", "Should be start with q")
    if char==None:
        return 
    if  len(char)<2:
        messagebox.showinfo("Error ", "If you wants to add State, Please Enter again")
        return
    
    if char[0]!='q':
        messagebox.showinfo("Error ", "Please Enter valid state initialise with q")
        return
    b=True
    if  len(char)>=2 and   char.isalnum() :
            for i in range(len(state_list)):
                if char==state_list[i] :
                    b=False
                    messagebox.showinfo("Error ", "2. state Already added, Please enter new state")
                    break    

    if b==True and char.isalnum():     
        state_list.append(char)
    printState()
    
def deleteState():
    char = simpledialog.askstring("Delete State", "Should be already added into the  State list")
    if char==None:
        return
    if  len(state_list)!=0 and len(char)>=2 and char.isalnum() :
        for i in range(len(state_list)):
            if char==state_list[i] :
                state_list.remove(char)
                break
    else :
        messagebox.showinfo("Error ", "Please Enter valid state")

    printState()

def addInitialState():
    char = simpledialog.askstring("Add Initial State", "Should be already added into the  State list and it can have only one state") 
    if char==None:
        return
    
    b=True
    if len(char)<2 or len(initial_state_list)==1 :
        messagebox.showinfo("Error ", "State is not valid or initial state already added, Please Enter again")
        return 
    if char.isalnum() and  len(state_list)>0:
        for i in range(len(state_list)):
                if char==state_list[i] :
                    b=False
                    break
        # if b==True:
        #     messagebox.showinfo("Error ", "Please Enter valid state  ")
    

    if b==False and char.isalnum():     
        initial_state_list.append(char)
    
    else :
        messagebox.showinfo("Error ", "Please Enter valid state  ")
    
    printInitialState()
    


def deleteInitialState():
    char = simpledialog.askstring("Delete Initial State", "Should be already added into the Initial State list")
    
    if char==None:
        return
    b=True
    if len(char)<2 :
        messagebox.showinfo("Error ", "1. If you wants to delete initial State, Please Enter again")
        return

    elif char.isalnum :
        if len(initial_state_list)==1 :
            for i in range(len(initial_state_list)):
                if char==initial_state_list[i] :
                    initial_state_list.remove(char)
                else:
                    messagebox.showinfo("Error ", "Please Enter valid state")

        else :
            messagebox.showinfo("Error ", "You can add initial state ")

    else :
        messagebox.showinfo("Error ", "Please Enter valid state")

    printInitialState()
    

def addFinalState():
    char = simpledialog.askstring("Final State", "Should be already added into the  State list")
    if char==None:
        return
    
    if len(char)<2:
        messagebox.showinfo("Error ", "1. If you wants to add final State, Please Enter valid state")
        return 
    b=True 
    if char[0]=='q' :
        for i in range(len(final_state_list)):
            if char==final_state_list[i] :
                messagebox.showinfo("Error ", "state Already added, Please enter new state")
                return
         
        for i in range(len(state_list)):
            if char==state_list[i] :
                final_state_list.append(char)
                b=False
                break
        if b==True:               
            messagebox.showinfo("Error ", "Please Enter valid state in alphanumeric format")
            return     
    else :
        messagebox.showinfo("Error ", "Please Enter valid state in alphanumeric format")
    printFinalState()
    

def deleteFinalState():
    char = simpledialog.askstring("Delete State", "Should be already added into the Final State list ")
    if char==None:
        return
    b=True
    if len(final_state_list)==0:
        messagebox.showinfo("Error ", "0. No State added yet, First add valid final state")
        return 
    elif char==None or len(char)<2 :
        b=False
        messagebox.showinfo("Error ", "1. If you wants to Delete State, Please Enter again")

    elif char.isalnum():
        for i in range(len(final_state_list)):
            if char==final_state_list[i] :
                b=False
                final_state_list.remove(char)
                break
        
        if b==True:
            messagebox.showinfo("Error ", "Please Enter valid state")

    else :
        messagebox.showinfo("Error ", "Please Enter valid state")

    printFinalState()
    


def addClock():
    char=simpledialog.askstring("Add Clock","Should be Capital letters A-Z")
    if char==None:
        return
    
    if len(char)>1 or len(char)==0:
        b=False
        messagebox.showinfo("Error","Enter valid clock name")
        return 

    b=True
    if char.isalpha() and char.isupper():
        for i in range(len(clock_list)):
            if char==clock_list[i]:
                b=False
                messagebox.showinfo("Error","clock already Addded, Enter valid clock name")

    else:
        messagebox.showinfo("Error", "Enter valid clock name")
    
    if b==True and char.isalpha() and char.isupper():
        clock_list.append(char)

    printClock()
    

def deleteClock():
    char=simpledialog.askstring("Delete Clock","Should be already added into the  Clock List ")
    if char==None:
        return
    
    if  len(char)>1 or len(char)==0 or len(clock_list)==0:
        b=False
        messagebox.showinfo("Error","Enter valid clock name")
        return

    b=True
    if char.isalpha():
        for i in range(len(clock_list)):
            if char==clock_list[i]:
                clock_list.remove(char)
                b=False
                break
        if b==True:
            messagebox.showinfo("Error", "Enter valid clock name")

    else:
        messagebox.showinfo("Error", "Enter valid clock name")

    printClock()
    

def addTransition():
    count=0
    transitions_dict_temp={}
    b=True

    From_state=From_state_entry.get()
    if From_state==None:
        messagebox.showinfo("Error", "Transitions is not valid due to invalid From State, please Enter again")
        return
    if From_state!= None and len(From_state)>1 and  From_state[0]=='q' and  From_state.isalnum() :
        for i in range(len(state_list)):
            if From_state==state_list[i] :
                transitions_dict_temp[count]=From_state
                count+=1
                print("from state",From_state)
                b=False
                break
        if b==True:
            messagebox.showinfo("Error", "Transitions is not valid due to invalid From State, please Enter again")
            return
    else:
        messagebox.showinfo("Error", "Transitions is not valid due to invalid From State, please Enter again")
        return
        #messagebox.showinfo("Error", "Enter valid state")

    
    input_symbol=Input_alphabet_entry.get()
    if input_symbol==None:
        messagebox.showinfo("Error", "Transitions are not valid due to invalid input alphabet, please Enter again")
        return
    if input_symbol!=None and len(input_symbol)==1 and input_symbol.isalpha() :
        for i in range(len(alphabet_list)):
            if input_symbol==alphabet_list[i] :
                transitions_dict_temp[count]=input_symbol
                print("input",input_symbol)
                count+=1
                break
    else:
        messagebox.showinfo("Error", "Transitions are not valid due to invalid input alphabet, please Enter again")
        return
        

    
    guard=Guard_entry.get()
    if len(guard)==0 :
        transitions_dict_temp[count]=guard
        count+=1
    elif guard!=None and len(guard)>=0  :
            guard_temp=guard.split(',')
            count_guard=0
            for i in range(len(guard_temp)) :
                char=guard_temp[i]
                for  j in range(len(clock_list) ):
                    if char[0]==clock_list[j] :
                        count_guard+=1
                        print("guard clock ",i ," ")
                        break

                    
            if count_guard==len(guard_temp) :
                transitions_dict_temp[count]=guard
                count+=1

            else :
                messagebox.showinfo("Error", "Transitions are not valid due to invalid guard, please Enter again")
                return
                #messagebox.showinfo("Error", "Enter valid clock guard")
    else:
        messagebox.showinfo("Error", "Transitions are not valid due to invalid guard, please Enter again")
        return

    
    To_state=To_state_entry.get()
    if To_state==None:
        messagebox.showinfo("Error", "Transitions is not valid due to invalid To State, please Enter again")
        return
    if To_state!= None and  len(To_state)>1 and To_state[0]=='q'  and To_state.isalnum() :
        for i in range(len(state_list)):
            if To_state==state_list[i] :
                transitions_dict_temp[count]=To_state
                count+=1
                print("to state",To_state)
                b=False
                break
        if b==True:
            messagebox.showinfo("Error", "Transitions is not valid due to invalid To State, please Enter again")
            return
    else:
        messagebox.showinfo("Error", "Transitions is not valid due to invalid To State, please Enter again")
        return
        #messagebox.showinfo("Error", "Enter valid state")
    
    reset=Reset_entry.get()
    if len(reset)==0:
        transitions_dict_temp[count]=reset
        count+=1
    elif reset !=None and len(reset)>=0 :
            reset_temp=reset.split(',')
            b=True
            count_reset=0
            for i in range(len(reset_temp)) :
                char=reset_temp[i]
                for  j in range(len(clock_list) ):
                    if char[0]==clock_list[j] :            
                        count_reset+=1
                        print("reset clock ",i ," ")
                        break
            if count_reset==len(reset_temp) :
                transitions_dict_temp[count]=reset
                count+=1
                
            else :
                messagebox.showinfo("Error", "Transitions are not valid due to Reset, please Enter again")
                return
              
    else :
        messagebox.showinfo("Error", "Transitions are not valid due to Reset, please Enter again")
        return

    if  count==5 :
        #print(transitions_dict_temp)
        p=len(transition_dict)
        transition_dict[p] = transitions_dict_temp
        print(transition_dict) 
        resetText()
    


    
def resetText():
        To_state_entry.delete(0, 'end')
        Input_alphabet_entry.delete(0, 'end')
        Guard_entry.delete(0, 'end')
        From_state_entry.delete(0, 'end')
        Reset_entry.delete(0, 'end')




#----------------------------Completeness---------------------------------------
# class tp:
#     def __repr__(self):
#         return "(%d,%d)" % (self.start, self.end)

#     def __init__(self, start, end):
#         self.start = start
#         self.end = end

class tp():
    def __repr__(self):
        return '(%.2f,%.2f)' % (self.start, self.end)
    def __init__(self,start,end): 
        self.start=start
        self.end=end
        

# posi=math.inf
# negi=math.inf        
# s=[tp(0,1),tp(0,3),tp(11,posi)]
# s.append(tp(4,10))
# s.sort(key=lambda self: self.start)
# print(s)
# y=[ s[0] ]
# for x in s[1:]:
#     if y[-1].end < x.start:
#         y.append(x)
#     elif y[-1].end == x.start:
#         y[-1].end = x.end
#     if x.end > y[-1].end:
#         y[-1].end = x.end
# print(y)
# print(len(y))

def checkCompleteness():
    max_int=sys.maxsize
    count_state_list=[False]*len(state_list)    
    for i in range(len(state_list)):    
        count_alphabet_list=[False]*len(alphabet_list)
        for j in range(len(alphabet_list)):
            guard_hashmap=defaultdict(list)
            check_transition_for_alphabet=False
            for k in range(len(transition_dict)):
                transition=transition_dict[k]
                
                if transition[0]==state_list[i] and transition[1]==alphabet_list[j] :
                    check_transition_for_alphabet=True 
                    if transition[2]==None or len(transition[2])==0:
                        count_alphabet_list[j]=True
                    else:    
                        temp_guard=re.split(',',transition[2])
                        for t in range(len(temp_guard)):
                            single_guard=temp_guard[t]
                            if  single_guard!=None and len(single_guard)>=8 and 'or' in single_guard:
                                G1=re.split(' ',single_guard)
                                print("this is or:",G1)
                                for p in G1:
                                    if(p=='or'):
                                        continue
                                    else:
                                        guard_hashmap[p[0]].append(p)
                            elif  single_guard!=None and len(single_guard)>=8 and 'and' in single_guard:
                                guard_hashmap[single_guard[0]].append(single_guard)

                            else:
                                guard_hashmap[single_guard[0]].append(single_guard)    
            
            for key in guard_hashmap:
                interval_list=[]
                for guard in guard_hashmap[key]:
                    if len(guard)>9 and 'and' in guard:
                        G1=re.split(' ',guard)
                        print("This is and :",G1)
                        t=True
                        m=-1
                        n=-1
                        for x in G1:
                            if(x=='and'):
                                continue
                            if(t==False):
                                if x[1]=='<' and x[2]=='=' :
                                    n=float(x[3:])    
                            
                                elif x[1]=='<':
                                    n=float(x[2:])-0.1
                                
                                t=True

                            elif(t==True):
                                if x[1]=='>' and x[2]=='=' :
                                    m=float(x[3:])    
                            
                                elif x[1]=='>':
                                    m=float(x[2:])+0.1

                                t=False

                        interval_list.append(tp(m,n))
                                
                    
    
                    elif guard[1]=='<' and guard[2]=='=':
                        interval_list.append(tp(0,float(guard[3:])))
                    
                    elif guard[1]=='>' and guard[2]=='=':
                        interval_list.append(tp(float(guard[3:]),float('inf')))

                    elif guard[1]=='<' :
                        interval_list.append(tp(0,float(guard[2:])-0.1))

                    elif guard[1]=='>' :
                        interval_list.append(tp(float(guard[2:])+0.1,float('inf')))
   
                    elif guard[1]=='!' and guard[2]=='=':
                        interval_list.append(tp(0,float(guard[3:]-0.1)))
                        interval_list.append(tp(float(guard[3:])+0.1,float('inf')))
                    elif guard[1]=='=':
                        interval_list.append(tp(float(guard[3:]),float(guard[3:])))
 


                print("\nthis is intervsls")
                print(interval_list)

                interval_list.sort(key=lambda self: self.start)

                print("After sorted intervsls")
                print(interval_list)

                y=[ interval_list[0] ]
                for x in interval_list[1:]:
                    if y[-1].end == x.start:
                        y[-1].end = x.end
                    elif   y[-1].end+0.1>=x.start:
                        y[-1].end = x.end
                    elif y[-1].end < x.start :
                        y.append(x)


                    #-------
    #                   if y[-1].end < x.start:
    #     y.append(x)
    # elif y[-1].end == x.start:
    #     y[-1].end = x.end
    # if x.end > y[-1].end:
    #     y[-1].end = x.end


                print("after union",interval_list)
                print(y)

                temp=y[0]
                # print(y)
                # print("thihs is x")
                # print(x.start)
                # print(x.end)
                if(temp.start!=0 or temp.end!=float('inf')):
                    messagebox.showinfo("Completeness", "NO, It does not follow completeness")
                    return 
            if check_transition_for_alphabet==True:
                count_alphabet_list[j]=True
            
        if False in count_alphabet_list:   
            messagebox.showinfo("Completeness", "NO, It does not follow completeness")
            return

        count_state_list[i]=True
        
    if False in count_state_list:   
        messagebox.showinfo("Completeness", "NO, It does not follow completeness")
        return

    messagebox.showinfo("Completeness", "Yes, It follow completeness")





#--------------------------------------------------------------------------

def check_disjuntion_of_guard(g1,g2):
    if(g1[0]!=g2[0]):
        return False

    g="("+g1+") and ("+g2+")"
    k='A'
    for i in range(26):
      g=g.replace(k,'x')
      k=chr(ord(k)+1)
    r=re.split(' ' '|>=|<=|>|<|==|!=|and|or|x', g)
    res=[]
    for s in r:
        if(s.isnumeric()):
            res.append(int(s))
    print("this is res",res)
    for x in res:
        if(eval(g)):
             return True
        x=x-1
        if(eval(g)):
             return True
        x=x+2
        if(eval(g)):
             return True
    return False


def check_disjuntion_of_guard_multiple_clock(guard1,guard2):
    if guard1==None and guard1==guard2:
        return True
    elif len(guard1)==0 and len(guard2)==0:
        return True
    
    elif len(guard1)==0 or len(guard2)==0:
        return False
    elif guard1==None or guard2==None:
        return False    
    G1=re.split(',', guard1)
    G2=re.split(',', guard2)
    ans=False
    for a in G1:
      for b in G2:
        ans |= check_disjuntion_of_guard(a,b)
        if(ans==True):
            return ans
    return ans 

def checkDeteminism():
    dicti={}
    dictj={}
    for i in range(len(transition_dict)):
        dicti=transition_dict[i]
        for j in range(i+1,len(transition_dict)):
            dictj=transition_dict[j]
            # print("this is determinism")
            # print(dicti[2])
            # print(dictj[2])
            if(dicti[0]==dictj[0] and dicti[1]==dictj[1] and check_disjuntion_of_guard_multiple_clock(dicti[2],dictj[2])):
                messagebox.showinfo("Deterministic vs Non-Deterministic", " It is Non-Deterministic")
                return

    messagebox.showinfo("Deterministic vs Non-Deterministic", "Yes, It is Deterministic")    



#----------------------Define label-------------------------------
l1=Label(window, text="Alphabets: Σ : ")
l1.grid(row=0,column=0)

l2=Label(window, text="States S :")
l2.grid(row=1,column=0)

l3=Label(window, text="initial  state:  ")
l3.grid(row=2,column=0)

l4=Label(window, text="final states: ")
l4.grid(row=3,column=0)

l5=Label(window, text="clocks : ")
l5.grid(row=4,column=0)



l6=Label(window, text="Insert transition:")
l6.grid(row=7,column=0)

l7=Label(window, text="From State")
l7.grid(row=7,column=2)


l8=Label(window, text="Input")
l8.grid(row=7,column=3)


l9=Label(window, text="Guard")
l9.grid(row=7,column=4)

l10=Label(window, text="To state")
l10.grid(row=7,column=5)

l11=Label(window, text="Reset")
l11.grid(row=7,column=6)

####################Currenly working

l12=Label(window, text="Start with q and Should be state")
l12.grid(row=9,column=2)


l13=Label(window, text="Should be  an alphabet list")
l13.grid(row=9,column=3)


l14=Label(window, text="Guard should Capital alphabet \n Should be start with Clocks\n Format for same clock: \n(2>=X<=10)as(X>=2 and X<=10)\n for or condition: (X<10 or X>20)\n Format for different clocks Use (,) as:\n as X<=10,Y<=2,Z>30  ")
l14.grid(row=9,column=4)

l15=Label(window, text="Should be an state")
l15.grid(row=9,column=5)

l16=Label(window, text="Reset should be same as guard")
l16.grid(row=9,column=6)

#--------------------------Label for output-------------------------------------
alphabet_label=Label(window,text={})
alphabet_label.grid(row=0,column=1)

state_label=Label(window,text={})
state_label.grid(row=1,column=1)

initial_state_label=Label(window,text={})
initial_state_label.grid(row=2,column=1)

final_state_label=Label(window,text={})
final_state_label.grid(row=3,column=1)

clock_label=Label(window,text={})
clock_label.grid(row=4,column=1)



#-------------------------------BUTTON---------------------
Button(text="Add Alphabet",command=addChar).grid(row=0,column=9)
Button(text="Delete Alphabet",command=deleteChar).grid(row=0,column=11)

Button(text="Add State",command=addState).grid(row=1,column=9)
Button(text="Delete State",command=deleteState).grid(row=1,column=11)

Button(text="Set Initial State",command=addInitialState).grid(row=2,column=9)
Button(text="Delete Initial State",command=deleteInitialState).grid(row=2,column=11)

Button(text="Add Final State",command=addFinalState).grid(row=3,column=9)
Button(text="Delete Final State",command=deleteFinalState).grid(row=3,column=11)

Button(text="Add Clock",command=addClock).grid(row=4,column=9)
Button(text="Delete Clock",command=deleteClock).grid(row=4,column=11)


Button(text="Ok",command=addTransition,fg="blue",bg="yellow").grid(row=8,column=8)
Button(text="Reset",command=resetText,fg="red",bg="yellow").grid(row=8,column=9)



Button(text="Draw Timed Automata",command=getvals,fg="green",bg="yellow").grid(row=15,column=3)

Button(text="CheckCompleteness",command=checkCompleteness,fg="black",bg="yellow").grid(row=15,column=5)

Button(text="CheckDeterminism",command=checkDeteminism,fg="black",bg="yellow").grid(row=15,column=7)

#----------------------Define Entries------------------------------------

From_state=StringVar()
From_state_entry=Entry(window, textvariable=From_state)
From_state_entry.grid(row=8,column=2)

Input_alphabet=StringVar()
Input_alphabet_entry=Entry(window, textvariable=Input_alphabet)
Input_alphabet_entry.grid(row=8,column=3)

Guard=StringVar()
Guard_entry=Entry(window, textvariable=Guard)
Guard_entry.grid(row=8,column=4)

To_state=StringVar()
To_state_entry=Entry(window, textvariable=To_state)
To_state_entry.grid(row=8,column=5)



Reset=StringVar()
Reset_entry=Entry(window, textvariable=Reset)
Reset_entry.grid(row=8,column=6)


window.mainloop()