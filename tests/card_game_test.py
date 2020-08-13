import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    
    def setUp(self):
        self.card1=Card("Hearts",1)
        self.card2=Card("Hearts",2)
        self.card3=Card("Spades",2)
        self.game1=CardGame()
        
    #test card has suit
    def test_card_has_suit(self):
        self.assertEqual("Hearts",self.card1.suit)
    #test card has value
    def test_card_has_value(self):
        self.assertEqual(1,self.card1.value)
    
    #test check for ace true
    def test_check_ace_returns_true(self):
        output = self.game1.checkforAce(self.card1)
        self.assertEqual(True,output)
        
    # test card is not ace
    def test_check_ace_returns_false(self):
        output = self.game1.checkforAce(self.card2)
        self.assertEqual(False,output)

    # test for highest card is 2
    def test_check_which_highest(self):
        output = self.game1.highest_card(self.card2, self.card1)
        self.assertEqual(2,output.value)

    # test cards same value
    def test_check_neither_highest(self):
        output = self.game1.highest_card(self.card2, self.card3)
        self.assertEqual(2,output.value)

   