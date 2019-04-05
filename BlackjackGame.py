# -*- coding: utf-8 -*-
import random
input = raw_input
def blackjack():
  print(" This is a game of Blackjack. In this game the goal is to get as close to 21 as possible without going over. You and the AI will each recieve 2 cards initially. You will have the choice to either hit or stand until you are satisfied with your hand. Then the AI will go. The AI wins on ties. ")
  p_score = 0
  p_card_list = []
  p_ace = 0
  a_score = 0
  a_card_list = []
  a_ace = 0
  deck = [
  ['Ace', 'Spade'],['2', 'Spade'],['3', 'Spade'],['4', 'Spade'],['5', 'Spade'],['6', 'Spade'],['7', 'Spade'],['8', 'Spade'],['9', 'Spade'],['10', 'Spade'],['Jack', 'Spade'],['Queen', 'Spade'],['King', 'Spade'],

  ['Ace', 'Heart'],['2', 'Heart'],['3', 'Heart'],['4', 'Heart'],['5', 'Heart'],['6', 'Heart'],['7', 'Heart'],['8', 'Heart'],['9', 'Heart'],['10', 'Heart'],['Jack', 'Heart'],['Queen', 'Heart'],['King', 'Heart'],

  ['Ace', 'Diamond'],['2', 'Diamond'],['3', 'Diamond'],['4', 'Diamond'],['5', 'Diamond'],['6', 'Diamond'],['7', 'Diamond'],['8', 'Diamond'],['9', 'Diamond'],['10', 'Diamond'],['Jack', 'Diamond'],['Queen', 'Diamond'],['King', 'Diamond'],

  ['Ace', 'Club'],['2', 'Club'],['3', 'Club'],['4', 'Club'],['5', 'Club'],['6', 'Club'],['7', 'Club'],['8', 'Club'],['9', 'Club'],['10', 'Club'],['Jack', 'Club'],['Queen', 'Club'],['King', 'Club'],
  ]

# card_num is the number of the card including Jack, Queen etc
# card_value is what value the card number corresponds to (a number between 1-11)
# card_suit is either heart, spade, diamond or club
  used_numbers = []
  
  def draw():
    while True:
      val = random.randint(0,51)
      card_num = deck[val][0]
      card_suit = deck[val][1]
      if val not in used_numbers:
        used_numbers.append(val)
        break
    if card_num in ('2','3','4','5','6','7','8','9','10'):
      card_value = int(card_num)

    if card_num in ('Jack', 'Queen', 'King'):
      card_value = 10

    if card_num == 'Ace':
      card_value = 11
  
    return (card_value, card_num, card_suit)
    
  def graphics(card,suit):
    suits_symbols = {'Spade':'♠', 
                    'Diamond':'♦',
                    'Heart': '♥',
                    'Club' : '♣'
                    }
    card_values = {
    'Ace': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10
    }
    if card != '10':
      space = ' '
    if card =='10':
      space = ''

    if card in ('Jack', 'Queen', 'King', 'Ace'):
      card_value = card[0]
    else:
      card_value = card
 
    suit_val = suits_symbols[suit]
    
    # format
    lines = []
    lines.append('____________')
    lines.append('│{}{}       │'.format(card_value, space))
    lines.append('│         │')
    lines.append('│         │')
    lines.append('│    {}    │'.format(suit_val))
    lines.append('│         │')
    lines.append('│         │')
    lines.append('│       {}{}│'.format(space, card_value))
    lines.append('------------')
    return '\n'.join(lines)

  # Draw twice
  p_card = draw()
  if p_card[1] == 'Ace':
    p_ace += 1
  p_score += p_card[0]
  p_card_list.append((p_card[1], p_card[2]))

  p_card = draw()
  if p_card[1] == 'Ace':
    p_ace += 1
  p_score += p_card[0]
  p_card_list.append((p_card[1], p_card[2]))

  a_card = draw()
  if a_card[1] == 'Ace':
    a_ace += 1
  a_score += a_card[0]
  a_card_list.append((a_card[1], a_card[2]))

  a_card = draw()
  if a_card[1] == 'Ace':
    a_ace += 1
  a_score += a_card[0]
  a_card_list.append((a_card[1], a_card[2]))

  for i in p_card_list:
    print(graphics(i[0],i[1]))

  if p_score > 21:
    p_score -= 10
    p_ace -=1
    
  print('Your Score: '+str(p_score))

  for i in a_card_list:
    print(graphics(i[0],i[1]))
  
  if a_score > 21:
    a_score -= 10
    a_ace -= 1
  if a_score ==21:
    print('AI got blackjack, so they win')
    return

  print('AI score: ' + str(a_score))

  answer = 'hi'
  while answer != 'stand':
    answer = input('stand or hit: ')
    if answer == 'stand':
      for i in p_card_list:
        print(graphics(i[0],i[1]))
    
      print('Your score: '+ str(p_score))
      break
    p_card = draw()
    if p_card[1] == 'Ace':
      p_ace += 1
    p_score += p_card[0]
    p_card_list.append((p_card[1], p_card[2]))
    while p_score > 21 and p_ace > 0:
      p_ace -= 1
      p_score -= 10
    for i in p_card_list:
      print(graphics(i[0],i[1]))
    
    print('Your score: '+ str(p_score))
    if p_score > 21 and p_ace == 0:
      print("you lost because you went over 21")
      break
    if p_score == 21:
      print("BLACKJACK. But if the dealer gets this as well, they win")
      answer = 'stand'
      break
  
  if answer == 'stand':    
    print("The AI is now picking")
    while a_score < p_score:
      a_card = draw()
      if a_card[1] == 'Ace':
        a_ace += 1
      a_score += a_card[0]
      a_card_list.append((a_card[1], a_card[2]))
      while a_score > 21 and a_ace > 0:
        a_ace -= 1
        a_score -= 10
    for i in a_card_list:
      print(graphics(i[0],i[1]))
    
    print('AI score: '+ str(a_score))
    if a_score > 21 and a_ace == 0:
      print('You won because AI went over 21')
    elif a_score > p_score:
      print("AI won becasue it was closer to 21")
    if a_score == p_score:
      print("AI win because dealer wins on ties")  

# takes inputs of card and suit



replay = 'yes'
while replay == 'yes':
  blackjack()
  replay = input('Do you want to play again ( yes or no): ')
  

