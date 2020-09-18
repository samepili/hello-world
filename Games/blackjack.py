import random

suits = ('Diamonds','Clubs','Hearts','Spades')
ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')
values = {'Two':2,'Three':3,'Four':4,'Five':5,'Six':6,'Seven':7,'Eight':8,'Nine':9,'Ten':10,'Jack':10,'Queen':10,'King':10,'Ace':11}


class Card:

	def __init__(self,suit,rank):
		self.suit = suit
		self.rank = rank

	def __str__(self):
		return self.rank + ' of ' + self.suit

class Deck:

	def __init__(self):
		self.deck = []
		for suit in suits:
			for rank in ranks:
				self.deck.append(Card(suit,rank))

	def __str__(self):
		deck_str = ''
		for card in self.deck:
			deck_str += '\n ' + card.__str__()
		return 'Cards in Deck: ' + deck_str

	def shuffle_cards(self):
		random.shuffle(self.deck)

	def deal(self):
		top_card = self.deck.pop()
		return top_card


class Hand:

	def __init__(self):
		self.hand = []
		self.value = 0
		self.aces = 0

	def add_card(self,card):
		self.hand.append(card)
		self.value += values[card.rank]
		if card.rank == 'Ace':
			self.aces += 1

	def check_for_aces(self):
		while self.value > 21 and self.aces:
			self.value -= 10
			self.aces -= 1

class Chips:

	def __init__(self):
		self.total = 100 #can be changed
		self.bet = 0 #intialize bet

	def bet_chips(self):
		while True:
			try:
				self.bet = int(input('Place your bet: '))

			except ValueError:
				print('Please enter an integer amount')

			else:
				if self.bet > self.total:
					print('You cannot bet more chips than you currently have')
				else:
					break

	def win_bet(self):
		self.total += self.bet

	def lose_bet(self):
		self.total -= self.bet


#functions

def show_some(dealer,player):
	print("\nDealer's hand:")
	print(" <hidden>")
	print(" ",dealer.hand[1])
	print("\nYour Hand:", *player.hand, sep = '\n ')
	print('Your Hand= ',player_hand.value,'\n')

def show_all(dealer,player):
	print("\nDealer's hand:", *dealer.hand, sep = '\n ')
	print('Dealer total= ',dealer_hand.value,'\n')
	print("\nYour Hand:", *player.hand, sep = '\n ')
	print('Your Hand= ',player_hand.value,'\n')

def player_wins(chips):
	print('You won!')
	chips.win_bet()

def player_busts(chips):
	print('You busted!')
	chips.lose_bet()

def dealer_wins(chips):
	print('Dealer wins with a higher hand!')
	chips.lose_bet()

def dealer_busts(chips):
	print('Dealer busts! You won!')
	chips.win_bet()

def push():
	print("You tied with the dealer! It's a push!")

def hit(hand,deck):
	hand.add_card(deck.deal())
	hand.check_for_aces()


def hit_or_stand(hand,deck):
	global playing

	while True:
		x = input("Hit 'h' or Stand 's': ")

		if x.lower() == 'h':
			hit(hand,deck)

		elif x.lower() == 's':
			print("You stand. Dealer's turn.")
			playing = False

		else:
			print('Please enter a valid input')
			continue

		break

#logic

if __name__ == '__main__':

	print('Welcome to Blackjack!')

	player_chips = Chips()	

	while True:

		playing = True

		deck = Deck()
		deck.shuffle_cards()
		player_hand = Hand()
		dealer_hand = Hand()


		print(f'\nYou have {player_chips.total} chips')
		player_chips.bet_chips()

		player_hand.add_card(deck.deal())
		dealer_hand.add_card(deck.deal())
		player_hand.add_card(deck.deal())
		dealer_hand.add_card(deck.deal())

		show_some(dealer_hand,player_hand)

		#player's turn
		while playing:
			hit_or_stand(player_hand,deck)
			show_some(dealer_hand,player_hand)

			if player_hand.value > 21:
				player_busts(player_chips)
				print(f'You lost {player_chips.bet} chips!')
				break

		#dealer's turn
		if player_hand.value <= 21:

			while dealer_hand.value < 17:
				hit(dealer_hand,deck)
			
			show_all(dealer_hand,player_hand)

			if dealer_hand.value > 21:
				dealer_busts(player_chips)

			elif dealer_hand.value > player_hand.value:
				dealer_wins(player_chips)

			elif dealer_hand.value < player_hand.value:
				player_wins(player_chips)

			else:
				push()

		replay = input('\nWould you like to play again (y/n)? ')

		if replay.lower() == 'y':
			continue
			playing = True
		
		else:
			print(f'Thank you for playing! You walked away with {player_chips.total} chips')
			break