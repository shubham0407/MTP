# Importing only those functions which are needed
from  tkinter import *
from dialogs import *
from tkinter import simpledialog
from tkinter import messagebox


#impoert other files
import automata



#from PIL import Image
#creating tkinter window
window=Tk()


# Title
window.title("Timed Automata")
#window['bg'] = '' #'#ffbf00'
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


# Add photo
#photo=PhotoImage(file="heart.png")
#hayat_label=Label(image=photo)
#hayat_label.pack()


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

"""
    for i in alphabet_list:
        alphabet_entry = alphabet_entry + str(i.get()) + ' '
        alphabet_label.config(text=alphabet_entry)

    
    pname = Alphabet_entry.get()
    Label(ws, text=f'{pname}, Registered!', pady=20, bg='#ffbf00').pack()
"""



def addChar():
    char = simpledialog.askstring("Add New Alphabet", "Enter alphabet")
    print(char)
    b=False
    
    if char==None or len(char)==0 :
        b=True
        messagebox.showinfo("Error ", "1. If you wants to add alphabet, Please Enter again")

    elif len(char)==1 and char.isalpha() :
            for i in range(len(alphabet_list)):
                if char[0]==alphabet_list[i] :
                    b=True
                    if b==True :
                        messagebox.showinfo("Error ", "2. Alphabet Already added, Please enter again")
                        break
        
    else :
        messagebox.showinfo("Error ", "Please Enter an Alphabet of size 1.")

    if b==False and len(char)==1 and char.isalpha():     
        alphabet_list.append(char)
    
    printAlphabet()

    print(alphabet_list)
    #if char:
    #    self.fsm.addChar(char)
    #    self.update()



def deleteChar():
    char = simpledialog.askstring("Delete Alphabet", "Enter alphabet")
    print(char)
    b=False

    if len(alphabet_list)==0:
        messagebox.showinfo("Error ", "0. No Element added yet, First add alphabet ")
    
    elif char==None or len(char)==0 :
        b=True
        messagebox.showinfo("Error ", "1. If you wants to Delete alphabet, Please Enter again")

    elif len(char)==1 and char.isalpha():
        for i in range(len(alphabet_list)):
            if char[0]==alphabet_list[i] :
                b=True
                if b==True :
                    alphabet_list.remove(char)
                    break
    
    elif b==False and char!=None  and len(char)==1 :    
        messagebox.showinfo("Error ", "Alphabet not found, Please Enter again")

    else :
        messagebox.showinfo("Error ", "Please Enter an Alphabet of size 1.")

    
    
    printAlphabet()

    print(alphabet_list)
    #if char:
    #    self.fsm.addChar(char)
    #    self.update()


def addState():
    char = simpledialog.askstring("Add New Statw", "Enter State")
    print(char)
    b=True

    if char==None or len(char)==0 or len(char)==1:
        b=False
        messagebox.showinfo("Error ", "1. If you wants to add State, Please Enter again")

    elif    char.isalnum() :
            for i in range(len(state_list)):
                if char==state_list[i] :
                    b=False
                    if b==False :
                        messagebox.showinfo("Error ", "2. state Already added, Please enter new state")
                        break
        
    else :
        messagebox.showinfo("Error ", "Please Enter valid state in alphanumeric format")

    if b==True and char.isalnum():     
        state_list.append(char)
    
    printState()
    print(state_list)



def deleteState():
    char = simpledialog.askstring("Delete State", "Enter State Name")
    print(char)
    b=True
    #print(char[1])
    if len(state_list)==0 :
        messagebox.showinfo("Error ", "0. No State added yet, First add valid new state")
    
    elif char==None or len(char)<2 :
        b=False
        messagebox.showinfo("Error ", "1. If you wants to Delete State, Please Enter again")

    elif char.isalnum():
        for i in range(len(state_list)):
            if char==state_list[i] :
                b=False
                if b==False :
                    state_list.remove(char)
                    break
    
        if b==True :    
            messagebox.showinfo("Error ", "State not found, Please Enter again")

    else :
        messagebox.showinfo("Error ", "Please Enter an Alphabet of size 1.")

    printState()
    print(state_list)



