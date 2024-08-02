#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.state import State

new_state = State(name="state1")
storage.new(new_state)
new_state = State(name="state2")
storage.new(new_state)
new_state = State(name="state3")
storage.new(new_state)
new_state = State(name="state4")
storage.new(new_state)
new_state = State(name="state5")
storage.new(new_state)

print("All objects: {}".format(storage.count()))
print("State objects: {}".format(storage.count(State)))

first_state_id = list(storage.all(State).values())[0].id
print("first_state_id: {}".format(first_state_id))

print("First state: {}".format(storage.get(State, first_state_id)))