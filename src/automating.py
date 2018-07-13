import os;

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


	def VoiceSpeak(self, text):
		self.__navigateToIndexIfNeeded();

		escapedText = self.__escapeText(text);
		script = 'fluidImprov.voiceControl.speak("{0}");'.format(escapedText);

		self.__execScript(script);


	def VoiceCancel(self):
		self.__navigateToIndexIfNeeded();

		script = 'fluidImprov.voiceControl.cancel()';

		self.__execScript(script);


	def SetTextSpeechRate(self, rate):
		self.__navigateToIndexIfNeeded();
		script = 'fluidImprov.config.textSpeechRate = {0}'.format(rate);
		self.__execScript(script);


	def SetTextSpeechPitch(self, pitch):
		self.__navigateToIndexIfNeeded();
		script = 'fluidImprov.config.textSpeechPitch = {0}'.format(pitch);
		self.__execScript(script);


	def SetTextSize(self, size):
		self.__navigateToIndexIfNeeded();
		script = 'fluidImprov.config.textSize = {0}'.format(size);
		self.__execScript(script);


	def SetTextFadeDuration(self, fadeDuration):
		self.__navigateToIndexIfNeeded();
		script = 'fluidImprov.config.textFadeDuration = {0}'.format(fadeDuration);
		self.__execScript(script);


	def __escapeText(self, text):
		escapedText = text.replace('"', '\\"');
		escapedText = escapedText.replace('\n', '\\n');

		return escapedText;


	def __execScript(self, script):
		#print('Executing script: {0}'.format(script));
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