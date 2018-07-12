"use strict";

(function(fluidImprov) {

	fluidImprov.voiceControl = (function(){

		const _speak = function(msg) {

			const utterance = new SpeechSynthesisUtterance(msg);

			utterance.lang = 'fr-FR';
			utterance.pitch = fluidImprov.config.textPitch;
			utterance.rate = fluidImprov.config.textRate;

			window.speechSynthesis.speak(utterance);
		};

		const _cancel = function() {
			window.speechSynthesis.cancel();
		};

		return {
			speak: _speak,
			cancel: _cancel
		};

	})();

})(window.fluidImprov = window.fluidImprov || {});