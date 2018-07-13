import tkinter as tk;

from fluidpanel import FluidPanel;

class MusicPanel(FluidPanel):

	def __init__(self, parent, **options):
		super(FluidPanel, self).__init__(parent, options);

		self.__onPlayButtonClickedCallback = None;
		self.__onPauseButtonClickedCallback = None;

		hWeights = [1, 0, 0, 1];
		vWeights = [1, 0, 1];

		row = 0;
		self.__initializePlaceHolderRow(row);
		row += 1;
		self.__initializeButtonsRow(row);
		row += 1;
		self.__initializePlaceHolderRow(row);

		self._setupGrid(hWeights, vWeights);
		self._setControlsPadding(self._childPaddingX, self._childPaddingY);


	def OnPlayButtonClickedCallback(self, callback):
		self._funcCheck(callback);
		self.__onPlayButtonClickedCallback = callback;


	def OnPauseButtonClickedCallback(self, callback):
		self._funcCheck(callback);
		self.__onPauseButtonClickedCallback = callback;


	def __initializeButtonsRow(self, row):

		col = 1;
		playButton = tk.Button(self, text = 'Jouer', width = self._buttonWidth, height = self._widgetHeight, command = self.__onPlayButtonClicked);
		playButton.grid(row = row, column = col);

		col += 1;
		pauseButton = tk.Button(self, text = 'Arrêter', width = self._buttonWidth, height = self._widgetHeight, command = self.__onPauseButtonClicked);
		pauseButton.grid(row = row, column = col);


	def __initializePlaceHolderRow(self, row):

		placeHolder = tk.Frame(self);
		placeHolder.grid(row = row, column = 0, rowspan = 1, columnspan = 3, sticky = self.NSEW);


	def __onPlayButtonClicked(self, *args):
		print('__onPlayButtonClicked');
		if self.__onPlayButtonClickedCallback is not None:
			self.__onPlayButtonClickedCallback();


	def __onPauseButtonClicked(self, *args):
		print('__onPauseButtonClicked');
		if self.__onPauseButtonClickedCallback is not None:
			self.__onPauseButtonClickedCallback();