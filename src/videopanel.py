import tkinter as tk;

class VideoPanel(tk.Frame):

	childPaddingX = 4;
	childPaddingY = 5;

	buttonWidth = 17;
	widgetHeight = 2;

	NSEW = (tk.N, tk.S, tk.E, tk.W);


	def __init__(self, parent):
		tk.Frame.__init__(self, parent);