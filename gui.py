# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 18:41:37 2019

@author: TinaEREN
"""

import tkinter
from tkinter import ttk
from tkinter import *

root = tkinter.Tk()
root.title("Maid Training")
root.geometry("692x555")

style = ttk.Style()
settings = { "TNotebook": {"configure": {"padding": [5, 5, 5, 5],"background":"DeepPink" }},
             "TNotebook.Tab": {"configure": {"padding": [3, 3],
                                             "background": "#f0f0f0"
                                             }
                               }
             }
style.theme_create("Maidstyle", parent="alt", settings=settings)
style.theme_use("Maidstyle")


             
def on_tab(event):
    global tab_styles
    global style
    nb = event.widget
    tab = nb.tab(nb.select(), "text")
    st = tab_styles[tab]
    style.map('TNotebook.Tab', **st)

tab_styles = {}
nb = ttk.Notebook()
nb.pressed_index = None


f1 = tkinter.Frame(nb, background="#ffffff")
f2 = tkinter.Frame(nb, background="#ffffff")
f3 = tkinter.Frame(nb, background="#ffffff")
f4 = tkinter.Frame(nb, background="#ffffff")
f5 = tkinter.Frame(nb, background="#ffffff")
f6 = tkinter.Frame(nb, background="#ffffff")
f7 = tkinter.Frame(nb, background="#ffffff")
f8 = tkinter.Frame(nb, background="#ffffff")
f9 = tkinter.Frame(nb, background="#ffffff")

nb.add(f1, text="Report")
tab_styles["Report"] = {"background": [("selected", "#ffffff")],
                                              "foreground": [("selected", "#000000")]
                                              }

nb.add(f2, text="Status")
tab_styles["Status"] = {"background": [("selected", "#ffffff")],
                                                "foreground": [("selected", "#000000")]
                                                }
nb.add(f3, text="Maid in uniform")
tab_styles["Maid in uniform"] = {"background": [("selected", "#ffffff")],
                      "foreground": [("selected", "#000000")]
                      }

nb.add(f4, text="Chores for the maid")
tab_styles["Chores for the maid"] = {"background": [("selected", "#ffffff")],
                                              "foreground": [("selected", "#000000")]
                                              }

nb.add(f5, text="Training Of the maid")
tab_styles["Training of the maid"] = {"background": [("selected", "#ffffff")],
                                                "foreground": [("selected", "#000000")]
                                                }
nb.add(f6, text="Permissions")
tab_styles["Permissions"] = {"background": [("selected", "#ffffff")],
                      "foreground": [("selected", "#000000")]
                      }

nb.add(f7, text="Punishments")
tab_styles["Punishments"] = {"background": [("selected", "#ffffff")],
                                              "foreground": [("selected", "#000000")]
                                              }

nb.add(f8, text="Assigned to")
tab_styles["Assigned to"] = {"background": [("selected", "#ffffff")],
                                                "foreground": [("selected", "#000000")]
                                                }
nb.add(f9, text="?")
tab_styles["?"] = {"background": [("selected", "#ffffff")],
                      "foreground": [("selected", "#000000")]
                      }

lbl1 = Label(f1, text='label1', background="#ffffff")
lbl1.grid(column=0, row=0)

lbl2 = Label(f2, text='label2', background="#ffffff")
lbl2.grid(column=0, row=0)

lbl3 = Label(f2, text='label2', background="#ffffff")
lbl2.grid(column=0, row=0)

lbl2 = Label(f2, text='label2', background="#ffffff")
lbl2.grid(column=0, row=0)

lbl1 = Label(f1, text='label1', background="#ffffff")
lbl1.grid(column=0, row=0)

lbl6 = Label(f3, text='label3', background="#ffffff")

lbl6.grid(column=0, row=0)

lbl7 = Label(f1, text='label1', background="#ffffff")

lbl7.grid(column=0, row=0)

lbl8 = Label(f8, text='label8', background="#ffffff")

lbl8.grid(column=0, row=0)

lbl9 = Label(f9, text='label3', background="#ffffff")

lbl9.grid(column=0, row=0)

nb.pack(expand=1, fill='both')
nb.bind("<<NotebookTabChanged>>", on_tab)
root.mainloop()
