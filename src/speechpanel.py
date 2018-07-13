import tkinter as tk;

from fluidpanel import FluidPanel;
from fluidslider import FluidSlider;

class SpeechPanel(FluidPanel):

	def __init__(self, parent, **options):
		super(FluidPanel, self).__init__(parent, options);

		self.__speechSubmittedCallback = None;
		self.__rateSliderValueChangedCallback = None;
		self.__pitchSliderValueChangedCallback = None;
		self.__cancelButtonClickedCallback = None;
		
		hWeights = [0, 1, 0, 0, 1];
		vWeights = [1, 0, 0, 0];

		row = 0;
		self.__initializeSpeechTextRow(row);
		row += 1;
		self.__initializeRateScaleRow(row);
		row += 1;
		self.__initializePitchScaleRow(row);
		row += 1;
		self.__initializeButtonsRow(row);

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
		self.speechTextEntry.grid(row = row, column = col, rowspan = 1, columnspan = 4, sticky = self.NSEW);	


	def __initializeRateScaleRow(self, row):

		col = 0;
		rateTextLabel = tk.Label(self, anchor = tk.E, text = 'Vitesse du texte :');
		rateTextLabel.grid(row = row, column = col);
		
		col += 1;
		self.textRateSlider = FluidSlider(self, command = self.__onRateSliderChanged, minValue = 0, initialValue = 10, maxValue = 20,
											valueFormat = 'Vitesse x {0:.2f}', labelFormat = 'x {0:.2f}', valueTransform = lambda v: 0.1 * 10 ** (v / 10.0));
		self.textRateSlider.grid(row = row, column = col, rowspan = 1, columnspan = 4, sticky = self.NSEW);


	def __initializePitchScaleRow(self, row):

		col = 0;
		pitchTextLabel = tk.Label(self, anchor = tk.E, text = 'Hauteur de la voix :');
		pitchTextLabel.grid(row = row, column = col);

		col += 1;
		self.textPitchSlider = FluidSlider(self, command = self.__onPitchSliderChanged, minValue = 0.0, initialValue = 1.0, maxValue = 2.0,
											valueFormat = 'Hauteur : {0:.2f}', labelFormat = '{0:.2f}', resolution = 0.05);
		self.textPitchSlider.grid(row = row, column = col, rowspan = 1, columnspan = 4, sticky = self.NSEW);


	def __initializeButtonsRow(self, row):
		
		col = 2;
		speechTextBtn = tk.Button(self, text = 'Énoncer', width = self._buttonWidth, height = self._widgetHeight, command = self.__onSpeechTextClick);
		speechTextBtn.grid(row = row, column = col);
				
		col += 1;
		cancelButton = tk.Button(self, text = 'Annuler', width = self._buttonWidth, height = self._widgetHeight, command = self.__onCancelButtonClick);
		cancelButton.grid(row = row, column = col);


	def __onSpeechTextClick(self, *args):
		if self.__speechSubmittedCallback is not None:
			text = self.speechTextEntry.get('1.0', 'end-1c');
			self.__speechSubmittedCallback(text);


	def __onRateSliderChanged(self, *args):
		if self.__rateSliderValueChangedCallback is not None:
			rate = self.textRateSlider.get();
			self.__rateSliderValueChangedCallback(rate);


	def __onPitchSliderChanged(self, *args):
		if self.__pitchSliderValueChangedCallback is not None:
			pitch = self.textPitchSlider.get();
			self.__pitchSliderValueChangedCallback(pitch);


	def __onCancelButtonClick(self, *args):
		if self.__cancelButtonClickedCallback is not None:
			self.__cancelButtonClickedCallback();