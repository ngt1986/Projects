//  main
function runGame() {
	//  initialize game area and size canvas to fit inside container (div id = canvasContainer)
	gameCanvas.initCanvas();
	resizeCanvas();
	
	//  event listener for resize of window to adjust canvas
	//  window.addEventListener('resize', resizeCanvas, false);
	//  resizeCanvas(container, canvas);
	
	window.onresize = resizeCanvas;
	
	//  canvasSizing(document.getElementById("canvasContainer"), document.getElementById("canvas"));
	playerBlock = new block(30, 30, "red",canvas.width/2, canvas.height/2,0,0, "player");
	
}

//  game area and key press detection
var gameCanvas = {
	initCanvas : function() {
		container = document.getElementById("canvasContainer"),
		canvas = document.createElement("canvas");
		container.appendChild(canvas);
		context = canvas.getContext("2d");
		interval = setInterval(updateGameCanvas, 20);  //20 millisecond update time
		frameNumber = 0;
		//  add detection for pressed keys
		window.addEventListener('keydown', function (e) {
			gameCanvas.keys = (gameCanvas.keys || []);
			gameCanvas.keys[e.keyCode] = true;
		})
		window.addEventListener('keyup', function (e) {
			gameCanvas.keys[e.keyCode] = false;
		})
	},
	
	//  function to clear screen
	clear : function () {
		context.clearRect(0, 0, canvas.width, canvas.height);
	},
	
	// function to stop game
	crash : function () {
		clearInterval(this.interval);
	}
}

//  updating position of things
function updateGameCanvas() {
    //  check if collision
    if (checkCrash(playerBlock,enemyBlocks) == true) {
	    gameCanvas.crash();
		return;
    }
	gameCanvas.clear();
	frameNumber += 1;
	
	//spawn interval in # of frames
	spawnRate = 50;
	spawnEnemyBlocks(spawnRate);

	// stops player if movement keys not pressed.
	playerBlock.speedX = 0;
	playerBlock.speedY = 0;

	//  if a key is pressed and it's one of the arrow keys, adjust speed accordingly
	if (gameCanvas.keys && (gameCanvas.keys[37] || gameCanvas.keys[65])) {playerBlock.speedX = -5;}  //  left arrow or 'a'
	if (gameCanvas.keys && (gameCanvas.keys[39] || gameCanvas.keys[68])) {playerBlock.speedX = 5;}  // right arrow or 'd'
	if (gameCanvas.keys && (gameCanvas.keys[38] || gameCanvas.keys[87])) {playerBlock.speedY = -5;}  // up arrow or 'w'
	if (gameCanvas.keys && (gameCanvas.keys[40] || gameCanvas.keys[83])) {playerBlock.speedY = 5;}  // down arrow or 's'
	playerBlock.updatePosition();
	playerBlock.updateDraw();
  
	//  update enemyBlocks
	for (i = 0; i < enemyBlocks.length; i += 1) {
		enemyBlocks[i].updatePosition();
		enemyBlocks[i].updateDraw();
		
		// if enemy block out of bounds, remove it;
		if (enemyBlocks[i].x < 0 - enemyBlocks[i].width || enemyBlocks[i].x > canvas.width || enemyBlocks[i].y < 0 - enemyBlocks[i].width || enemyBlocks[i].y > canvas.height) {
			enemyBlocks.splice(i,1);
		}
	}
}

/*function redrawCanvas(width, height, canvas, context) {
	context = canvas.getContext("2d");
	context.strokeStyle = 'black';
	context.lineWidth = '1';
	context.strokeRect(0,0, width, height);
} 
*/

