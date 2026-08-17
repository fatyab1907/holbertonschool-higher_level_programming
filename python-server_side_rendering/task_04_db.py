#!/usr/bin/python3
"""Flask app displaying product data from JSON, CSV, or SQLite DB."""
import csv
import json
import sqlite3
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


def read_sql():
    """Read products from SQLite database."""
    products = []
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        for row in rows:
            products.append({
                "id": row[0],
                "name": row[1],
                "category": row[2],
                "price": row[3]
            })
        conn.close()
    except sqlite3.Error:
        pass
    return products


@app.route('/products')
def products():
    """Render product data based on source (json, csv, sql) and optional id."""
    source = request.args.get('source')
    product_id = request.args.get('id')

    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', error="Wrong source")

    if source == 'json':
        items = read_json('products.json')
    elif source == 'csv':
        items = read_csv('products.csv')
    else:
        items = read_sql()

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
