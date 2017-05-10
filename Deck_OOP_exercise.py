import random
from functools import wraps
import csv
import pdb

def log(fn):
	@wraps(fn)
	def inner(*args):
		with open('deck.log', 'a') as file:
			file.write('\n')
			file.write(fn.__name__)
			file.write('\n')
			for a in args:
				file.write(str(a))
		return fn(*args)
	return inner

class Deck:
	def __init__(self):
		self.full_deck = []
		self.counter = 0

		suits = ['H', 'S', 'D', 'C']
		values = ['A', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q' , 'K']
		for value in values:
			for suit in suits:
				self.full_deck.append(Card(suit, value))

	def __repr__(self):
		return ','.join(map(str,self.full_deck))
	
	def __iter__(self):
		return self
	
	def __next__(self):
		if self.counter == len(self.full_deck):
			raise StopIteration
			self.counter = 0
		else:
			self.counter += 1
			return self.full_deck[self.counter-1]

	# @log
	def shuffle(self):
		random.shuffle(self.full_deck)

	# @log
	def deal(self):
		return self.full_deck.pop(0)

	def save(self):
		with open('deck.csv', 'w') as csvfile:
			current_deck = csv.writer(csvfile, delimiter=',')
			for card in self.full_deck:
				current_deck.writerow([card.suit, str(card.value)])


	def restore_saved_deck(self):
		with open('deck.csv', 'r') as csvfile:
			reader = csv.reader(csvfile)
			rows = list(reader)
			self.full_deck = []
			for row in rows:
				self.full_deck.append(Card(row[0], row[1]))


class Card:
	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __str__(self):
		return self.suit + str(self.value)

	def __repr__(self):
		return self.suit + str(self.value)


d = Deck()
for c in d:
	print(c)
from IPython import embed; embed()
# d.shuffle()
# start = d.shuffle()
# round1 = d.deal()
# round2 = d.deal()
# round3 = d.deal()
# round4 = d.deal()
# round5 = d.deal()
# round6 = d.deal()
# round7 = d.deal()
# # round8 = d.deal()
# d.restore_saved_deck()
# round9 = d.deal()
# round10 = d.deal()
# round11 = d.deal()
# d.save()
# d2 = Deck()
# d2.save()
