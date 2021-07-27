module.exports = function() {
	var express = require('express');
	var router = express.Router();



	//  GET route to output text on screen and in response body
	router.get('/',function(req,res){
	  var context = {};
	  var stringNum = getRandomInt(0,textStrings.length);
	  //  console.log("stringNum: ", stringNum);
	  context.results = textStrings[stringNum];
	  //  console.log(context.results);
	  res.json(context)
	  //res.render('get-string', context);
	  //res.json(context);
	});


	var textStrings = [ "Take out trash", "Walk the dog",
					"Do homework", "Read a book", "Brush Teeth",
					"Mop the Kitchen", "Vacuum the living room",
					"Sweep the garage", "Cook dinner", "Clean Refrigerator",
					"A/C Maintenance", "Pest Control Appointment", "Mow the Lawn",
					"Workout", "Study for exams", "Take car for oil change",
					"Get groceries", "Take cat to the vet", "Play fetch with dog",
					

					];
	
	
	// function to get a random integer between two values, from https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random
	function getRandomInt(min, max) {
	  min = Math.ceil(min);
	  max = Math.floor(max);
	  return Math.floor(Math.random() * (max - min) + min); //The maximum is exclusive and the minimum is inclusive
	}

	return router;
}();
