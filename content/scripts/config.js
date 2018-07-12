"use strict";

(function(fluidImprov) {

	let _textRate = 1.0;
	let _textPitch = 1.0;

	fluidImprov.config = {};

	Object.defineProperty(fluidImprov.config, 'textRate', {
		get() { return _textRate; },
		set(value) {
			if (value >= 0.1 && value <= 10.0) {
				_textRate = value;
			}
			else {
				throw "Invalid textRate!";
			}
		}
	});

	Object.defineProperty(fluidImprov.config, 'textPitch', {
		get() { return _textPitch; },
		set(value) {
			if (value >= 0.0 && value <= 2.0) {
				_textPitch = value;
			}
			else {
				throw "Invalid textPitch!";
			}
		}
	});

})(window.fluidImprov = window.fluidImprov || {});