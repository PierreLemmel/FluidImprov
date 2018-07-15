import tkinter as tk;

from fluidpanel import FluidPanel;
from fluidslider import FluidSlider;

class TextPanel(FluidPanel):

	def __init__(self, parent, **options):

		super(FluidPanel, self).__init__(parent, options);

		self.__onTextSizeSliderValueChangedCallback = None;
		self.__onFadeTimeSliderValueChangedCallback = None;
		self.__onShowButtonClickedCallback = None;
		self.__onHideButtonClickedCallback = None;

		hWeights = [0, 1, 0, 0, 1];
		vWeights = [1, 0, 0, 0];

		row = 0;
		self.__initializeTextAreaRow(row);
		row += 1;
		self.__initializeTextSizeSliderRow(row);
		row += 1;
		self.__initializeTextFadeTimeSliderRow(row);
		row += 1;
		self.__initializeControlButtonsRow(row);

		self._setupGrid(hWeights, vWeights);
		self._setControlsPadding(self._childPaddingX, self._childPaddingY);


	def OnTextSizeSliderValueChangedCallback(self, callback):
		self._funcCheck(callback);
		self.__onTextSizeSliderValueChangedCallback = callback;


	def OnTextFadeTimeSliderValueChangedCallback(self, callback):
		self._funcCheck(callback);
		self.__onFadeTimeSliderValueChangedCallback = callback;


	def OnShowButtonClickedCallback(self, callback):
		self._funcCheck(callback);
		self.__onShowButtonClickedCallback = callback;


	def OnHideButtonClickedCallback(self, callback):
		self._funcCheck(callback);
		self.__onHideButtonClickedCallback = callback;


	def __initializeTextAreaRow(self, row):
		col = 0;

		textLabel = tk.Label(self, anchor = tk.E, text = 'Saisissez un texte à afficher :');
		textLabel.grid(row = row, column = col);
		col += 1;

		self.textEntry = tk.Text(self, width = 0);
		self.textEntry.grid(row = row, column = col, rowspan = 1, columnspan = 4, sticky = self.NSEW);


	def __initializeTextSizeSliderRow(self, row):
		col = 0;

		textSizeLabel = tk.Label(self, anchor = tk.E, text = 'Taille du texte :');
		textSizeLabel.grid(row = row, column = col);
		col += 1;

		self.textSizeSlider = FluidSlider(self, minValue = 100, maxValue = 400, initialValue = 300, 
										valueFormat = 'Taille du texte : {0:0g}', labelFormat = '{0:0g}', command = self.__onTextSizeSliderValueChanged);
		self.textSizeSlider.grid(row = row, column = col, rowspan = 1, columnspan = 4, sticky = self.NSEW);


	def __initializeTextFadeTimeSliderRow(self, row):
		col = 0;

		textSizeLabel = tk.Label(self, anchor = tk.E, text = 'Transition du texte :');
		textSizeLabel.grid(row = row, column = col);
		col += 1;

		self.fadeTimeSlider = FluidSlider(self, minValue = 0, maxValue = 2000, initialValue = 400, resolution = 50,
										valueFormat = 'Transition : {0:0g} ms', labelFormat = '{0:0g} ms', command = self.__onFadeTimeSliderValueChanged);
		self.fadeTimeSlider.grid(row = row, column = col, rowspan = 1, columnspan = 4, sticky = self.NSEW);


	def __initializeControlButtonsRow(self, row):
		col = 2;

		showButton = tk.Button(self, text = 'Afficher', width = self._buttonWidth, height = self._widgetHeight, command = self.__onShowButtonClicked);
		showButton.grid(row = row, column = col);
		col += 1;

		cancelButton = tk.Button(self, text = 'Cacher', width = self._buttonWidth, height = self._widgetHeight, command = self.__onHideButtonClicked);
		cancelButton.grid(row = row, column = col);


	def __onTextSizeSliderValueChanged(self, *args):
		if self.__onTextSizeSliderValueChangedCallback is not None:
			textSize = self.textSizeSlider.get();
			self.__onTextSizeSliderValueChangedCallback(textSize);


	def __onFadeTimeSliderValueChanged(self, *args):
		if self.__onFadeTimeSliderValueChangedCallback is not None:
			fadeTime = self.fadeTimeSlider.get();
			self.__onFadeTimeSliderValueChangedCallback(fadeTime);


	def __onShowButtonClicked(self, *args):
		if self.__onShowButtonClickedCallback is not None:
			text = self.textEntry.get('1.0', 'end-1c');
			self.__onShowButtonClickedCallback(text);


	def __onHideButtonClicked(self, *args):
		if self.__onHideButtonClickedCallback is not None:
			self.__onHideButtonClickedCallback();