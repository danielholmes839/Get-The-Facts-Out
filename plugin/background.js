HOST = '127.0.0.1:5000'

chrome.runtime.onMessage.addListener(
  function(request, sender, sendResponse) {
    if (request.message == "classify/groups") {

    	// Create the request
    	const API = new Request('http://'+HOST+'/classify/groups', {
			'method': 'POST',
			'headers': {
				'Content-Type': 'application/json'
			},
			'body': JSON.stringify({'texts': request.texts})
		})

    	// Make the request to the API and get predictions 
		fetch(API)	
			.then(function(response) {
				return response.json();
			})
			.then(function(predictions) {
				// Send predictions back to content.js
				sendResponse(predictions);
			});

		return true;
    }

    return;
  });
