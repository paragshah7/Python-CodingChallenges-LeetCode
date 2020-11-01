## BlackJack Game
This game has been developed using Python 3. Enjoy playing!

#### Requirements: 
- Running the program
  - Run using the command in Python 3 interpreter: **python3 blackjack.py**
  - No dependencies

- Assumptions/Choices made
  - Running the program once means player can play only once. If player wants to play again, the program must be ran again
  - Used output format given in freenome_coding_interview.pdf
  - Since we don't concern ourselves with card suit, I'm using all 13 cards and multiplying it by 4 to get 52 cards

- Things I did well
  - I handled most of the game rules mentioned in the pdf by creating various cases
  - Created functions for more clarity
  - Added comments wherever necessary
  
- Design choices made
  - Used functional programming by creating functions and handling each scenario as the game progresses for a user
  - Used list to store card values
  - Used list to add cards for player and dealer

- Tradeoffs I encountered and how I resolved them
  - This game contains many cases to be handled. I resolved them by tackling each case and making sure I'm not breaking any previously fixed case
  - Initially I hardcoded value of 'A' to be 11 for simple calculations. At the very last I added scenario for 'Intricacies of Ace' in calculate_total
  - I hardcoded inputs while testing various scenarios
  - Not showing a dealer card to the player and displaying '?' was challenging. I created separate function to handle that

- How would I improve
  - I can create a couple more functions to handle print statements more aesthetically
  - I would try to learn to do it in an object oriented way

- Manual tests I ran
  - Ran player win scenarios with BlackJack, better score, dealer bust cases
  - Ran dealer win scenarios with BlackJack, better score, player bust cases
  - Handled incorrect input to prompt user to enter from required input
