import tkinter as tk;
import tkinter.ttk as ttk;

from fluidpanel import FluidPanel;

from os import listdir, getcwd;
from os.path import isfile, join, splitext;

class FluidFolderCombobox(FluidPanel):

	def __init__(self, parent, **options):

		self.__folder = self._retrieveParam(options, 'folder');
		self.__extension = self._retrieveParam(options, 'extension');

		self.__command = self._retrieveParam(options, 'command');
		if (self.__command and not callable(self.__command)):
			raise ValueError('The input parameter is not a function');

		super(FluidPanel, self).__init__(parent, options);

		self.__values = self.__initValuesFromFiles();

		self.__combo = ttk.Combobox(self, state = 'readonly', values = self.__values);
		self.__combo.bind('<<ComboboxSelected>>', self.__fireValueChangedEvent);

		self.__combo.pack(fill=tk.BOTH, expand=1);


	def __initValuesFromFiles(self):
		contentPath = self.__getContentPath();
		fullPath = join(contentPath, self.__folder);
		values = [splitext(file)[0] for file in listdir(fullPath) if (isfile(join(fullPath, file)) and splitext(file)[1] == self.__extension)];

		return values;


	def __fullPathFromName(self, fileName):
		contentPath = self.__getContentPath();
		fullFileName = fileName + self.__extension;
		fullPath = join(contentPath, self.__folder, fullFileName);

		return fullPath;


	def __fireValueChangedEvent(self, *args):
		if self.__command:
			value = self.get();
			self.__command(value);


	def __getContentPath(self):
		basePath = getcwd();
		contentPath = join(basePath, '..\content');

		return contentPath;


	def get(self):
		value = self.__combo.get();
		return value;


	def getFullValue(self):
		fullValue = self.__fullPathFromName(self.get());
		return fullValue;