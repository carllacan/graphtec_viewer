#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkwrapper import tkwrapper
from tkwrapper.option import option

#import tkinter as tk
#from tkinter import ttk

import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


# TODO: make it so that I can call option classes as tkwrapper.option.NumEntry
class PlotFrame (tkwrapper.Frame):
    
    def __init__(self, parent, row, col):
        tkwrapper.Frame.__init__(self, parent, row, col,
                                 border=False,
                                 title="")
        
        self.xmin = 0
        self.xmax = 100
        
        self.ymin = 0
        self.ymax = 100
        
        # make the plot object
        
        self.cursor1pos = (0,0)
        self.cursor2pos = (0,0)
        self.cursor1channel = (0,0)
        self.cursor2channel = (0,0)
        
        self.xs = np.linspace(self.xmin, self.xmax)
        self.ys = np.linspace(self.ymin, self.ymax)
        self.canvas = 0
        
        f = Figure(figsize=(6, 2), dpi=100, facecolor='none',
                   tight_layout=True)
        
        plt = f.add_subplot(111)
        plt.plot(self.xs, self.ys, '-')
        plt.set_xlabel('Tiempo (s)')
        plt.set_ylabel('Temperatura (A)')
        
        self.canvas = FigureCanvasTkAgg(f, master=self)
        self.canvas.show()
        self.canvas._tkcanvas.grid(row=0,column=0)
#                                   sticky = tk.E)
        
    def update(self):
        pass
                

            
class ChannelsFrame(tkwrapper.Frame):
    def __init__(self, parent, row, col):
        tkwrapper.Frame.__init__(self, parent, row, col,
                                 border=True,
                                title="Channels") # can object init the padding?
        
#        tkwrapper.Object.__init__(self, parent, row, col)
        
        self.channelframes =  []
        colors = ["blue",
                  "red",
                  "green",
                  "orange",
                  "purple",
                  "blue",
                  "red",
                  "green",
                  "orange",
                  "purple"]
        for i in range(0, 10):
            print(i)
            self.channelframes.append(ChannelFrame(self, i, 0, 
                                                   i, colors[i]))

class LeftAxisFrame(tkwrapper.Frame):
    
    def __init__(self, parent, row, col):
        tkwrapper.Frame.__init__(self, parent, row, col,
                                title="Left axis") # can object init the padding?
        
        tkwrapper.Object.__init__(self, parent, row, col)
        
        self.minimum = option.NumEntry(self, 0, 0, "Min", default=0)
        self.maximum = option.NumEntry(self, 1, 0, "Max", default=100)
        self.units = option.List(self, 2, 0, "Unit", choices=["a", "b"], default = 0)
        
class Cursor1Frame(tkwrapper.Frame):
    
    def __init__(self, parent, row, col):
        tkwrapper.Frame.__init__(self, parent, row, col,
                           title="Cursor 1")
        
#        tkwrapper.Object.__init__(self, parent, row, col)
        # needs the cursor object to callbacks
        
        self.xpos = option.NumEntry(self, 0, 0, label = "Pos")
        # if xpos set to X cursor jumps to that xpos
        self.ypos =option. NumEntry(self, 1, 0, label = "Value")
        # if ypos set to X move to the next pos with value == X, or closest possible
        self.channel = option.List(self, 2, 0, label = "Channel")
        
        #TODO: set to next maximum
        #TODO: set to next minimum
        #TODO: set to next zero
        
class ChannelFrame(tkwrapper.Frame):
    
    def __init__(self, parent, row, col, number, color):
        tkwrapper.Frame.__init__(self, parent, row, col,
                           title="", border = True)
        
        self.number = number
        self.color = color
        
        # TODO: a square the color of the plot with a number inside
        self.square = None
        
        # TODO: don't add a label in options if label is ""
        self.name = option.Entry(self, number, 1, 
                                 label= str(number), 
                                 default="Channel {}".format(number))
        self.active = option.CheckBox(self, number, 2,
                                      label = "",
                                      default = False)
        
        
        
##############################

class MainFrame (tkwrapper.Frame):
    # Should this object maintain the state of the program? the data?
    def __init__(self, parent, row, col):
        tkwrapper.Frame.__init__(self, parent, row, col)
        
        # what is this?
#        parent.report_callback_exception = self.report_callback_exception
        
        # Init the subobjects
        self.plotframe = PlotFrame(self, 0, (0, 5))
        self.leftaxisframe = LeftAxisFrame(self, 1, 0)
        self.rightaxisframe = LeftAxisFrame(self, 1, 1)
        self.timeaxisframe= LeftAxisFrame(self, 1, 2)
        self.cursor1frame= Cursor1Frame(self, 1, 3)
        self.cursor2frame= Cursor1Frame(self, 1, 4)
        self.cursordiffframe= Cursor1Frame(self, 1, 5)
        
        self.channelsframe = ChannelsFrame(self, (0, 1), 7)
        
    
root = tkwrapper.Root()
    
root.title("Whatever")
mainframe = MainFrame(root, 0, 0)
    
        
for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)


root.mainloop()
