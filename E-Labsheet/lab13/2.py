def card_value(card):
    if card == 'A':
        return 1
    elif card in ['J', 'Q', 'K']:
        return 10
    else:
        return int(card)

def blackjack_bot(test_cases):
    results = []

    for cards in test_cases:
        total_score = 0
        drawn_cards = 0

        for i in range(2):
            total_score += card_value(cards[i])
            drawn_cards += 1

        while total_score <= 16 and drawn_cards < 5:
            total_score += card_value(cards[drawn_cards])
            drawn_cards += 1

        if total_score > 21:
            results.append("busted")
        else:
            results.append(str(total_score))

    return results

n = int(input().strip())
test_cases = [input().strip().split() for _ in range(n)]

for result in blackjack_bot(test_cases):
    print(result)










n = int(input().strip())
test_cases = [input().strip().split() for _ in range(n)]
results = []

for cards in test_cases:
    done = 0
    drawn_cards = 0

    for i in range(2):
        card = cards[i]
        if card == 'A':
            done += 1
        elif card in ['J', 'Q', 'K']:
            done += 10
        else:
            done += int(card)
        drawn_cards += 1

    while done <= 16 and drawn_cards < 5:
        card = cards[drawn_cards]
        if card == 'A':
            done += 1
        elif card in ['J', 'Q', 'K']:
            done += 10
        else:
            done += int(card)
        drawn_cards += 1

    if done > 21:
        results.append("busted")
    else:
        results.append(str(done))

for result in results:
    print(result)




n = int(input().strip())
results = []

for _ in range(n):
    cards = input().strip().split()
    done = 0

    for card in cards[:2]:
        if card == 'A':
            done += 1
        elif card in 'JQK':
            done += 10
        else:
            done += int(card)

    drawn_cards = 2
    while done <= 16 and drawn_cards < len(cards):
        card = cards[drawn_cards]
        if card == 'A':
            done += 1
        elif card in 'JQK':
            done += 10
        else:
            done += int(card)
        drawn_cards += 1

    if done > 21:
        results.append("busted")
    else:
        results.append(str(done))

print("\n".join(results))