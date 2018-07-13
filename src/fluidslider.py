import tkinter as tk;

from fluidpanel import FluidPanel;

class FluidSlider(FluidPanel):

	def __init__(self, parent, **options):

		self.__command = self._retrieveParam(options, 'command');
		if (self.__command and not callable(self.__command)):
			raise ValueError('The input parameter is not a function');

		minValue = self._retrieveParam(options, 'minValue', 0);
		initialValue = self._retrieveParam(options, 'initialValue', 50);
		maxValue = self._retrieveParam(options, 'maxValue', 100);
		resolution = self._retrieveParam(options, 'resolution', 1);

		self.__valueFormat = self._retrieveParam(options, 'valueFormat', '{0}');
		self.__valueTransform = self._retrieveParam(options, 'valueTransform', lambda v: v);

		self.__labelFormat = self._retrieveParam(options, 'labelFormat', '{0}');

		labelLeft = self.__labelText(minValue);
		labelCenter = self.__labelText((minValue + maxValue) / 2.0);
		labelRight = self.__labelText(maxValue);
		
		super(FluidPanel, self).__init__(parent, options);

		self.slide = tk.Scale(self, orient = tk.HORIZONTAL, command = self.__setValue, showvalue = 0,
							fro = minValue, to = maxValue, sliderrelief = tk.RIDGE, resolution = resolution);
		self.text = tk.Label(self);

		txt000 = tk.Label(self, text = labelLeft, anchor = tk.W);
		txt100 = tk.Label(self, text = labelCenter);
		txt200 = tk.Label(self, text = labelRight, anchor = tk.E);
		
		self.text.grid(sticky = self.NSEW, row = 0, column = 0, rowspan = 1, columnspan = 3);
		self.slide.grid(sticky = self.NSEW, row = 1, column = 0, rowspan = 1, columnspan = 3);
		txt000.grid(sticky = self.NSEW, row = 2, column = 0);
		txt100.grid(sticky = self.NSEW, row = 2, column = 1);
		txt200.grid(sticky = self.NSEW, row = 2, column = 2);
		
		self._setupGrid([1, 1, 1], [1, 1, 1]);

		self.__number = initialValue;
		self.slide.set(initialValue);


	def __setValue(self, val):

		nbVal = float(val);

		self.__number = self.__valueTransform(nbVal);
		self.text.configure(text = self.__valueFormat.format(self.__number));

		if (self.__command):
			self.__command(nbVal);
			

	def __labelText(self, val):

		fltVal = float(val);
		
		transformedValue = self.__valueTransform(fltVal);
		return self.__labelFormat.format(transformedValue);


	def get(self):
		return self.__number;


	def _retrieveParam(self, options, key, default = None):
		value = options.get(key, default);

		if (key in options):
			del options[key];

		return value;