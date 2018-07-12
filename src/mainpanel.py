import tkinter as tk;

from fluidpanel import FluidPanel;
from speechpanel import SpeechPanel;

class MainPanel(FluidPanel):

	def __init__(self, parent, **options):
		super(FluidPanel, self).__init__(parent, options);

		row = 0;
		col = 0;
		self.__initSpeechPanel(row, col);


		hWeights = [1];
		vWeights = [1];

		self._setupGrid(hWeights, vWeights);


	def __initSpeechPanel(self, row, col):
		self.speechPanel = SpeechPanel(self);
		self.speechPanel.grid(row = row, column = col, sticky = self.NSEW);