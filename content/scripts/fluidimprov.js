"use strict";

const MuteImprov = (function() {

	let timeout = null;
	const clearTimeoutIfNeeded = function() {
		if (timeout !== null) {
			clearTimeout(timeout);
		}
	};

	const clearText = function() {
		$('div.frame-text').empty();
	}

	const setTextImmediate = function(text) {
		clearTimeoutIfNeeded();
		clearText();

		const paragraphs = text.split('\n');
		const div = $('div.frame-text')
		paragraphs.forEach(function(paragraph) {
			const pElt = $('<p></p>');
			pElt.text(paragraph);
			div.append(pElt);
		});
	};

	const setTextTimed = function(text, minDelay, maxDelay) {
		clearTimeoutIfNeeded();
		clearText();

		if (maxDelay == null) {
			maxDelay = minDelay;
		}

		if (maxDelay < minDelay) {
			const tmp = minDelay;
			minDelay = maxDelay;
			maxDelay = tmp;
		}

		let rawGroups = text.split('//');
		rawGroups.reverse();

		let groups = [];
		rawGroups.forEach(function(rawGroup) {
			let paragraphs = rawGroup.split('\n');
			paragraphs.reverse();
			groups.push(paragraphs);
		})

		const divElt = $('div.frame-text');
		const scrollBox = $('div.frame-text-scrollbox');

		let currentGroup = groups.pop();
		let currentParagraph = currentGroup.pop();
		let currentParagraphElt = null;
		let charIndex = 0;

		const timeoutFunction = function() {
			
			console.log(currentParagraph);
			if (currentParagraph !== undefined) {

				if (charIndex < currentParagraph.length) {

					if (charIndex == 0) {
						currentParagraphElt = $('<p></p>');
						divElt.append(currentParagraphElt);
					}

					currentParagraphElt.append(currentParagraph[charIndex]);

					charIndex++;
				}
				else {
					currentParagraph = currentGroup.pop();
					charIndex = 0;
				}
			}
			else {
				currentGroup = groups.pop();
				currentParagraph = currentGroup.pop();
				if (currentGroup === undefined) {
					return;
				}

				console.log(currentGroup);
				divElt.empty();
			}

			const r = Math.random();
			const nextDelay = r * minDelay + (1.0 - r ) * maxDelay;
			timeout = setTimeout(timeoutFunction, nextDelay);

			scrollBox.scrollTop(scrollBox[0].scrollHeight);
		};

		timeoutFunction();
	}

	return {
		setTextImmediate: setTextImmediate,
		setTextTimed: setTextTimed
	};

})();