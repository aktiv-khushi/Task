
//4.Random Number Guessing Game:

function guessNumber() {
    const random = Math.floor(Math.random() * 10) + 1;
    let number = parseInt(prompt('Guess a number from 1 to 10: '));
    while(number !== random) {
        number = parseInt(prompt('Not matched,Guess againas'));
    }
    if(number == random) {
        console.log('You guessed the correct number.');
    }
  }
  guessNumber();






