//  Send request to teammember's microservice, which generates a random hex color.
// http://flip3.engr.oregonstate.edu:5414
/*
    SETUP
*/
//var express = require('express');   // We are using the express library for the web server
//var app     = express();            // We need to instantiate an express object to interact with the server in our code
//app.use(express.json())
//app.use(express.urlencoded({extended: true}))

var XMLHttpRequest = require("xmlhttprequest").XMLHttpRequest;

// ROUTE

function grabColor() {
	var req = new XMLHttpRequest();
	var URL = "https://flip3.engr.oregonstate.edu:5414";
	req.open('GET', URL, true);
	// req.setRequestHeader('Content-Type', 'application/json');
	req.addEventListener('load', function() 
		{
			if (req.status >= 200 && req.status < 400) {
				var response = JSON.parse(req.responseText);
				console.log(response);
				console.log('response status OK');
			} else {
				console.log('error in request');
			}
		});
	req.send();
	console.log('request sent');
}

grabColor();

		// Send the results to the browser
        // res.send(JSON.stringify(results));