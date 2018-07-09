import tkinter as tk;

class MainWindow(tk.Frame):

	childPaddingX = 4;
	childPaddingY = 5;

	buttonWidth = 17;
	widgetHeight = 2;

	NSEW = (tk.N, tk.S, tk.E, tk.W);

	def __init__(self, parent):
		tk.Frame.__init__(self, parent);

		self.__speechSubmittedCallback = None;
		self.__rateScaleValueChangedCallback = None;
		self.__pitchScaleValueChangedCallback = None;
		self.__cancelButtonClickedCallback = None;
		
		hWeights = [0, 1, 0];
		vWeights = [1, 0, 0, 0];

		row = 0;
		self.__initializeSpeechTextRow(row);
		row += 1;
		self.__initializeRateScaleRow(row);
		row += 1;
		self.__initializePitchScaleRow(row);
		row += 1;
		self.__initializeCancelButtonRow(row);

		self.__setupGrid(hWeights, vWeights);
		self.__setControlsPadding(self.childPaddingX, self.childPaddingY);


	def OnSpeechSubmittedCallback(self, callback):
		self.__funcCheck(callback);
		self.__speechSubmittedCallback = callback;


	def OnRateScaleValueChangedCallback(self, callback):
		self.__funcCheck(callback);
		self.__rateScaleValueChangedCallback = callback;


	def OnPitchScaleValueChangedCallback(self, callback):
		self.__funcCheck(callback);
		self.__pitchScaleValueChangedCallback = callback;


	def OnCancelButtonClickedCallback(self, callback):
		self.__funcCheck(callback);
		self.__cancelButtonClickedCallback = callback;


	def __setupGrid(self, horizontalWeights, verticalWeights):
		i = 0;
		for hWeight in horizontalWeights:
			self.columnconfigure(i, weight = hWeight);
			i += 1;

		j = 0;
		for vWeight in verticalWeights:
			self.rowconfigure(j, weight = vWeight);
			j += 1;


	def __setControlsPadding(self, padx, pady):
		for control in self.winfo_children():
			control.grid_configure(padx = padx, pady = pady);


	def __funcCheck(self, func):
		if not callable(func):
			raise ValueError('The input parameter is not a function');


	def __initializeSpeechTextRow(self, row):
		col = 0;

		speechTextLabel = tk.Label(self, anchor = tk.E, text='Saisissez un texte à énoncer :');
		speechTextLabel.grid(row = row, column = col);
		col += 1;

		self.speechTextEntry = tk.Text(self, width = 0);
		self.speechTextEntry.grid(row = row, column = col, sticky = self.NSEW);
		col += 1;

		self.speechTextBtn = tk.Button(self, text = 'Énoncer', width = self.buttonWidth, height = self.widgetHeight, command = self.__onSpeechTextClick);
		self.speechTextBtn.grid(row = row, column = col);


	def __initializeRateScaleRow(self, row):
		col = 0;

		rateTextLabel = tk.Label(self, anchor = tk.E, text='Vitesse du texte :');
		rateTextLabel.grid(row = row, column = col);
		col += 1;

		self.rateTextScale = tk.Scale(self, orient = 'horizontal', command = self.__onRateScaleChanged);
		self.rateTextScale.grid(row = row, column = col, sticky = self.NSEW);


	def __initializePitchScaleRow(self, row):
		pass;


	def __initializeCancelButtonRow(self, row):
		pass;


	def __onSpeechTextClick(self, *args):
		text = self.speechTextEntry.get('1.0', 'end-1c');
		if self.__speechSubmittedCallback is not None:
			self.__speechSubmittedCallback(text);


	def __onRateScaleChanged(self, *args):
		pass;