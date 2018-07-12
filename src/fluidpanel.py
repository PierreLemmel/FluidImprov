import tkinter as tk;

class FluidPanel(tk.Frame):

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