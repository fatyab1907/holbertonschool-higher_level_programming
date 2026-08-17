#!/usr/bin/python3
"""Basic serialization module using JSON."""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file."""
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """Load and deserialize JSON data from a file into a dictionary."""
    with open(filename, encoding="utf-8") as f:
        return json.load(f)
