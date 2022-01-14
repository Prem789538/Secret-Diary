import tkinter as tk



class DiaryWriter:
    def __init__(self,saved_file_path):
        self.saved_file_path = saved_file_path
        self.one_line = ""
        self.caught = False
        self.count = 0

        self.get_fake_data()

        self.windo = tk.Tk()
        self.windo.title("Diary writer")

        self.windo.protocol("WM_DELETE_WINDOW",self.disable_event)

        #text box
        self.txt = tk.Text(self.windo,height=30,width=80)
        self.txt.pack()
        self.txt.configure(state='disabled')

        #clear button
        self.clearBtn = tk.Button(self.windo,text="Clear",command=self.pressClear)
        self.clearBtn.pack()


        #exit button
        self.exitBtn = tk.Button(self.windo,text="Exit",command=self.closeProgram)
        self.exitBtn.pack()



        self.windo.bind('<KeyPress>',self.pressed)
        self.windo.mainloop()
    

    def disable_event(self):
        pass


    def closeProgram(self):
        self.save_one_line()
        self.windo.destroy()


        


    def pressClear(self):      #when clear is pressed
        self.txt.configure(state='normal')
        self.txt.delete("1.0",tk.END)    #clear the box
        if not self.caught:
            self.txt.configure(state='disabled')
        else:
            self.txt.configure(state='normal')
            self.txt.focus_set()


    def save_one_line(self):    #saving one line of buffer to hidden file
        if not self.one_line:
            return
        saved_file = open(self.saved_file_path,'a')
        saved_file.write(self.one_line)
        saved_file.write('\n')
        saved_file.close()
        self.one_line = ""        #empty the buffer


    def pressed(self,key):     #when a key is pressed
        to_show = 'x'     #it is string to show to user
        if key.char == "\\":      #it is \  
            self.save_one_line()
            self.txt.configure(state='normal')
            self.txt.focus_set()
            self.caught = True
        
        if self.caught:    #when get caught
            return

        if key.char == "\r":   #when we press enter
            cmplete_wrd = ""
            while self.fake_str[self.count] != " ":      #word completion
                cmplete_wrd += self.fake_str[self.count]
                self.count += 1 

            to_show = cmplete_wrd+'\n'
            self.count+=1
            self.save_one_line()

        elif key.keycode==22:   #backspace (22 => linux & 8 => windows)
            #in real buffer
            if len(self.one_line) > 1:
                self.one_line = self.one_line[:-1]
            #to show user
            self.txt.configure(state='normal')
            self.txt.focus_set()
            return  

        else:             #for any other character
            to_show = self.fake_str[self.count]
            self.count += 1
            self.one_line += key.char   #put fake character in buffer

        self.txt.configure(state='normal')
        self.txt.insert(tk.END,to_show)    #this is where we actually put in text box
        self.txt.configure(state='disabled')


    def get_fake_data(self):           #fake data to be retrieved from file 
        fake_file = open("fake_file.txt",'r')
        fake_data = fake_file.readlines()
        fake_data = [line[:-1] for line in fake_data]
        fake_data = " ".join(fake_data)
        self.fake_str = fake_data 
    


DiaryWriter("saved_file.txt")
