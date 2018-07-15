import os;

from sys import platform;
from selenium import webdriver;
from selenium.webdriver.common.by import By;

class Controller:

	def __init__(self):
		pathToDriver = self.__getPathToDriver();

		print(pathToDriver);
		self.driver = webdriver.Chrome(pathToDriver);
		self.urlForIndex = self._getUrlForIndex();


	def OpenBrowser(self):
		self.driver.get(self.urlForIndex);



	#########################
	# 		Text speech		#
	#########################
	def VoiceSpeak(self, text):
		self._navigateToIndexIfNeeded();
		escapedText = self.__escapeText(text);
		script = 'fluidImprov.voiceControl.speak("{0}");'.format(escapedText);
		self._execScript(script);


	def VoiceCancel(self):
		self._navigateToIndexIfNeeded();
		script = 'fluidImprov.voiceControl.cancel()';
		self._execScript(script);


	def SetTextSpeechRate(self, rate):
		self._navigateToIndexIfNeeded();
		script = 'fluidImprov.config.textSpeechRate = {0};'.format(rate);
		self._execScript(script);


	def SetTextSpeechPitch(self, pitch):
		self._navigateToIndexIfNeeded();
		script = 'fluidImprov.config.textSpeechPitch = {0};'.format(pitch);
		self._execScript(script);



	#########################
	# 		Text panel		#
	#########################
	def SetTextSize(self, size):
		self._navigateToIndexIfNeeded();
		script = 'fluidImprov.textControl.setTextSize({0});'.format(size);
		self._execScript(script);


	def SetTextFadeDuration(self, fadeDuration):
		self._navigateToIndexIfNeeded();
		script = 'fluidImprov.config.textFadeDuration = {0};'.format(fadeDuration);
		self._execScript(script);


	def FadeInText(self, text):
		self._navigateToIndexIfNeeded();
		escapedText = self.__escapeText(text);
		script = 'fluidImprov.textControl.fadeInText()';
		self._execScript(script);


	def FadeOutText(self):
		self._navigateToIndexIfNeeded();
		script = 'fluidImprov.textControl.fadeOutText()';
		self._execScript(script);



	#########################
	# 		Vidéo panel		#
	#########################
	def PlayVideo(self):
		self._navigateToIndexIfNeeded();
		script = 'fluidImprov.videoControl.playVideo()';
		self._execScript(script);


	def StopVideo(self):
		self._navigateToIndexIfNeeded();
		script = 'fluidImprov.videoControl.stopVideo()';
		self._execScript(script);



	#########################
	# 		Privates		#
	#########################
	def __escapeText(self, text):
		escapedText = text.replace('"', '\\"');
		escapedText = escapedText.replace('\n', '\\n');

		return escapedText;


	def _execScript(self, script):
		print('Executing script: {0}'.format(script));
		self.driver.execute_script(script);


	def _navigateToIndexIfNeeded(self):
		self._checkForUrl(self.urlForIndex);


	def _checkForUrl(self, url):
		currentFileName = self.driver.current_url.split('/')[-1];
		requiredFileName = url.split('\\')[-1];
		if (currentFileName != requiredFileName):
			self.driver.get(url);


	def _getUrlForIndex(self):
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