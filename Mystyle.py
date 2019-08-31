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
root.geometry("693x555")

style = ttk.Style()
settings = { "TNotebook": {"configure": {"padding": [5, 5, 5, 5],"background":"DeepPink" },
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

nb.add(f1, text="Tab4")
tab_styles["Tab1"] = {"background": [("selected", "#ffffff")],
                                              "foreground": [("selected", "#000000")]
                                              }

nb.add(f2, text="Tab2")
tab_styles["Tab8"] = {"background": [("selected", "#ffffff")],
                                                "foreground": [("selected", "#000000")]
                                                }
nb.add(f3, text="Tab3")
tab_styles["Tab3"] = {"background": [("selected", "#ffffff")],
                      "foreground": [("selected", "#000000")]
                      }

nb.add(f4, text="Tab4")
tab_styles["Tab4"] = {"background": [("selected", "#ffffff")],
                                              "foreground": [("selected", "#000000")]
                                              }

nb.add(f5, text="Tab5")
tab_styles["Tab5"] = {"background": [("selected", "#ffffff")],
                                                "foreground": [("selected", "#000000")]
                                                }
nb.add(f6, text="Tab6")
tab_styles["Tab6"] = {"background": [("selected", "#ffffff")],
                      "foreground": [("selected", "#000000")]
                      }

nb.add(f7, text="Tab7")
tab_styles["Tab7"] = {"background": [("selected", "#ffffff")],
                                              "foreground": [("selected", "#000000")]
                                              }

nb.add(f8, text="Tab8")
tab_styles["Tab8"] = {"background": [("selected", "#ffffff")],
                                                "foreground": [("selected", "#000000")]
                                                }
nb.add(f9, text="Tab9")
tab_styles["Tab9"] = {"background": [("selected", "#ffffff")],
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
