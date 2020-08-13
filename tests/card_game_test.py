import unittest

from src.card import Card
from src.card_game import CardGame

class CardGameTest(unittest.TestCase):
    
    def setUp(self):
        self.card1=Card("Hearts",1)
        self.card2=Card("Hearts",2)

    #test card has suit
    def test_card_has_suit(self):
        self.assertEqual("Hearts",self.card1.suit)
    #test card has value
    def test_card_has_value(self):
        self.assertEqual(1,self.card1.value)
    
    #test check for ace true
    def test_check_ace_returns_true(self):
        output = CardGame.checkforAce(self.card1)
        self.assertEqual(True,output)
        
    # test card is ace

    # test for highest card is 2

    # test for 
   