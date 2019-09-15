


chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if (request.message == "classify") {

    	const API = new Request('http://127.0.0.1:5000/classify_many', {
			'method': 'POST',
			'headers': {
				'Content-Type': 'application/json'
			},
			'body': JSON.stringify({'texts': request.texts})
		})

		fetch(API)
			.then(function(response) {
				return response.json();
			})
			.then(function(predictions) {
				sendResponse(predictions);
			});

		return true;
    }
  });


function classify(texts) {


	

}
