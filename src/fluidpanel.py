import tkinter as tk;

class FluidPanel(tk.Frame):

	_childPaddingX = 4;
	_childPaddingY = 5;

	_buttonWidth = 17;
	_widgetHeight = 2;

	NSEW = (tk.N, tk.S, tk.E, tk.W);


	def __init__(self, parent, **options):
		
		super().__init__(parent);


	def _setupGrid(self, horizontalWeights, verticalWeights):

		i = 0;
		for hWeight in horizontalWeights:
			self.columnconfigure(i, weight = hWeight);
			i += 1;

		j = 0;
		for vWeight in verticalWeights:
			self.rowconfigure(j, weight = vWeight);
			j += 1;


	def _setControlsPadding(self, padx, pady):
		for control in self.winfo_children():
			control.grid_configure(padx = padx, pady = pady);


	def _funcCheck(self, func):
		if not callable(func):
			raise ValueError('The input parameter is not a function');


	def _retrieveParam(self, options, key, default = None):
		value = options.get(key, default);

		if (key in options):
			del options[key];

		return value;