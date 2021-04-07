From tkintar import *
From tkintar.ttk import *

From time import strftime

Root = tk()
Root.title("clock")

def time():
  string = strftime('%H:%M:%S %p')
  label.config(text=string)
  label.after(1000, time)

Label = Label(root, font=("arial", 80), background = "gray", foreground = "red")
Lable.pck(anchor='center')
time()

mainloop()
