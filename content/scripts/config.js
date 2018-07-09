"use strict";

(function(fluidImprov) {

	let _rate = 1.0;
	let _pitch = 1.0;

	fluidImprov.config = {};

	Object.defineProperty(fluidImprov.config, 'rate', {
		get() { return _rate; },
		set(value) {
			if (value >= 0.1 && value <= 10.0) {
				_rate = value;
			}
			else {
				throw "Invalid rate!";
			}
		}
	});

	Object.defineProperty(fluidImprov.config, 'pitch', {
		get() { return _pitch; },
		set(value) {
			if (value >= 0.0 && value <= 2.0) {
				_pitch = value;
			}
			else {
				throw "Invalid pitch!";
			}
		}
	});

})(window.fluidImprov = window.fluidImprov || {});