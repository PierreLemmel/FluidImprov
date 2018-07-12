import tkinter as tk;

from fluidpanel import FluidPanel;

class TextPanel(FluidPanel):

	def __init__(self, parent, **options):

		super(FluidPanel, self).__init__(parent, options);

		self.__onTextSizeSliderValueChanged = None;
		self.__onTextFadeTimeSliderValueChanged = None;
		self.__onShowButtonClicked = None;
		self.__onHideButtonClicked = None;

		hWeights = [0, 0, 0, 1];
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
		self.__onTextSizeSliderValueChanged = callback;


	def OnTextFadeTimeSliderValueChangedCallback(self, callback):
		self._funcCheck(callback);
		self.__onTextFadeTimeSliderValueChanged = callback;


	def OnShowButtonClickedCallback(self, callback):
		self._funcCheck(callback);
		self.__onShowButtonClicked = callback;


	def OnHideButtonClickedCallback(self, callback):
		self._funcCheck(callback);
		self.__onHideButtonClicked = callback;


	def __initializeTextAreaRow(self, row):
		col = 0;

		textLabel = tk.Label(self, anchor = tk.E, text = 'Saisissez un texte à afficher :');
		textLabel.grid(row = row, column = col);
		col += 1;

		self.textEntry = tk.Text(self, width = 0);
		self.textEntry.grid(row = row, column = col, rowspan = 1, columnspan = 3);


	def __initializeTextSizeSliderRow(self, row):
		col = 0;

		textSizeLabel = tk.Label(self, anchor = tk.E, text = 'Taille du texte :');
		textSizeLabel.grid(row = row, column = col);
		col += 1;

		self.textSizeSlider = TextSizeSlider(self);
		self.textSizeSlider.grid(row = row, column = col, rowspan = 1, columnspan = 3);


	def __initializeTextFadeTimeSliderRow(self, row):
		pass;


	def __initializeControlButtonsRow(self, row):
		pass;


class TextSizeSlider(FluidPanel):

	def __init__(self, parent, **options):

		self.__command = options.get('command', None);
		if (self.__command and not callable(self.__command)):
			raise ValueError('The input parameter is not a function');

		if ('command' in options):
			del options['command'];

		super(FluidPanel, self).__init__(parent, options);

		self.number = 1.0;
		self.slide = tk.Scale(self, orient = tk.HORIZONTAL, command = self.__setValue, showvalue = 0, fro = 10, to = 100, sliderrelief = tk.RIDGE, resolution = 1);
		self.text = tk.Label(self);

		txt000 = tk.Label(self, text = str(10), anchor = tk.W);
		txt100 = tk.Label(self, text = str(32));
		txt200 = tk.Label(self, text = str(100), anchor = tk.E);
		
		self.text.grid(sticky = self.NSEW, row = 0, column = 0, rowspan = 1, columnspan = 3);
		self.slide.grid(sticky = self.NSEW, row = 1, column = 0, rowspan = 1, columnspan = 3);
		txt000.grid(sticky = self.NSEW, row = 2, column = 0);
		txt100.grid(sticky = self.NSEW, row = 2, column = 1);
		txt200.grid(sticky = self.NSEW, row = 2, column = 2);
		
		self._setupGrid([1, 1, 1], [1, 1, 1]);

		self.slide.set(32);


	def __setValue(self, val):

		nbVal = float(val);

		self.number = nbVal;
		self.text.configure(text = 'Taille du texte : {0}'.format(self.number));

		if (self.__command):
			self.__command(nbVal);


	def get(self):
		return self.number;