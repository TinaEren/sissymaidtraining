# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 18:41:37 2019

@author: TinaEREN
"""

import tkinter
from tkinter import ttk
from tkinter import *

root = tkinter.Tk()

root.title("Window Title")

style = ttk.Style()
settings = { "TNotebook": {"configure": {"padding": [5, 5, 5, 5],"background": "#bfbfbf"}},
             "TNotebook.Tab": {"configure": {"padding": [5, 1],
                                             "background": "#f0f0f0"
                                             }
                               }
             }

style.theme_create("Mystyle", parent="alt", settings=settings)
style.theme_use("Mystyle")

def on_tab(event):
    global tab_styles
    global style
    nb = event.widget
    tab = nb.tab(nb.select(), "text")
    st = tab_styles[tab]
    style.map('TNotebook.Tab', **st)

tab_styles = {}
nb = ttk.Notebook(width=693, height=555)
nb.pressed_index = None


f1 = tkinter.Frame(nb, background="#ffffff")
f2 = tkinter.Frame(nb, background="#ffffff")
f3 = tkinter.Frame(nb, background="#ffffff")

nb.add(f1, text="Tab1")
tab_styles["Tab1"] = {"background": [("selected", "#ffffff")],
                                              "foreground": [("selected", "#000000")]
                                              }

nb.add(f2, text="Tab2")
tab_styles["Tab2"] = {"background": [("selected", "#ffffff")],
                                                "foreground": [("selected", "#000000")]
                                                }
nb.add(f3, text="Tab3")
tab_styles["Tab3"] = {"background": [("selected", "#ffffff")],
                      "foreground": [("selected", "#000000")]
                      }
lbl1 = Label(f1, text='label1', background="#ffffff")

lbl1.grid(column=0, row=0)

lbl2 = Label(f2, text='label2', background="#ffffff")

lbl2.grid(column=0, row=0)

lbl3 = Label(f3, text='label3', background="#ffffff")

lbl3.grid(column=0, row=0)

nb.pack(expand=1, fill='both')
nb.bind("<<NotebookTabChanged>>", on_tab)
root.mainloop()
