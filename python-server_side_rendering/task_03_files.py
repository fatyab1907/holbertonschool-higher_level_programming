#!/usr/bin/python3
"""Flask app to display product data from JSON or CSV files."""
import csv
import json
from flask import Flask, render_template, request

app = Flask(__name__)


def read_json(filename):
    """Read products from a JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception:
        return []


def read_csv(filename):
    """Read products from a CSV file."""
    products = []
    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    "id": int(row["id"]),
                    "name": row["name"],
                    "category": row["category"],
                    "price": float(row["price"])
                })
    except Exception:
        pass
    return products


@app.route('/products')
def products():
    """Render product data based on source and optional id parameters."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        items = read_json('products.json')
    else:
        items = read_csv('products.csv')

    if product_id:
        try:
            p_id = int(product_id)
            items = [item for item in items if item.get('id') == p_id]
            if not items:
                return render_template(
                    'product_display.html', error="Product not found"
                )
        except ValueError:
            return render_template(
                'product_display.html', error="Product not found"
            )

    return render_template('product_display.html', products=items)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
