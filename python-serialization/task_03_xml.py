#!/usr/bin/python3
"""Module for XML serialization and deserialization."""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into an XML file."""
    root = ET.Element("data")
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Deserialize an XML file into a Python dictionary."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()
        data_dict = {}
        for child in root:
            data_dict[child.tag] = child.text
        return data_dict
    except Exception:
        return None
