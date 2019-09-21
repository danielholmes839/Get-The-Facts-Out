document.addEventListener('DOMContentLoaded', function () {
	// When content is loaded
  	document.getElementById('highlight-btn').addEventListener('click', on_click, false);

    // Tell the page to highlight
  	function on_click() {
  		chrome.tabs.query({currentWindow: true, active: true}, function(tabs) {
  			chrome.tabs.sendMessage(tabs[0].id, 'highlight');
  		});
	}
	
}, false);