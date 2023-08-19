import random
import os

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def main():
 
    while True:
        print("You are now playing Blackjack - 21")
        #inicia el juego se reparten las cartas
        player, dealer = [], []
        for i in range(2):
            player.append(deal_card(cards))
            dealer.append(deal_card(cards))
        #player tiene 2 y se ven , cpu tiene 2 y solo la primera es visible
        #mostrar cartas de usuario
        print(f"Player cards {player}")
        # mostrar carda de dealer
        print(f"Delaer hand {dealer[0]}")
        
        # ciclo de agregar cartas jugador
        while True:
            if sum(player) == 21:
                break
            elif sum(player) > 21:
                break
            else:
                another_card = input("Type 'y' if want another card: ")
                if another_card == 'y':
                    player_new_card = deal_card(cards)
                    if player_new_card == 11 and sum(player) > 10:
                        player_new_card == 1
                    player.append(player_new_card)
                    print(f"Player cads {player} -> Total {sum(player)}")
                else:
                    break
        
        # ciclo de agregar cartas dealer
        while True:
            if sum(dealer) < 17:
                dealer_new_card = deal_card(cards)
                if dealer_new_card == 11:
                    dealer_new_card = 1
                dealer.append(dealer_new_card)
            else:
                break
               
        # comparing hands
        total_player = sum(player)
        total_delaer = sum(dealer)
        print(f"Player cards {player}  -> Total: {total_player}")
        print(f"Dealer cards {dealer}  -> Total: {total_delaer}")
        
        if (total_player > 21 and total_delaer > 21) or total_player ==  total_delaer:
            print("Draw")
        elif total_player > 21:
            print("Dealer wins")
        elif total_delaer > 21:
            print("Player wins!")
        elif total_player > total_delaer:
            print("Player wins!")
        else:
            print("Dealer wins")
            
        if input("Type 'y' if you want another round: ") != 'y':
            break
        else:
            os.system('clear')
    
    
# retorna una carta de la baraja
def deal_card(cards):
    """Returns a random card from the deck.
    Cards are not popped form the deck"""
    return cards[random.randint(0, len(cards) - 1)]
main()