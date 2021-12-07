class BingoCard:
    def __init__(self, lines):
        self.numbers = [int(number) for line in lines for number in line.split(" ") if number != ""]
        self.markings = [0] * len(self.numbers)
        self.marked_numbers = set()
        print("Created!")

    def mark(self, number):
        try:
            self.markings[self.numbers.index(number)] = 1
            self.marked_numbers.add(number)
            print("Marked!")
        except ValueError:
            pass

    def has_bingo(self):
        for index in range(0, 5):
            if sum(self.markings[index*5:index*5+5]) == 5:
                return True
            if sum(self.markings[index::5]) == 5:
                return True
        return False

    def get_score(self, number):
        print("Trying to score!")
        return sum([entry for entry in self.numbers if entry not in self.marked_numbers]) * number


with open("input_day4.txt") as file:
    lines = file.readlines()
lines = [line.strip() for line in lines]
bingo_cards = []
numbers = [int(entry) for entry in lines[0].split(",") if entry != ""]
print(numbers)
offset = 2
# Create all cards
while True:
    lines_to_create = lines[offset:offset+5]
    offset += 6
    if len(lines_to_create) == 0:
        break
    bingo_cards.append(BingoCard(lines_to_create))
num_cards = len(bingo_cards)
# For the cards, mark and score
try:
    for number in numbers:
        for bingo_card in bingo_cards:
            bingo_card.mark(number)
            if bingo_card.has_bingo():
                final_score = bingo_card.get_score(number)
            # The final score will now be the last that got bingo
            if sum([bingo_card.has_bingo() for bingo_card in bingo_cards]) == num_cards:
                raise StopIteration
except StopIteration:
    pass

print(final_score)