def addInitialState():
    char = simpledialog.askstring("Add Initail State", "Enter State")
    print(char)
    b=True

    if char==None or len(char)<2 or len(initial_state_list)==1 :
        #b=False
        messagebox.showinfo("Error ", "1. If you wants to add Initial State, Please Enter again")

    elif char.isalnum() and  len(state_list)>0:
        for i in range(len(state_list)):
                if char==state_list[i] :
                    b=False
                    break
        
        if b==True:
            messagebox.showinfo("Error ", "Please Enter valid state  ")
    else :
        #b=False
        messagebox.showinfo("Error ", "Please Enter valid state  ")

    if b==False and char.isalnum():     
        initial_state_list.append(char)
    
    printInitialState()
    print(initial_state_list)


def deleteInitialState():
    char = simpledialog.askstring("Delete Initial State", "Enter State")
    print(char)
    b=True

    if char==None or len(char)<2 :
        #b=False
        messagebox.showinfo("Error ", "1. If you wants to delete initial State, Please Enter again")
    
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
    print(initial_state_list)



    
def addFinalState():
    char = simpledialog.askstring("Final State", "Enter  state")
    print(char)
    b=True

    if char==None or len(char)<2:
        b=False
        messagebox.showinfo("Error ", "1. If you wants to add final State, Please Enter valid state")

    elif    char.isalnum() :
            for i in range(len(final_state_list)):
                if char==final_state_list[i] :
                    b=False
                    if b==False :
                        messagebox.showinfo("Error ", "2. state Already added, Please enter new state")
                        break
    else :
        messagebox.showinfo("Error ", "Please Enter valid state in alphanumeric format")

    if b==True:          
        for i in range(len(state_list)):
            if char==state_list[i] :
                final_state_list.append(char)
                break
    
    printFinalState()
    print(final_state_list)



def deleteFinalState():
    char = simpledialog.askstring("Delete State", "Enter State ")
    print(char)
    b=True
    #print(char[1])
    if len(final_state_list)==0:
        messagebox.showinfo("Error ", "0. No State added yet, First add valid final state")
    
    elif char==None or len(char)<2 :
        b=False
        messagebox.showinfo("Error ", "1. If you wants to Delete State, Please Enter again")

    elif char.isalnum():
        for i in range(len(final_state_list)):
            if char==final_state_list[i] :
                b=False
                if b==False :
                    final_state_list.remove(char)
                    break
        
        if b==True:
            messagebox.showinfo("Error ", "Please Enter valid state")
#    elif b==True and char!=None :    
#        messagebox.showinfo("Error ", "State not found, Please Enter again")

    else :
        messagebox.showinfo("Error ", "Please Enter valid state")

    printFinalState()
    print(final_state_list)


def addClock():
    char=simpledialog.askstring("Add Clock","Enter clock")
    print(char)
    b=True
    if char==None or len(char)>1 or len(char)==0:
        b=False
        messagebox.showinfo("Error","Enter valid clock name")
    
    elif char.isalpha():
        for i in range(len(clock_list)):
            if char==clock_list[i]:
                b=False
                messagebox.showinfo("Error","clock already Addded, Enter valid clock name")

    else:
        messagebox.showinfo("Erroe", "Enter valid clock name")
    
    if b==True and char.isalpha():
        clock_list.append(char)

    printClock()
    print(clock_list)


def deleteClock():
    char=simpledialog.askstring("Delete Clock","Enter clock ")
    print(char)
    b=True
    if char==None or len(char)>1 or len(char)==0 or len(clock_list)==0:
        b=False
        messagebox.showinfo("Error","Enter valid clock name")
    
    elif char.isalpha():
        for i in range(len(clock_list)):
            if char==clock_list[i]:
                b=False
                clock_list.remove(char)
        if b==True:
            messagebox.showinfo("Erroe", "Enter valid clock name")

    else:
        messagebox.showinfo("Erroe", "Enter valid clock name")

    printClock()
    print(clock_list)
"""
def addChar1():
    char = simpledialog.askstring("Add New Alphabet", "Enter alphabet")
    transitions_list.append(char)
"""