function resizeCanvas() {
	var width = container.offsetWidth,
		height = container.offsetHeight;
	canvas.width = width;
	canvas.height = height;
}


	
var playerBlock;
//  player's block
function block(width, height, color, x, y, vx, vy, entity) {
	//  initialize values for width/height/speed for player/enemies
	this.width = width;
    this.height = height;
	this.speedX = vx;
	this.speedY = vy;
    this.x = x;
    this.y = y;    
	this.id = entity;
	//  draw block on the canvas
	this.updateDraw = function () {
		context.fillStyle = color;
		context.fillRect(this.x, this.y, this.width, this.height);
	}
	//  update position of block on canvas
	this.updatePosition = function() {
		
	// add check for if playerBlock at boundary
		if (this.id == "player") {
			if (this.x <= 0 && this.speedX < 0) {
				if (this.y <= 0 && this.speedY < 0) {
					return;
				} else if (this. y >= canvas.height - width && this.speedY > 0){
					return;
				} else {
					this.y += this.speedY;
				}
			} else if (this.x >= canvas.width - this.width && this.speedX > 0) {
				if (this.y <= 0 && this.speedY < 0) {
					return;
				} else if (this.y >= canvas.height - width && this.speedY > 0){
					return;
				} else {
					this.y += this.speedY;
				}
			} else if (this.y >= canvas.height - this.width && this.speedY > 0) {
				if (this.x <= 0 && this.speedX < 0) {
					return;
				} else if (this.X >= canvas.width - width && this.speedX > 0){
					return;
				} else {
					this.x += this.speedX;
				}
			} else if (this.y <= 0 && this.speedY < 0) {
				if (this.x <= 0 && this.speedX < 0) {
					return;
				} else if (this.X >= canvas.width - width && this.speedX > 0){
					return;
				} else {
					this.x += this.speedX;
				}
			}	else {
				this.x += this.speedX;
				this.y += this.speedY;
			}
		} else {
			this.x += this.speedX;
			this.y += this.speedY;
		}
	}
}

var enemyBlocks = [];
function spawnEnemyBlocks(interval) {
	var dir = getRandomInt(1, 5);
	var width = getRandomInt(25, 50);
	var speed = getRandomInt(5,15);
	
	if ((frameNumber) % interval == 0) {
		if (dir == 1) {
			xPosition = getRandomInt(0, canvas.width-width);
			yPosition = 0-width;
			vx = 0;
			vy = speed;
		}
		if(dir == 2) {
			xPosition = canvas.width;
			yPosition = getRandomInt(0, canvas.height - width);
			vx = -speed;
			vy = 0;
		}
		if (dir == 3) {
			xPosition = getRandomInt(0, canvas.width - width);
			yPosition = canvas.height;
			vx = 0;
			vy = -speed;
		}
		if (dir == 4) {
			xPosition = 0 - width;
			yPosition = getRandomInt(0, canvas.height - width);
			vx = speed;
			vy = 0;
		}
		enemyBlocks.push(new block(width, width, "green", xPosition, yPosition, vx, vy, "enemy"));
	}
}

// function to get a random integer between two values, from https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/random
function getRandomInt(min, max) {
  min = Math.ceil(min);
  max = Math.floor(max);
  return Math.floor(Math.random() * (max - min) + min); //The maximum is exclusive and the minimum is inclusive
}

function checkCrash(playerBlock,enemyBlocks) {
	p = playerBlock;
	//console.log(p.x, p.y, p.width,p.height);
	crash = false;
	for (i = 0; i < enemyBlocks.length; i += 1) {
		e = enemyBlocks[i];
		if ((p.x + p.width > e.x && e.x > p.x) && (p.y + p.height > e.y && e.y > p.y)) {
			crash = true;
		} else if 
			((p.x + p.width > e.x + e.width && e.x + e.width > p.x) && (p.y + p.height > e.y && e.y > p.y)) {
			crash = true;
		} else if 
			((p.x + p.width > e.x  && e.x > p.x) && (p.y + p.height > e.y + e.height && e.y + e.height > p.y)) {
			crash = true;
		} else if 
			((p.x + p.width > e.x + e.width && e.x + e.width > p.x) && (p.y + p.height > e.y + e.height && e.y + e.height > p.y)) {
			crash = true;
		}
	}
	return crash;
}