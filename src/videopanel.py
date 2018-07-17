import tkinter as tk;

from fluidpanel import FluidPanel;
from fluidslider import FluidSlider;
from fluidfoldercombobox import FluidFolderCombobox;

class VideoPanel(FluidPanel):

	def __init__(self, parent, **options):
		super(FluidPanel, self).__init__(parent, options);

		self.__onVideoSourceChangedCallback = None;
		self.__onFadeDurationSliderValueChangedCallback = None;
		self.__onPlayButtonClickedCallback = None;
		self.__onPauseButtonClickedCallback = None;

		hWeights = [0, 1, 0, 0, 1];
		vWeights = [1, 0, 0, 0, 1];

		row = 0;
		self.__initializePlaceHolderRow(row);
		row += 1;
		self.__initializeSourceCombobox(row);
		row += 1;
		self.__initializeFadeDurationSlider(row);
		row += 1;
		self.__initializeButtonsRow(row);
		row += 1;
		self.__initializePlaceHolderRow(row);

		self._setupGrid(hWeights, vWeights);
		self._setControlsPadding(self._childPaddingX, self._childPaddingY);


	def OnVideoSourceChangedCallback(self, callback):
		self._funcCheck(callback);
		self.__onVideoSourceChangedCallback = callback;


	def OnFadeDurationSliderValueChangedCallback(self, callback):
		self._funcCheck(callback);
		self.__onFadeDurationSliderValueChangedCallback = callback;


	def OnPlayButtonClickedCallback(self, callback):
		self._funcCheck(callback);
		self.__onPlayButtonClickedCallback = callback;


	def OnPauseButtonClickedCallback(self, callback):
		self._funcCheck(callback);
		self.__onPauseButtonClickedCallback = callback;


	def __initializeSourceCombobox(self, row):
		col = 0;

		sourceLabel = tk.Label(self, anchor = tk.E, text = 'Source :');
		sourceLabel.grid(row = row, column = col);
		col += 1;

		self.sourceCombo = FluidFolderCombobox(self, command = self.__onSourceValueChanged, folder = 'videos', extension = '.mp4');
		self.sourceCombo.grid(row = row, column = col, rowspan = 1, columnspan = 4, sticky = self.NSEW);


	def __initializeFadeDurationSlider(self, row):

		col = 0;
		fadeDurationLabel = tk.Label(self, anchor = tk.E, text = 'Transition de la vidéo :');
		fadeDurationLabel.grid(row = row, column = col);
		
		col += 1;
		self.fadeDurationSlider = FluidSlider(self, command = self.__onFadeDurationSliderValueChanged, minValue = 0, initialValue = 2500, maxValue = 4000,
											valueFormat = 'Transition : {0:0g} ms', labelFormat = '{0:0g}');
		self.fadeDurationSlider.grid(row = row, column = col, rowspan = 1, columnspan = 4, sticky = self.NSEW);



	def __initializeButtonsRow(self, row):

		col = 2;
		playButton = tk.Button(self, text = 'Afficher', width = self._buttonWidth, height = self._widgetHeight, command = self.__onPlayButtonClicked);
		playButton.grid(row = row, column = col);

		col += 1;
		pauseButton = tk.Button(self, text = 'Arrêter', width = self._buttonWidth, height = self._widgetHeight, command = self.__onPauseButtonClicked);
		pauseButton.grid(row = row, column = col);


	def __initializePlaceHolderRow(self, row):

		placeHolder = tk.Frame(self);
		placeHolder.grid(row = row, column = 0, rowspan = 1, columnspan = 3, sticky = self.NSEW);


	def __onSourceValueChanged(self, *args):
		if self.__onVideoSourceChangedCallback is not None:
			source = self.sourceCombo.get();
			self.__onVideoSourceChangedCallback(source);


	def __onFadeDurationSliderValueChanged(self, *args):
		if self.__onFadeDurationSliderValueChangedCallback is not None:
			fadeTime = self.fadeDurationSlider.get();
			self.__onFadeDurationSliderValueChangedCallback(fadeTime);


	def __onPlayButtonClicked(self, *args):
		if self.__onPlayButtonClickedCallback is not None:
			self.__onPlayButtonClickedCallback();


	def __onPauseButtonClicked(self, *args):
		if self.__onPauseButtonClickedCallback is not None:
			self.__onPauseButtonClickedCallback();