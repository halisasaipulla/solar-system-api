from app import db
from app.models.planet import Planet
from flask import Blueprint, request, make_response, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")


@planets_bp.route("", methods=["POST","GET"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "habitable" : planet.habitable

            })
        return jsonify(planets_response)
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                        description=request_body["description"],
                        habitable=request_body["habitable"])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} successfully created", 201)


@planets_bp.route("/<planet_id>", methods=["GET", "PUT", "DELETE"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)
    if planet is None:
        return make_response("Planet does not exist", 404)

    if request.method == "GET":
        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "habitable" : planet.habitable
        }
    elif request.method == "PUT":
        form_data = request.get_json()

        planet.name = form_data["name"]
        planet.description = form_data["description"]
        planet.habitable = form_data["habitable"]

        db.session.commit()

        return make_response(f"Planet #{planet.id} successfully updated")
    elif request.method == "DELETE":
        db.session.delete(planet)
        db.session.commit()
        return make_response(f"Planet #{planet.id} successfully deleted")
