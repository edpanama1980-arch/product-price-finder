from flask import Flask, render_template_string, request

app = Flask(__name__)

# Mock product data
products = [
    {"name": "Wireless Mouse", "store": "Store A", "price": 25.99, "link": "https://store-a.com/mouse"},
    {"name": "Wireless Mouse", "store": "Store B", "price": 22.49, "link": "https://store-b.com/mouse"},
    {"name": "Wireless Mouse", "store": "Store C", "price": 27.00, "link": "https://store-c.com/mouse"},
    {"name": "Bluetooth Headphones", "store": "Store A", "price": 59.99, "link": "https://store-a.com/headphones"},
    {"name": "Bluetooth Headphones", "store": "Store B", "price": 49.99, "link": "https://store-b.com/headphones"},
    {"name": "Bluetooth Headphones", "store": "Store C", "price": 54.99, "link": "https://store-c.com/headphones"}
]

# HTML template as a multi-line string
template = """<!doctype html>
<html>
<head>
    <title>Product Price Finder</title>
</head>
<body>
    <h1>Find the Cheapest Product</h1>
    <form method='post'>
        <input type='text' name='product_name' placeholder='Enter product name' required>
        <input type='submit' value='Search'>
    </form>
    {% if results %}
        <h2>Results for '{{ query }}'</h2>
        <ul>
        {% for item in results %}
            <li>{{ item.name }} - {{ item.store }} - ${{ item.price }} - <a href='{{ item.link }}'>Buy</a></li>
        {% endfor %}
        </ul>
    {% endif %}
</body>
</html>"""

@app.route('/', methods=['GET', 'POST'])
def index():
    results = []
    query = ""
    if request.method == 'POST':
        query = request.form['product_name'].lower()
        results = [p for p in products if query in p['name'].lower()]
        results.sort(key=lambda x: x['price'])
    return render_template_string(template, results=results, query=query)

if __name__ == '__main__':
    app.run(debug=True)
