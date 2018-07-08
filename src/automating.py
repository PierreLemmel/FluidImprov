import os;
import unidecode;
from sys import platform;
from selenium import webdriver;
from selenium.webdriver.common.by import By;

class Controller:

	def __init__(self):
		pathToDriver = self.__getPathToDriver();

		print(pathToDriver);
		self.driver = webdriver.Chrome(pathToDriver);
		self.urlForIndex = self.__getUrlForIndex();


	def OpenBrowser(self):
		self.driver.get(self.urlForIndex);


	def __escapeText(self, text):
		escapedText = text.replace('"', '\\"');
		escapedText = escapedText.replace('\n', '\\n');
		escapedText = unidecode.unidecode(escapedText);

		return escapedText;


	def __execScript(self, script):
		print('Executing script: {0}'.format(script));
		self.driver.execute_script(script);


	def __navigateToIndexIfNeeded(self):
		self.__checkForUrl(self.urlForIndex);


	def __checkForUrl(self, url):
		currentFileName = self.driver.current_url.split('/')[-1];
		requiredFileName = url.split('\\')[-1];
		if (currentFileName != requiredFileName):
			self.driver.get(url);


	def __getUrlForIndex(self):
		basePath = os.getcwd();
		path = os.path.join(basePath, '..\content', 'index.html');
		return path;


	def __getPathToDriver(self):
		osFolder = None;
		driver = None;
		if platform == "linux" or platform == "linux2":
			osFolder = "linux";
			driver = "chromedriver";
		elif platform == "win32":
			osFolder = "windows";
			driver = "chromedriver.exe";

		if osFolder is None:
			raise ValueError('Unexpected platform: %s' % platform);

		basePath = os.getcwd();
		path = os.path.join(basePath, '..\drivers', osFolder, driver);

		return path;