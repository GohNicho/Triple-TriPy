## Triple TriPy Spec (Triple Triads)

### Board Specifications
- Played on a 3x3 grid
- At all times, played cards are in possession of either one of two players
- First player gets the first and last play

### Card Specifications
- Four values on each card called **rank**
	- Each value corresponds with a direction(up, down, left, right)
- Ranges from **1-9** and **A** which represents a 10.

### Gameplay Specifications
- Players hold 5 cards each
- Coin-flip decides starting player
- Players play cards alternately in an unoccupied space
- When a card is played, adjacent ranks are compared:
	- Ex - Top rank of a card placed below another card is compared to that cards bottom rank
	- Card with the higher adjacent rank flips the other card to the player's possession (only if played on the player's turn)
- **Capturing only occurs on the players turn**
- A player is considered to have won if they own a majority of the 10 cards played
	- One unplayed card is counted to always be in possession of the second player
	- This essentially means player 1 must possess at least 6/9 cards on the board to win
	- Equal number of possession results in a draw.

### Optional Rules
- Limits on which cards can be played (In FF8 this is denoted by elements on cards)
- **A rank can be treated as "beats anything, but anything beats it"**
