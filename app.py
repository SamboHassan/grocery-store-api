from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data to mimic the API response
data = [
    {
        "id": 4643,
        "category": "coffee",
        "name": "Starbucks Coffee Variety Pack, 100% Arabica",
        "inStock": True,
    },
    {
        "id": 4646,
        "category": "coffee",
        "name": "Ethical Bean Medium Dark Roast, Espresso",
        "inStock": True,
    },
    {
        "id": 4641,
        "category": "coffee",
        "name": "Don Francisco Colombia Supremo Medium Roast",
        "inStock": True,
    },
]


@app.route("/products", methods=["GET"])
def get_products():
    # Extract query parameters
    results = request.args.get("results", default=None, type=int)
    category = request.args.get("category", default=None, type=str)

    # Validate the 'results' parameter
    if results is not None and results > 20:
        return (
            jsonify(
                {
                    "error": "Invalid value for query parameter 'results'. Cannot be greater than 20."
                }
            ),
            400,
        )

    # Filter data by category if specified
    filtered_data = (
        [item for item in data if item["category"] == category] if category else data
    )

    # Limit results if the results parameter is provided
    if results:
        filtered_data = filtered_data[:results]

    return jsonify(filtered_data)


if __name__ == "__main__":
    app.run(debug=True)
