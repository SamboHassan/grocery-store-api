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

"""
    URL: https://localhost/carts/:cartId/items

    Method: POST

    Body:
    {
        "productId": 4643,
        "quantity": 2
    }
        
    Response:
    
    {
    "created": true,
    "itemId": 68891739
    },
    201 created

    Data Model: CartModel

    Database: sqlite3
   

"""


@app.route("/carts/<string:cart_id>/items", methods=["POST"])
def add_item_to_cart(cart_id):
    # Extract the request data
    data = request.json

    # Validate the request data
    if "productId" not in data or "quantity" not in data:
        return (
            jsonify(
                {"error": "Request must include 'productId' and 'quantity' parameters."}
            ),
            400,
        )

    # Dummy data for the item ID
    item_id = 68891739

    return jsonify({"created": True, "itemId": item_id}), 201


@app.route("/carts/<string:cart_id>/items", methods=["GET"])
def get_cart_items(cart_id):
    # Dummy data for the cart items
    cart_items = []

    return jsonify(cart_items)


@app.route("/carts/<string:cart_id>", methods=["GET"])
def get_cart(cart_id):
    # Dummy data for the cart
    cart_data = {"items": [], "created": "2025-01-30T16:42:03.316Z"}

    return jsonify(cart_data)


@app.route("/carts", methods=["POST"])
def create_cart():
    # Generate a dummy cart ID
    cart_id = "i8ZUFV6xg8l1nnBBwNA5-"

    return jsonify({"created": True, "cartId": cart_id}), 201


@app.route("/products/<int:product_id>", methods=["GET"])
def get_product(product_id):
    # Find the product with the given ID
    product = next((item for item in data if item["id"] == product_id), None)

    # Return a 404 error if the product is not found
    if product is None:
        return jsonify({"error": "Product not found."}), 404

    return jsonify(product)


@app.route("/products", methods=["POST"])
def add_product():
    # Extract the request data
    data = request.json

    # Validate the request data
    if "category" not in data or "name" not in data or "inStock" not in data:
        return (
            jsonify(
                {
                    "error": "Request must include 'category', 'name', and 'inStock' parameters."
                }
            ),
            400,
        )

    # Add the product to the data
    data.append(data)

    return jsonify(data), 201


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


@app.route("/api-clients", methods=["POST"])
def get_api_key():
    # Extract the request data
    data = request.json

    # Validate the request data
    if "client_id" not in data or "client_secret" not in data:
        return (
            jsonify(
                {
                    "error": "Request must include 'client_id' and 'client_secret' parameters."
                }
            ),
            400,
        )

    # Validate the client_id and client_secret
    if (
        data["client_id"] != "my_client_id"
        or data["client_secret"] != "my_client_secret"
    ):
        return (
            jsonify(
                {
                    "error": "Invalid client credentials. Please check the 'client_id' and 'client_secret'."
                }
            ),
            401,
        )

    # Return the API key
    return jsonify({"api_key": "my_api_key"})

    @app.route("/api-clients", methods=["POST"])
    def register_api_client():
        # Extract the request data
        data = request.json

        # Validate the request data
        if "clientName" not in data or "clientEmail" not in data:
            return (
                jsonify(
                    {
                        "error": "Request must include 'clientName' and 'clientEmail' parameters."
                    }
                ),
                400,
            )

        # Check if the client is already registered (dummy check for example purposes)
        if data["clientEmail"] == "existing_client@example.com":
            return (
                jsonify(
                    {"error": "API client already registered. Try a different email."}
                ),
                409,
            )

        # Generate a dummy access token
        access_token = (
            "523da3d671c40b7885be046ed8aef74493c43eb067983e7f12b8d511bfda56e7"
        )

        # Return the access token
        return jsonify({"accessToken": access_token}), 201


if __name__ == "__main__":
    app.run(debug=True)


"""
    URL: https://localhost/products/:productId

    Method: GET
    Request Body:
    {
        "category": "coffee",
        "name": "Starbucks Coffee Variety Pack, 100% Arabica",
        "inStock": true,
    }
    
    Response:
    {
    "id": 4643,
    "category": "coffee",
    "name": "Starbucks Coffee Variety Pack, 100% Arabica",
    "inStock": true,
    }
    201 created

     """
