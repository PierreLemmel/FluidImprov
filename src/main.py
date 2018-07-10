print('Launching FluidImprov');

import os;

from tkinter import *;
from pathlib import Path;
from gui import MainWindow;
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

window = MainWindow(tk);
window.pack(side = TOP, fill = BOTH, expand = True);


window.OnSpeechSubmittedCallback(lambda text: controller.VoiceSpeak(text));
window.OnRateSliderValueChangedCallback(lambda rate: controller.SetTextRate(rate));
window.OnPitchSliderValueChangedCallback(lambda pitch: controller.SetTextPitch(pitch));
window.OnCancelButtonClickedCallback(lambda: controller.VoiceCancel());

tk.mainloop();


print('Exiting program');