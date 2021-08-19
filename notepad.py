import tkinter as tk


def closeProgram():
    save_one_line()
    exit(0)


def save_one_line():    #saving one line of buffer to hidden file
    global one_line
    saved_file = open('saved_file.txt','a')
    if one_line:
        saved_file.write(one_line)
    saved_file.write('\n')
    saved_file.close()
    one_line = ""        #empty the buffer
    print(one_line)
    

def get_fake_data():           #fake data to be retrieved from file 
    fake_file = open("fake_file.txt",'r')
    fake_data = fake_file.readlines()
    fake_data = [line[:-1] for line in fake_data]
    fake_data = " ".join(fake_data)
    return fake_data  

def pressClear():      #when clear is pressed
    t.configure(state='normal')
    t.delete("1.0",tk.END)    #clear the box
    if not caught:
        t.configure(state='disabled')
    else:
        t.configure(state='normal')
        t.focus_set()
    


def pressed(key):     #when a key is pressed
    global one_line
    global count
    global caught
    to_show = 'x'     #it is string to show to user
    if key.char == "\\":      #it is \  
        save_one_line()
        t.configure(state='normal')
        t.focus_set()
        caught = True
    
    if caught:    #when get caught
        return

    if key.char == "\r":   #when we press enter
        cmplete_wrd = ""
        while fake_str[count] != " ":      #word completion
            cmplete_wrd += fake_str[count]
            count += 1 

        to_show = cmplete_wrd+'\n'
        count+=1
        save_one_line()

    elif key.keycode==22:   #backspace
        #in real buffer
        if len(one_line) > 1:
            one_line = one_line[:-1]
        #to show user
        t.configure(state='normal')
        t.focus_set()
        return  

    else:             #for any other character
        to_show = fake_str[count]
        count += 1
        one_line += key.char   #put fake character in buffer

    t.configure(state='normal')
    t.insert(tk.END,to_show)    #this is where we actually put in text box
    t.configure(state='disabled')



#global variables
one_line = ""   #store one line 
fake_str = get_fake_data()    #all fake data in string format
count = 0   #fake data fetch count
caught = False        #are we caught
   


#tkinter code
root = tk.Tk()

root.title("heybuddy")
#root.geometry("500x500")

#text box
t = tk.Text(root,height=30,width=80)
t.pack()
t.configure(state='disabled')

#clear button
clearBtn = tk.Button(root,text="Clear",command=pressClear)
clearBtn.pack()


#exit button
exitBtn = tk.Button(root,text="Exit",command=closeProgram)
exitBtn.pack()



#for everykey press, run pressed fxn
root.bind('<KeyPress>',pressed)

root.mainloop()
