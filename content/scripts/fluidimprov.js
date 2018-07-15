"use strict";

(function(fluidImprov) {

	fluidImprov.voiceControl = (function(){

		const _speak = function(msg) {

			const utterance = new SpeechSynthesisUtterance(msg);

			utterance.lang = 'fr-FR';
			utterance.pitch = fluidImprov.config.textSpeechPitch;
			utterance.rate = fluidImprov.config.textSpeechRate;

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


	fluidImprov.textControl = (function(){

		const _setTextSize = function(textSize) {
			$('div.fluid-text').css('text-size', textSize + 'px');
		};

		const _fadeInText = function(text) {
			$('div.fluid-text').text(text);
			const fadeTime = fluidImprov.config.textFadeDuration;
			$('div.fluid-fade-container').fadeIn(fadeTime);
		};

		const _fadeOutText = function() {
			const fadeTime = fluidImprov.config.textFadeDuration;
			$('div.fluid-fade-container').fadeOut(fadeTime);
		};

		return {
			setTextSize: _setTextSize,
			fadeInText: _fadeInText,
			fadeOutText: _fadeOutText
		};

	})();


	fluidImprov.videoControl = (function(){

		const _playVideo = function() {
			const video = $('video.fullscreen-video')[0];
			video.play();
		};

		const _stopVideo = function() {
			const video = $('video.fullscreen-video')[0];
			video.pause();
			video.currentTime = 0;
		};

		return {
			playVideo: _playVideo,
			stopVideo: _stopVideo
		};

	})();

})(window.fluidImprov = window.fluidImprov || {});