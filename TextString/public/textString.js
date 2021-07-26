module.exports = function() {
	var express = require('express');
	var router = express.Router();
	//  Default page
	router.get('/', function(req, res) {
		var context = {};
		context.results = "Press button to generate string";
		res.render('index', context);
	});


	//  GET route to output text on screen and in response body
	router.get('/get-string',function(req,res){
	  var context = {};
	  var stringNum = Math.random(0,textStrings.length);
	  context.results = textStrings[stringNum];
	  console.log(context.results);
	  res.render('index', context);
	});


	var textStrings = [ "Take out trash", "Walk the dog",
					"Do homework", "Read a book", "Brush Teeth",
					
					
					];

	function generateText() {
		var req = new XMLHttpRequest();
		req.open("GET", "/get-string", true);
		req.addEventListener("load", function() {
			if (req.status >= 200 && req.status < 400) {
				console.log("Successful request.");
			} else {
				console.log("Error in request.");
			}
		});
		req.send();
		event.preventDefault();
	}
	
	return router;
}();