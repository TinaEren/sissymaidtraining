# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 18:41:37 2019

@author: TinaEREN
"""

from tkinter import *
  
from tkinter import ttk
  
window = Tk()
style = ttk.Style()
style.configure("TNotebook", background='DeepPink', foreground='white') 
  
window.title("Sissy Maid Training")
window.geometry("800x550")  
tab_control = ttk.Notebook(window, padding=(10, 5, 10, 5), style="TNotebook")




tab1 = ttk.Frame(tab_control)
  
tab2 = ttk.Frame(tab_control)
  
tab_control.add(tab1, text='First')
  
tab_control.add(tab2, text='Second')

tab_control.add(tab2, text='third')

  
lbl1 = Label(tab1, text= 'label1')
  
lbl1.grid(column=0, row=0)
  
lbl2 = Label(tab2, text= 'label2')
  
lbl2.grid(column=0, row=0)

lbl3 = Label(tab3, text= 'label3')
  
lbl3.grid(column=0, row=0)

  
tab_control.pack(expand=1, fill='both')
  
window.mainloop()

