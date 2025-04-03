from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

# Routes

# Home Route.
@app.route('/')
def home():
    return jsonify({"message": "Hello! Welcome to Superpower Management APi"})

# Heroes Route 
@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    heroes_dict = [{"id": hero.id, "name": hero.name, "super_name": hero.super_name} for hero in heroes]
    return jsonify(heroes_dict)

@app.route('/heroes/<int:id>', methods=['GET'])
def get_hero(id):
    hero = Hero.query.get(id)
    
    if not hero:
        return jsonify({"error": "Hero not found"}), 404
    
    return jsonify(hero.to_dict(rules=('-hero_powers.hero',)))

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    
    try:
        hero = Hero.query.get(data.get('hero_id'))
        power = Power.query.get(data.get('power_id'))
        
        if not hero or not power:
            return jsonify({"errors": ["Hero or Power not found"]}), 404
        
        new_hero_power = HeroPower(
            strength=data['strength'],
            hero_id=data['hero_id'],
            power_id=data['power_id']
        )
        
        db.session.add(new_hero_power)
        db.session.commit()
        
        return jsonify(new_hero_power.to_dict(rules=('-power.hero_powers', '-hero.hero_powers')))
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400

# Powers Route
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    return jsonify([power.to_dict(only=('id', 'name', 'description')) for power in powers])

@app.route('/powers/<int:id>', methods=['GET'])
def get_power(id):
    power = Power.query.get(id)
    
    if not power:
        return jsonify({"error": "Power not found"}), 404
    
    return jsonify(power.to_dict(only=('id', 'name', 'description')))

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    
    if not power:
        return jsonify({"error": "Power not found"}), 404
    
    data = request.get_json()
    
    try:
        if 'description' in data:
            power.description = data['description']
        
        db.session.commit()
        return jsonify(power.to_dict(only=('id', 'name', 'description')))
    except ValueError as e:
        return jsonify({"errors": [str(e)]}), 400

if __name__ == '__main__':
    app.run(port=5555, debug=True)