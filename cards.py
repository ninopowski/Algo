
# numbers = [1, 7, 8, 3, 4, 6, 9, 13, 15]
# sorted_numbers = sorted(numbers, reverse=True)
# print(sorted_numbers)

test1 = {
    "input": {
        "cards": [13, 11, 10, 7, 4, 3, 1, 0],
        "query": 4
    },
    "output": 4
}

test2 = {
    "input": {
        "cards": [],
        "query": 7
    },
    "output": -1
}

tests = [test1, test2]

def locate_card(cards, query):
    position = 0
    print("cards:", cards)
    print("query:", query)

    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1


def optimal_search(cards, query):
    lo, hi= 0, len(cards)-1
    counter = 0
    while lo <= hi:
        mid = (lo+hi) // 2
        mid_card = cards[mid]
        counter += 1
        print(f"lo: {lo}, hi: {hi}, mid: {mid}, mid_card: {mid_card}")

        if mid_card == query:
            print(f"It took {counter} tries.")
            return mid_card
        elif mid_card > query:
            lo = mid + 1
        elif mid_card < query:
            hi = mid - 1
    return -1


for test in tests:
    print(locate_card(**test["input"]) == test["output"])

for test in tests:
    optimal_search(**test["input"]) == test["output"]


