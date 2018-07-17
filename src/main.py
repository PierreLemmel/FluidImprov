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


window.textPanel.OnTextSizeSliderValueChangedCallback(lambda textSize: controller.SetTextSize(textSize));
window.textPanel.OnTextFadeTimeSliderValueChangedCallback(lambda fadeDuration: controller.SetTextFadeDuration(fadeDuration));
window.textPanel.OnShowButtonClickedCallback(lambda text: controller.FadeInText(text));
window.textPanel.OnHideButtonClickedCallback(lambda: controller.FadeOutText());


window.videoPanel.OnPlayButtonClickedCallback(lambda: controller.PlayVideo());
window.videoPanel.OnPauseButtonClickedCallback(lambda: controller.StopVideo());
window.videoPanel.OnVideoSourceChangedCallback(lambda source: controller.SetVideoSource(source));
window.videoPanel.OnFadeDurationSliderValueChangedCallback(lambda fadeDuration: controller.SetVideoFadeDuration(fadeDuration));


window.musicPanel.OnPlayButtonClickedCallback(lambda: controller.PlayAudio());
window.musicPanel.OnPauseButtonClickedCallback(lambda: controller.StopAudio());
window.musicPanel.OnAudioSourceChangedCallback(lambda source: controller.SetAudioSource(source));


tk.mainloop();
tk.quit();


print('Exiting program');