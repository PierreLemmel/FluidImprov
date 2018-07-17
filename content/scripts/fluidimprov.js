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

		const _getVideo = function() {
			return _getVideoElt()[0];
		};

		const _getVideoElt = function() {
			return $('video.fullscreen-video');
		};

		const _getBackground = function() {
			return $('div.fullscreen-video-background');
		};

		const _playVideo = function() {

			const background = _getBackground();
			background.fadeIn(fluidImprov.config.videoFadeDuration);

			const video = _getVideo();
			video.play();
		};

		const _stopVideo = function() {

			const background = _getBackground();
			background.fadeOut(fluidImprov.config.videoFadeDuration);

			const video = _getVideo();
			video.pause();
			video.currentTime = 0;
		};

		const _setVideoSource = function(file) {

			const source = _getVideoElt().find('source');

			const filePath = 'videos/' + file + '.mp4';
			source.attr('src', filePath);

			const video = _getVideo();
			video.load();
		}

		return {
			playVideo: _playVideo,
			stopVideo: _stopVideo,
			setVideoSource: _setVideoSource
		};

	})();


	fluidImprov.audioControl = (function() {
		
		const _getAudio = function() {
			return $('audio.fluid-audio')[0];
		};

		const _playAudio = function() {
			const audio = _getAudio();
			audio.play();
		};

		const _stopAudio = function() {
			const audio = _getAudio();
			audio.pause();
			audio.currentTime = 0;
		};

		const _setAudioSource = function(file) {
			const source = $('audio.fluid-audio source');

			const filePath = 'audios/' + file + '.mp3';
			source.attr('src', filePath);

			const audio = _getAudio();
			audio.load();
		};

		return {
			playAudio: _playAudio,
			stopAudio: _stopAudio,
			setAudioSource: _setAudioSource
		};

	})();

})(window.fluidImprov = window.fluidImprov || {});