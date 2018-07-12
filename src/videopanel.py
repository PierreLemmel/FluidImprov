import tkinter as tk;

from fluidpanel import FluidPanel;

class VideoPanel(FluidPanel):

	childPaddingX = 4;
	childPaddingY = 5;

	buttonWidth = 17;
	widgetHeight = 2;


	def __init__(self, parent, **options):
		super(FluidPanel, self).__init__(parent, options);