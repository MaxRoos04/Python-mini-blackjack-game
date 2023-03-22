import random

# Skapa kortleken
cards = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4

# Blanda kortleken
random.shuffle(cards)

# Funktion för att räkna poängen
def calculate_score(hand):
    score = sum(hand)
    if score > 21 and 11 in hand:
        # Om man har minst ett ess och får mer än 21 poäng,
        # räknas esset som 1 istället för 11
        score -= 10
    return score

# Ge två kort till spelaren
hand = [cards.pop(), cards.pop()]

# Spela spelet
while True:
    print("Dina kort är:", hand)
    score = calculate_score(hand)
    if score == 21:
        print("Grattis! Du har 21!")
        break
    elif score > 21:
        print("Tyvärr har du förlust.")
        break
    else:
        choice = input("Vill du ha ett mera kort? (j/n) ")
        if choice == "j":
            hand.append(cards.pop())
        else:
            print("Du har", score, "poäng och GAME IS OVER.")
            break
    