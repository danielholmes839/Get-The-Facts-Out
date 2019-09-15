chrome.runtime.onMessage.addListener(function (message, sender, sendResponse) {
	console.log('received message:', message)
	if (message === 'highlight') {
		main();
	} 	
});

function main() {
	// Get paragraphs
	var paragraphs = document.getElementsByTagName('p', 'span');
	var paragraphs_text = [];

	for (let paragraph of paragraphs) {
		paragraphs_text.push(paragraph.textContent);
	}

	chrome.runtime.sendMessage({
		'texts': paragraphs_text,
		'message': 'classify'
	}, function(response) {
		console.log(response);
		highlight(paragraphs, response.predictions);
	})
}

function mark(text) {
	let mark = document.createElement('mark');
	mark.innerHTML = text;
	mark.style.cssText = "color: black; background: yellow";
	return mark.outerHTML;
}

function highlight(paragraphs, predictions) {

	for (let i=0; i<paragraphs.length; i++) {

		// Process each paragraph
		let values = predictions[i].predictions;
		let sentences = predictions[i].sentences;
		let paragraph = paragraphs[i];
		paragraph.innerHTML = paragraph.textContent;

		// Process each sentence	
		for (let j=0; j<sentences.length; j++) {

			prediction = values[j];
			sentence = sentences[j];

			// If it's objective highlight
			if (prediction === 1) {
				let prev = paragraph.innerHTML;
				paragraph.innerHTML = paragraph.innerHTML.replace(sentence, mark(sentence));
				let after = paragraph.innerHTML;

				if (prev === after) {console.log('COULD NOT FIND:', sentence)}
			}
		}	
	}
}