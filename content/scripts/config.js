"use strict";

(function(fluidImprov) {

	let _textSpeechRate = 1.0;
	let _textSpeechPitch = 1.0;

	let _textFadeDuration = 400;

	let _videoFadeDuration = 2500;

	fluidImprov.config = {};

	Object.defineProperty(fluidImprov.config, 'textSpeechRate', {
		get() { return _textSpeechRate; },
		set(value) {
			if (value >= 0.1 && value <= 10.0) {
				_textSpeechRate = value;
			}
			else {
				throw "Invalid textSpeechRate!";
			}
		}
	});

	Object.defineProperty(fluidImprov.config, 'textSpeechPitch', {
		get() { return _textSpeechPitch; },
		set(value) {
			if (value >= 0.0 && value <= 2.0) {
				_textSpeechPitch = value;
			}
			else {
				throw "Invalid textSpeechPitch!";
			}
		}
	});

	Object.defineProperty(fluidImprov.config, 'textFadeDuration', {
		get() { return _textFadeDuration; },
		set(value) {
			if (value >= 0.0 && value <= 2000.0) {
				_textFadeDuration = value;
			}
			else {
				throw "Invalid textFadeDuration!";
			}
		}
	});

	Object.defineProperty(fluidImprov.config, 'videoFadeDuration', {
		get() { return _videoFadeDuration; },
		set(value) {
			if (value >= 0.0 && value <= 4000.0) {
				_videoFadeDuration = value;
			}
			else {
				throw "Invalid videoFadeDuration!";
			}
		}
	});

})(window.fluidImprov = window.fluidImprov || {});