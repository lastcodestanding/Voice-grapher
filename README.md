# Voice-grapher
Latest version - v6

This python application uses voice commands to graph functions in two dimensions.
The functions we support are:
sin, cos, log, tan, asin, acos, atan, exp, +, -, /, *.
The code uses google voice recognition to convert the spoken equation to a string.
Then, it evaluates it with BODMAS, using a recursive function.

To run the code, download the entire v5 file, and run gui.py. 
Click the 'Speak' button in the Tkinter, and say the function in terms of x.
'(' and ')' must be said as 'open bracket' and 'close bracket'.
To plot a second graph, you must restart the program.

In case it fails to recognize your voice, you can press the speak button, but the program
will be terminated if a graph is plotted.

Dependencies: numpy, sympy, matplotlib, tkinter, speech-recognition (need to be installed using pip/other methods)
