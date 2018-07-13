print('Launching FluidImprov');

import os;

from tkinter import *;
from pathlib import Path;
from mainpanel import MainPanel;
from automating import Controller;


print('Starting selenium controller');

controller = Controller();
controller.OpenBrowser();

print('selenium controller started');


title = "Les Écorcés - Fluide";
dimension = "1000x600";

tk = Tk();
tk.title(title);
tk.geometry(dimension);

window = MainPanel(tk);
window.pack(side = TOP, fill = BOTH, expand = True);


window.speechPanel.OnSpeechSubmittedCallback(lambda text: controller.VoiceSpeak(text));
window.speechPanel.OnRateSliderValueChangedCallback(lambda rate: controller.SetTextSpeechRate(rate));
window.speechPanel.OnPitchSliderValueChangedCallback(lambda pitch: controller.SetTextSpeechPitch(pitch));
window.speechPanel.OnCancelButtonClickedCallback(lambda: controller.VoiceCancel());

tk.mainloop();


print('Exiting program');