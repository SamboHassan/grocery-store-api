from app.main import bp

users = [
    {"firstname": "Umar", "lastname": "Sadiya", "occupation": "Developer"},
    {"firstname": "Aisha", "lastname": "Tanko", "occupation": "UI Designer"},
]


@bp.route("/index", methods=["GET"])
def index():
    return {"users": users}
