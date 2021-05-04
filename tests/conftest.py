import pytest
from app import create_app
from app import db

from app.models.planet import Planet
# ...

@pytest.fixture
def two_saved_planets(app):
    # Arrange
    mars_planet = Planet(name="Mars",
                    description="4th planet",
                    habitable="False"
                    )
    venus_planet = Planet(name="Venus",
                    description="2nd planet", 
                    habitable="False"
                    )

    db.session.add_all([mars_planet, venus_planet])
    # Alternatively, we could do
    # db.session.add(ocean_book)
    # db.session.add(mountain_book)
    db.session.commit()

@pytest.fixture
def app():
    app = create_app({"TESTING": True})

    with app.app_context():
        db.create_all()
        yield app

    with app.app_context():
        db.drop_all()


@pytest.fixture
def client(app):
    return app.test_client()