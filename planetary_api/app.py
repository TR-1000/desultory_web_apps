from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import Column, Integer, String, Float
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_mail import Mail, Message # set up mail server eventually



app = Flask(__name__)
# basedir = os.path.abspath(os.path.dirname(__file__))
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'planets.db')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:@localhost:5432/planetary_api'
app.config['JWT_SECRET_KEY'] = 'super-secret' # change this IRL
db = SQLAlchemy(app)
migrate = Migrate(app,db)
ma = Marshmallow(app)
jwt = JWTManager(app)



# CLI commands to initiate the postgres db, enabling migrations and execute the migration and create the table.
# flask db init
# flask db migrate
# flask db upgrade


@app.cli.command('db_create') # I don't think we need this using postgres
def db_create():
    db.create_all()
    print('Database created!')


@app.cli.command('db_drop')
def db_drop():
    db.drop_all()
    print('Database dropped!')


@app.cli.command('db_seed')
def db_seed():
    mercury = Planet(planet_name='Mercury',
                     planet_type='Class D',
                     home_star='Sol',
                     mass=2.258e23,
                     radius=1516,
                     distance=35.98e6)

    venus = Planet(planet_name='Venus',
                         planet_type='Class K',
                         home_star='Sol',
                         mass=4.867e24,
                         radius=3760,
                         distance=67.24e6)

    earth = Planet(planet_name='Earth',
                     planet_type='Class M',
                     home_star='Sol',
                     mass=5.972e24,
                     radius=3959,
                     distance=92.96e6)

    db.session.add(mercury)
    db.session.add(venus)
    db.session.add(earth)


    test_user = User(first_name='William',
                     last_name='Herschel',
                     email='test@test.com',
                     password='P@ssw0rd')

    db.session.add(test_user)
    db.session.commit()
    print('Database seeded!')




# ======================== #
# =========ROUTES========= #
# ======================== #

@app.route('/')
def hello_world():
    return('Hello, World!')


@app.route('/greetings')
def greetings():
    # return 'Hello from the Planetary API.'
    return jsonify(message='Hello from the Planetary API.')

@app.route('/not_found')
def not_found():
    return jsonify(message='That resource was not found'), 404


# Adding parameters to api end points
@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message=f"Sorry, {name}. At {age} years of age you're not old enough to access this API.")
    else:
        return jsonify(message=f"Welcome to the API, {name}!")


# URL variables
@app.route('/url_variables/<string:name>/<int:age>')
def url_variables(name: str, age: int):
    if age < 18:
        return jsonify(message=f"Sorry, {name}. At {age} years of age you're not old enough to access this API.")
    else:
        return jsonify(message=f"Welcome to the API, {name}!")


@app.route('/planets', methods=['GET'])
def planets():
    planets_list = Planet.query.all()
    result = planets_schema.dump(planets_list)
    # return jsonify(result.data) didn't work. had to remove .data
    return jsonify(result)


@app.route('/planet_search', methods=['GET'])
def planet_search():
    search = request.form['search']
    found_planets = Planet.query.filter(Planet.planet_name.ilike(f'%{search}%'))
    result = planets_schema.dump(found_planets)
    return jsonify(result)


@app.route('/planet_details/<int:planet_id>', methods=['GET'])
def planet_details(planet_id: int):
    planet = Planet.query.filter_by(planet_id=planet_id).first()
    if planet:
        result = planet_schema.dump(planet)
        # return jsonify(result.data)
        return jsonify(result)
    else:
        return jsonify(message='That planet does not exist...yet'), 404


@app.route('/add_planet', methods=['POST'])
@jwt_required
def add_planet():
    planet_name = request.form['planet_name']
    test = Planet.query.filter_by(planet_name=planet_name).first()
    if test:
        return jsonify('There is already a planet by that name'), 409
    else:
        planet_type = request.form['planet_type']
        home_star = request.form['home_star']
        mass = float(request.form['mass'])
        radius = float(request.form['radius'])
        distance = float(request.form['distance'])

        new_planet = Planet(planet_name=planet_name,
                            planet_type=planet_type,
                            home_star=home_star,
                            mass=mass,
                            radius=radius,
                            distance=distance)
        db.session.add(new_planet)
        db.session.commit()
        return jsonify(message='You added a planet!'), 201


@app.route('/update_planet', methods=['PUT'])
@jwt_required
def update_planet():
    planet_id = int(request.form['planet_id'])
    planet = Planet.query.filter_by(planet_id=planet_id).first()
    if planet:
        planet.planet_name = request.form['planet_name']
        planet.planet_type = request.form['planet_type']
        planet.home_star = request.form['home_star']
        planet.mass = float(request.form['mass'])
        planet.radius = float(request.form['radius'])
        planet.distance = float(request.form['distance'])
        db.session.commit()
        return jsonify(message='You updated a planet'), 202
    else:
        return jsonify(Message='That planet doesn\'t exist'), 404


@app.route('/remove_planet/<int:planet_id>', methods=['DELETE'])
@jwt_required
def remove_planet(planet_id: int):
    planet = Planet.query.filter_by(planet_id=planet_id).first()
    if planet:
        db.session.delete(planet)
        db.session.commit()
        return jsonify(message='You\'ve deleted a planet'), 202
    else:
        return jsonify(message='That planet does not exist'),404




@app.route('/register', methods=['POST'])
def register():
    #FORM DATA
    email = request.form['email']
    test = User.query.filter_by(email=email).first()
    if test:
        return jsonify(message='That email already exists.'), 409
    else:
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        password = request.form['password']
        user = User(first_name=first_name, last_name=last_name, email=email, password=password)
        db.session.add(user)
        db.session.commit()
        return jsonify(message='User created successfully.'),201


@app.route('/login', methods=['POST'])
def login():
    #JSON DATA
    if request.is_json:
        email = request.json['email']
        password = request.json['password']
    else:
    #FORM DATA
        email = request.form['email']
        password = request.form['password']

    test = User.query.filter_by(email=email, password=password).first()
    if test:
        access_token = create_access_token(identity=email)
        return jsonify(message='Login successful!', access_token=access_token)
    else:
        return jsonify(message='Invalid email or password.'), 401





# ======================== #
# =====DATABASE MODELS==== #
# ======================== #

class User(db.Model):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String, unique=True)
    password = Column(String)

class Planet(db.Model):
    __tablename__ = 'planets'
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String)
    planet_type = Column(String)
    home_star = Column(String)
    mass = Column(Float)
    radius = Column(Float)
    distance = Column(Float)


class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'first_name', 'last_name', 'email', 'password')

class PlanetSchema(ma.Schema):
    class Meta:
        fields = ('planet_id', 'planet_name', 'planet_type', 'home_star', 'mass', 'radius', 'distance')


user_schema = UserSchema()
users_schema = UserSchema(many=True)

planet_schema = PlanetSchema()
planets_schema = PlanetSchema(many=True)








if __name__ == '__main__':
    app.run()
# app.run(port=5000)            If we want to run server on port 5000

#COMMANDS
# $env:FLASK_APP = "app.py"     Export the FLASK_APP environment variable
# $env:FLASK_ENV="development"  Turn on # DEBUG mode
# python -m flask run           Run the application
