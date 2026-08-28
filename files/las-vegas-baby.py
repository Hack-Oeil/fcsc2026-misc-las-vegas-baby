from treys import Card, Evaluator

def deal(deck, nbPlayers, cut = 0):
    # Cut the deck
    deck = deck[cut:] + deck[:cut]

    # Deal the pocket cards
    hands = [ [] for _ in range(nbPlayers) ]
    for i in range(2 * nbPlayers):
        card = Card.new(deck.pop(0))
        hands[i % nbPlayers].append(card)

    deck.pop(0)
    flop = [ Card.new(deck.pop(0)) for _ in "012" ]

    deck.pop(0)
    turn = Card.new(deck.pop(0))

    deck.pop(0)
    river = Card.new(deck.pop(0))
    
    board = flop + [turn, river]

    E = Evaluator()
    results = []
    for i, hand in enumerate(hands):
        score = E.evaluate(board, hand)
        results.append((i, score))

    results.sort(key = lambda x: x[1])
    winner = results[0]
    return winner[0]

if __name__ == "__main__":
    print("Welcome to Las Vegas!")
    print("You are in the small blind for the next hand.")
    print("You will be either 3 or 4 players at the next hand.")
    print("The deck is at your disposal, no one is watching you...")
    try:
        deck = input(">>> ").split(",")
        assert len(deck) == 52, "The deck must contain exactly 52 cards."
        assert len(set(deck)) == 52 , "All the cards must be unique."
        assert all(isinstance(c, str) and len(c) == 2 for c in deck), "The cards must be 2-character strings."
        assert all(c[0] in "AKQJT98765432" and c[1] in "shdc" for c in deck), "The cards must have the correct format."
        assert all(deal(deck, 3, cut = i) == 0 for i in range(52))
        assert all(deal(deck, 4, cut = i) == 0 for i in range(52))
        print(f"Congrats! Here is the flag:")
        print(open("flag.txt").read())
    except:
        print("Loose Vegas :(")
