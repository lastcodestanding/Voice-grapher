from tkinter import *
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg, NavigationToolbar2Tk)
from time import sleep
import m1
import sympy
from sympy.abc import q
import numpy as np

import speech_recognition as sr
# create the recognizer
def rec():
    r = sr.Recognizer()
    # define the microphone
    mic = sr.Microphone(device_index=0)
    # record your speech
    with mic as source:
        #r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # speech recognition
    result = r.recognize_google(audio)
    # export the result
    with open('my_result.txt',mode ='w') as file:
       #file.write("Recognized text:")
       #file.write("\n")
       file.write(result)
    print("Exporting process completed!")
    f = open("my_result.txt", "r")
    result = (f.read())
    print("You said:", result)
    result = "e ^ (2 x)"
    if "derivative of" in result.lower():
        plot(result[14:].lower(), dx = True)
    elif "integral of" in result.lower():
        plot(result[12:].lower(),ig = True)
    else:
        plot(result.lower())

# plot function is created for
# plotting the graph in
# tkinter window
def plot(result, dx=False, ig=False):

    l = Label(master=window, text = ("" if dx==False else "Derivative of ")+("" if ig==False else "Integral of ")+ result)

    l.config(font =("Courier", 10))
    l.pack()
    window.update()
    # the figure that will contain the plot
    fig = Figure(figsize = (7, 7),
                 dpi = 300)



    x = np.arange(0,3,0.001)
    # list of squares
    result = m1.format_space(result)
    print("f",result)
    result = m1.words2symbol(result)
    print("w2s",result)

    y = m1.f(result)
    print(y)
    # adding the subplot
    plot1 = fig.add_subplot(111)

    # plotting the graph
    if dx==False and ig==False:
        plot1.plot(x,y)
    elif dx:
        plot1.plot(x[1:],np.diff(y)/np.diff(x))
    elif ig:
        result1 = result.replace('x','q')
        print(result1)
        exp = sympy.sympify(result1)
        iexp = sympy.integrate(exp,q)
        print(iexp)
        for i in range(len(x)):
            y[i] = iexp.subs(q,x[i]).evalf()
            print(y[i])
        plot1.plot(x,y)

    # creating the Tkinter canvas
    # containing the Matplotlib figure
    canvas = FigureCanvasTkAgg(fig, master = window)
    canvas.draw()

    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()

    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,
                                   window)
    toolbar.update()

    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack()

# the main Tkinter window
window = Tk()

# setting the title
window.title('Voice-Graphing Calculator')

# dimensions of the main window
window.geometry("1500x700")

# button that displays the plot
plot_button = Button(master = window,
                     command = rec,
                     height = 2,
                     width = 10,
                     text = "Speak")
window.update()
# place the button
# in main window
plot_button.pack()

# run the gui
window.mainloop()
