import tkinter as tk;

from fluidpanel import FluidPanel;

class SpeechPanel(FluidPanel):

	def __init__(self, parent, **options):
		super(FluidPanel, self).__init__(parent, options);

		self.__speechSubmittedCallback = None;
		self.__rateSliderValueChangedCallback = None;
		self.__pitchSliderValueChangedCallback = None;
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

		self._setupGrid(hWeights, vWeights);
		self._setControlsPadding(self._childPaddingX, self._childPaddingY);


	def OnSpeechSubmittedCallback(self, callback):
		self._funcCheck(callback);
		self.__speechSubmittedCallback = callback;


	def OnRateSliderValueChangedCallback(self, callback):
		self._funcCheck(callback);
		self.__rateSliderValueChangedCallback = callback;


	def OnPitchSliderValueChangedCallback(self, callback):
		self._funcCheck(callback);
		self.__pitchSliderValueChangedCallback = callback;


	def OnCancelButtonClickedCallback(self, callback):
		self._funcCheck(callback);
		self.__cancelButtonClickedCallback = callback;


	def __initializeSpeechTextRow(self, row):
		col = 0;

		speechTextLabel = tk.Label(self, anchor = tk.E, text='Saisissez un texte à énoncer :');
		speechTextLabel.grid(row = row, column = col);
		col += 1;

		self.speechTextEntry = tk.Text(self, width = 0);
		self.speechTextEntry.grid(row = row, column = col, sticky = self.NSEW);
		col += 1;

		self.speechTextBtn = tk.Button(self, text = 'Énoncer', width = self._buttonWidth, height = self._widgetHeight, command = self.__onSpeechTextClick);
		self.speechTextBtn.grid(row = row, column = col);


	def __initializeRateScaleRow(self, row):
		col = 0;

		rateTextLabel = tk.Label(self, anchor = tk.E, text = 'Vitesse du texte :');
		rateTextLabel.grid(row = row, column = col);
		col += 1;

		self.textRateSlider = RateSlider(self, command = self.__onRateSliderChanged);
		self.textRateSlider.grid(row = row, column = col, sticky = self.NSEW);


	def __initializePitchScaleRow(self, row):
		col = 0;

		pitchTextLabel = tk.Label(self, anchor = tk.E, text = 'Hauteur de la voix :');
		pitchTextLabel.grid(row = row, column = col);
		col += 1;

		self.textPitchSlider = PitchSlider(self, command = self.__onPitchSliderChanged);
		self.textPitchSlider.grid(row = row, column = col, sticky = self.NSEW);


	def __initializeCancelButtonRow(self, row):
		self.cancelButton = tk.Button(self, width = self._buttonWidth, height = self._widgetHeight, command = self.__onCancelButtonClick, text = 'Annuler');
		self.cancelButton.grid(row = row, column = 1);


	def __onSpeechTextClick(self, *args):
		text = self.speechTextEntry.get('1.0', 'end-1c');
		if self.__speechSubmittedCallback is not None:
			self.__speechSubmittedCallback(text);


	def __onRateSliderChanged(self, *args):
		rate = self.textRateSlider.get();
		if self.__rateSliderValueChangedCallback is not None:
			self.__rateSliderValueChangedCallback(rate);


	def __onPitchSliderChanged(self, *args):
		pitch = self.textPitchSlider.get();
		if self.__pitchSliderValueChangedCallback is not None:
			self.__pitchSliderValueChangedCallback(pitch);


	def __onCancelButtonClick(self, *args):
		if self.__cancelButtonClickedCallback is not None:
			self.__cancelButtonClickedCallback();




class RateSlider(FluidPanel):

	def __init__(self, parent, **options):

		self.__command = options.get('command', None);
		if (self.__command and not callable(self.__command)):
			raise ValueError('The input parameter is not a function');

		if ('command' in options):
			del options['command'];

		super(FluidPanel, self).__init__(parent, options);
		
		self.number = 1.0;
		self.slide = tk.Scale(self, orient = tk.HORIZONTAL, command = self.__setValue, showvalue = 0, fro = 0, to = 20, sliderrelief = tk.RIDGE);
		self.text = tk.Label(self);

		textX01 = tk.Label(self, text = 'x 0,10', anchor = tk.W);
		textX1 = tk.Label(self, text = 'x 1,00');
		textx10 = tk.Label(self, text = 'x 10,00', anchor = tk.E);
		
		self.text.grid(sticky = self.NSEW, row = 0, column = 0, rowspan = 1, columnspan = 3);
		self.slide.grid(sticky = self.NSEW, row = 1, column = 0, rowspan = 1, columnspan = 3);
		textX01.grid(sticky = self.NSEW, row = 2, column = 0);
		textX1.grid(sticky = self.NSEW, row = 2, column = 1);
		textx10.grid(sticky = self.NSEW, row = 2, column = 2);
		
		self._setupGrid([1, 1, 1], [1, 1, 1]);

		self.slide.set(10);


	def __setValue(self, val):

		nbVal = 0.1 * 10 ** (float(val) / 10.0);

		self.number = nbVal;
		self.text.configure(text = 'Vitesse x {0:.2f}'.format(self.number));

		if (self.__command):
			self.__command(nbVal);


	def get(self):
		return self.number;




class PitchSlider(FluidPanel):

	def __init__(self, parent, **options):

		self.__command = options.get('command', None);
		if (self.__command and not callable(self.__command)):
			raise ValueError('The input parameter is not a function');

		if ('command' in options):
			del options['command'];

		super(FluidPanel, self).__init__(parent, options);

		self.number = 1.0;
		self.slide = tk.Scale(self, orient = tk.HORIZONTAL, command = self.__setValue, showvalue = 0, fro = 0.0, to = 2.0, sliderrelief = tk.RIDGE, resolution = 0.05);
		self.text = tk.Label(self);

		txt000 = tk.Label(self, text = '0,00', anchor = tk.W);
		txt100 = tk.Label(self, text = '1,00');
		txt200 = tk.Label(self, text = '2,00', anchor = tk.E);
		
		self.text.grid(sticky = self.NSEW, row = 0, column = 0, rowspan = 1, columnspan = 3);
		self.slide.grid(sticky = self.NSEW, row = 1, column = 0, rowspan = 1, columnspan = 3);
		txt000.grid(sticky = self.NSEW, row = 2, column = 0);
		txt100.grid(sticky = self.NSEW, row = 2, column = 1);
		txt200.grid(sticky = self.NSEW, row = 2, column = 2);
		
		self._setupGrid([1, 1, 1], [1, 1, 1]);

		self.slide.set(1.0);


	def __setValue(self, val):

		nbVal = float(val);

		self.number = nbVal;
		self.text.configure(text = 'Hauteur : {0:.2f}'.format(self.number));

		if (self.__command):
			self.__command(nbVal);


	def get(self):
		return self.number;