def addChar1():
    transitions_dict_temp={}
    char = simpledialog.askstring("Transitions", "Enter Transition")
    char = char.split(';')
    for i in range(len(char)):
        transitions_dict_temp[i]=char[i]
    print(transitions_dict_temp)
    p=len(transition_dict)
    transition_dict[p] = transitions_dict_temp
    print(transition_dict)

# Frame
#= Frame(root, borderwidth=6, bg='grey', relief=SUNKEN)                   # Not working
#frame.pack(side=LEFT, anchor='nw')

#button1= Button(frame, fg="red", text="Print Now", command=hello)
#button1.pack(side=LEFT, padx=23)







#----------------------Define label-------------------------------
l1=Label(window, text="Alphabets: Σ : ")
l1.grid(row=0,column=0)

l1=Label(window, text="States S :")
l1.grid(row=1,column=0)





l1=Label(window, text="initial  state:  ")
l1.grid(row=2,column=0)

l1=Label(window, text="final states: ")
l1.grid(row=3,column=0)





l1=Label(window, text="clocks : ")
l1.grid(row=4,column=0)
"""
l1=Label(window, text="gaurds")
l1.grid(row=5,column=2)

l1=Label(window, text="Reset")
l1.grid(row=5,column=4)



l1=Label(window, text="Grammer")
l1.grid(row=5,column=6)

"""



"""

l1=Label(window, text="From State ")
l1.grid(row=6,column=0)



l1=Label(window, text="To State ")
l1.grid(row=6,column=1)


l1=Label(window, text="input symbol")
l1.grid(row=6,column=2)


"""  




"""
l1=Label(window, text="reset")
l1.grid(row=6,column=3)



l1=Label(window, text="guards")
l1.grid(row=6,column=4)


"""





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

"""
# Check it again
transitions_label=Label(window,text={})
transitions_label.grid(row=7,column=2)
"""


#-------------------------------BUTTON---------------------




# Button for Alphabets Entry
Button(text="Add Alphabet",command=addChar).grid(row=0,column=9)
Button(text="Delete Alphabet",command=deleteChar).grid(row=0,column=11)

Button(text="Add State",command=addState).grid(row=1,column=9)
Button(text="Delete State",command=deleteState).grid(row=1,column=11)

Button(text="Set Initial",command=addInitialState).grid(row=2,column=7)
Button(text="Delete Initial",command=deleteInitialState).grid(row=2,column=9)

Button(text="Add Final",command=addFinalState).grid(row=3,column=7)
Button(text="Delete Final",command=deleteFinalState).grid(row=3,column=9)


Button(text="Add Clock",command=addClock).grid(row=4,column=7)
Button(text="Delete Clock",command=deleteClock).grid(row=4,column=9)
#answer = simpledialog.askstring("Input", "What is your first name?",)

#self.btnAddChar = tk.Button(
  #          self.root, text='Add Symbol', command=self.addChar)



Button(text="Insert Transition",command=addChar1).grid(row=7,column=4)
Button(text="Submit",command=getvals).grid(row=8,column=4)












