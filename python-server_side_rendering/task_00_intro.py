#!/usr/bin/python3
"""Module for generating invitation files from a template."""


def generate_invitations(template, attendees):
    """Generate invitation files from a template and attendees list."""
    if not isinstance(template, str):
        print("Invalid input type: template must be a string.")
        return

    if not isinstance(attendees, list) or not all(
        isinstance(item, dict) for item in attendees
    ):
        print("Invalid input type: attendees must be a list of dictionaries.")
        return

    if not template.strip():
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    placeholders = ["name", "event_title", "event_date", "event_location"]

    for idx, attendee in enumerate(attendees, start=1):
        content = template
        for key in placeholders:
            val = attendee.get(key)
            if val is None:
                val = "N/A"
            content = content.replace(f"{{{key}}}", str(val))

        filename = f"output_{idx}.txt"
        try:
            with open(filename, "w") as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
