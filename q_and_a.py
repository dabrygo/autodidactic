# Maps a question to an answer
import csv
import random


class Fact:
    def __init__(self, facts, key, attr):
        self._facts = facts
        self._key = key
        self._attr = attr

    def question(self):
        key = self._facts[self._key]
        attr = self._facts[self._attr]
        return f"{attr} is the {self._attr} of {key}"

    def is_true(self):
        return True

    def is_false(self):
        return False


states = []
with open('us-states.csv') as f:
    reader = csv.DictReader(f)
    for line in reader:
        state = line['state']
        states.append(line)


keys = states
choice = random.choice(keys)
fact = Fact(choice, 'state', 'capital')
print(fact.question())
