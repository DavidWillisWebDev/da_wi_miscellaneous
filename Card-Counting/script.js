/*
In BlackJack, cards are counted with -1, 0, 1 values:

2, 3, 4, 5, 6 are counted as +1
7, 8, 9 are counted as 0
10, J, Q, K, A are counted as -1
Create a function that counts the number and returns it from the array of cards provided.

Examples
count([5, 9, 10, 3, "J", "A", 4, 8, 5]) ➞ 1

count(["A", "A", "K", "Q", "Q", "J"]) ➞ -6

count(["A", 5, 5, 2, 6, 2, 3, 8, 9, 7]) ➞ 5
Notes
String inputs will always be upper case.
You do not need to consider case sensitivity.
If the argument is empty, return 0.
No input other than: 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A".
*/

var hand = ["A", 5, 5, 2, 6, 2, 3, 8, 9, 7];

function count(deck)
{
  var cardCount = 0;
	for (var i = 0; i < deck.length; i++)
  {
    card = deck[i];
    if (card == 2 || card == 3 || card == 4 || card == 5 || card == 6)
    {
      cardCount = cardCount+1;
    }
    else if (card == 10 || card == "J" || card == "Q" || card == "K" || card == "A")
    {
      cardCount = cardCount-1;
    }
  }
  return cardCount;
}

console.log(count(hand));