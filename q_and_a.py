# Maps a question to an answer
import csv
import random


class Fact:
    def __init__(self, fact, key, attr):
        self._fact = fact
        self._key = key
        self._attr = attr

    def question(self):
        key = self._fact[self._key]
        attr = self._fact[self._attr]
        return f"{attr} is the {self._attr} of {key}"

    def is_true(self):
        return True

    def is_false(self):
        return False


class Fiction:
    def __init__(self, fact, other_fact, key, attr):
        self._fact = fact
        self._other_fact = other_fact
        self._key = key
        self._attr = attr

    def question(self):
        key = self._fact[self._key]
        attr = self._other_fact[self._attr]
        return f"{attr} is the {self._attr} of {key}"

    def is_true(self):
        return False

    def is_false(self):
        return True


states = []
with open('us-states.csv') as f:
    reader = csv.DictReader(f)
    for line in reader:
        state = line['state']
        states.append(line)


n = 50
correct = 0
keys = states
for i in range(n):
    fact = random.randint(0, 1)
    if fact:
        choice = random.choice(keys)
        question = Fact(choice, 'state', 'capital')
    else:
        choice = random.choice(keys)
        choice2 = random.choice(keys)
        question = Fiction(choice, choice2, 'state', 'capital')

    print()
    print(f"Question {i}/{n}")
    print("True or False.", question.question())
    answer = input(">>> ").strip()
    while answer not in ['T', 'F']:
        print(f"Invalid answer '{answer}'. Please type T or F.")
        print("True or False:", question.question())
        answer = input(">>> ").strip()

    if answer == 'T' and question.is_true():
        correct += 1
    elif answer == 'F' and question.is_false():
        correct += 1
    else:
        print("Nope.")