#----------------------Define Entries------------------------------------
"""
Alphabet=StringVar()
Alphabet_entry=Entry(window, textvariable=Alphabet)
Alphabet_entry.grid(row=0,column=1)


States=StringVar()
States_entry=Entry(window, textvariable=States)
States_entry.grid(row=0,column=3)



Initial_state=StringVar()
Initial_state_entry=Entry(window, textvariable=Initial_state)
Initial_state_entry.grid(row=1,column=1)


Final_state=StringVar()
Final_state_entry=Entry(window, textvariable=Final_state)
Final_state_entry.grid(row=1,column=3)







clocks=StringVar()
e1=Entry(window, textvariable=clocks)
e1.grid(row=3,column=1)

grammer=StringVar()
e1=Entry(window, textvariable=grammer)
e1.grid(row=3,column=3)

reset=StringVar()
e1=Entry(window, textvariable=reset)
e1.grid(row=3,column=5)






gaurds=StringVar()
e1=Entry(window, textvariable=gaurds)
e1.grid(row=5,column=1)





from_state=StringVar()
e1=Entry(window, textvariable=from_state)
e1.grid(row=7,column=0)


to_state=StringVar()
e1=Entry(window, textvariable=to_state)
e1.grid(row=7,column=1)


input_symbol=StringVar()
e1=Entry(window, textvariable=input_symbol)
e1.grid(row=7,column=2)

reset=StringVar()
e1=Entry(window, textvariable=reset)
e1.grid(row=7,column=3)


guards=StringVar()
e1=Entry(window, textvariable=guards)
e1.grid(row=7,column=4)






from_state=StringVar()
e1=Entry(window, textvariable=from_state)
e1.grid(row=8,column=0)


to_state=StringVar()
e1=Entry(window, textvariable=to_state)
e1.grid(row=8,column=1)


input_symbol=StringVar()
e1=Entry(window, textvariable=input_symbol)
e1.grid(row=8,column=2)

reset=StringVar()
e1=Entry(window, textvariable=reset)
e1.grid(row=8,column=3)


guards=StringVar()
e1=Entry(window, textvariable=guards)
e1.grid(row=8,column=4)



from_state=StringVar()
e1=Entry(window, textvariable=from_state)
e1.grid(row=9,column=0)


to_state=StringVar()
e1=Entry(window, textvariable=to_state)
e1.grid(row=9,column=1)


input_symbol=StringVar()
e1=Entry(window, textvariable=input_symbol)
e1.grid(row=9,column=2)

reset=StringVar()
e1=Entry(window, textvariable=reset)
e1.grid(row=9,column=3)


guards=StringVar()
e1=Entry(window, textvariable=guards)
e1.grid(row=9,column=4)



from_state=StringVar()
e1=Entry(window, textvariable=from_state)
e1.grid(row=10,column=0)


to_state=StringVar()
e1=Entry(window, textvariable=to_state)
e1.grid(row=10,column=1)


input_symbol=StringVar()
e1=Entry(window, textvariable=input_symbol)
e1.grid(row=10,column=2)

reset=StringVar()
e1=Entry(window, textvariable=reset)
e1.grid(row=10,column=3)


guards=StringVar()
e1=Entry(window, textvariable=guards)
e1.grid(row=10,column=4)


from_state=StringVar()
e1=Entry(window, textvariable=from_state)
e1.grid(row=11,column=0)


to_state=StringVar()
e1=Entry(window, textvariable=to_state)
e1.grid(row=11,column=1)


input_symbol=StringVar()
e1=Entry(window, textvariable=input_symbol)
e1.grid(row=11,column=2)

reset=StringVar()
e1=Entry(window, textvariable=reset)
e1.grid(row=11,column=3)


guards=StringVar()
e1=Entry(window, textvariable=guards)
e1.grid(row=11,column=4)




from_state=StringVar()
e1=Entry(window, textvariable=from_state)
e1.grid(row=13,column=0)


to_state=StringVar()
e1=Entry(window, textvariable=to_state)
e1.grid(row=13,column=1)


input_symbol=StringVar()
e1=Entry(window, textvariable=input_symbol)
e1.grid(row=13,column=2)

reset=StringVar()
e1=Entry(window, textvariable=reset)
e1.grid(row=13,column=3)


guards=StringVar()
e1=Entry(window, textvariable=guards)
e1.grid(row=13,column=4)



from_state=StringVar()
e1=Entry(window, textvariable=from_state)
e1.grid(row=14,column=0)


to_state=StringVar()
e1=Entry(window, textvariable=to_state)
e1.grid(row=14,column=1)


input_symbol=StringVar()
e1=Entry(window, textvariable=input_symbol)
e1.grid(row=14,column=2)

reset=StringVar()
e1=Entry(window, textvariable=reset)
e1.grid(row=14,column=3)


guards=StringVar()
e1=Entry(window, textvariable=guards)
e1.grid(row=14,column=4)



from_state=StringVar()
e1=Entry(window, textvariable=from_state)
e1.grid(row=15,column=0)


to_state=StringVar()
e1=Entry(window, textvariable=to_state)
e1.grid(row=15,column=1)


input_symbol=StringVar()
e1=Entry(window, textvariable=input_symbol)
e1.grid(row=15,column=2)

reset=StringVar()
e1=Entry(window, textvariable=reset)
e1.grid(row=15,column=3)


guards=StringVar()
e1=Entry(window, textvariable=guards)
e1.grid(row=15,column=4)


"""

#for entries in alphabet_list:

window.mainloop()
