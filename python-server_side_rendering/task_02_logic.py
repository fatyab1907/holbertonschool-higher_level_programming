#!/usr/bin/python3
"""Flask application with dynamic template using loops and conditions."""
import json
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/items')
def items():
    """Render items list page with data from items.json."""
    try:
        with open('items.json', 'r') as f:
            data = json.load(f)
            items_list = data.get('items', [])
    except (FileNotFoundError, json.JSONDecodeError):
        items_list = []

    return render_template('items.html', items=items_list)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
