import tkinter as tk;

from fluidpanel import FluidPanel;

from videopanel import VideoPanel;
from textpanel import TextPanel;
from speechpanel import SpeechPanel;
from musicpanel import MusicPanel;


class MainPanel(FluidPanel):

	__labelsFont = ("Helvetica", 12);

	def __init__(self, parent, **options):

		super(FluidPanel, self).__init__(parent, options);
		
		mainPane = tk.PanedWindow(self, orient = tk.HORIZONTAL);


		leftPane = tk.PanedWindow(mainPane, orient = tk.VERTICAL);

		topLeftPanel = tk.Frame(leftPane);
		self.__initializeTopLeftPanel(topLeftPanel);
		leftPane.add(topLeftPanel, stretch = "always");

		bottomLeftPanel = tk.Frame(leftPane);
		self.__initializeBottomLeftPanel(bottomLeftPanel);
		leftPane.add(bottomLeftPanel, stretch = "always");

		mainPane.add(leftPane, stretch = "always");


		rightPane = tk.PanedWindow(mainPane, orient = tk.VERTICAL);

		topRightPanel = tk.Frame(rightPane);
		self.__initializeTopRightPanel(topRightPanel);
		rightPane.add(topRightPanel, stretch = "always");

		bottomRightPanel = tk.Frame(rightPane);
		self.__initializeBottomRightPanel(bottomRightPanel);
		rightPane.add(bottomRightPanel, stretch = "always");
		
		mainPane.add(rightPane, stretch = "always");


		mainPane.pack(fill = tk.BOTH, expand = 1);


	def __initializeTopLeftPanel(self, topLeftPanel):

		videoLabel = tk.Label(topLeftPanel, text = 'Vidéo', font = self.__labelsFont);
		videoLabel.pack(side = tk.TOP, fill = tk.X);

		self.videoPanel = VideoPanel(topLeftPanel);
		self.videoPanel.pack(side = tk.BOTTOM, fill = tk.BOTH, expand = 1);


	def __initializeBottomLeftPanel(self, bottomLeftPanel):

		speechLabel = tk.Label(bottomLeftPanel, text = 'Voix', font = self.__labelsFont);
		speechLabel.pack(side = tk.TOP, fill = tk.X);

		self.speechPanel = SpeechPanel(bottomLeftPanel);
		self.speechPanel.pack(side = tk.BOTTOM, fill = tk.BOTH, expand = 1);


	def __initializeTopRightPanel(self, topRightPanel):

		textLabel = tk.Label(topRightPanel, text = 'Texte', font = self.__labelsFont);
		textLabel.pack(side = tk.TOP, fill = tk.X);

		self.textPanel = TextPanel(topRightPanel);
		self.textPanel.pack(side = tk.BOTTOM, fill = tk.BOTH, expand = 1);


	def __initializeBottomRightPanel(self, bottomRightPanel):

		musicLabel = tk.Label(bottomRightPanel, text = 'Musique', font = self.__labelsFont);
		musicLabel.pack(side = tk.TOP, fill = tk.X);

		self.musicPanel = MusicPanel(bottomRightPanel);
		self.musicPanel.pack(side = tk.BOTTOM, fill = tk.BOTH, expand = 1);