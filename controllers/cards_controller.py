from flask import Blueprint

from db import db
from models.card import Card, CardSchema

cards_bp = Blueprint(
    "cards", __name__, url_prefix="/cards"
)  # First is name, second is import_name


@cards_bp.route("/")
# @jwt_required()
def all_cards():
    # if not authorize():
    #     return {"error": "You must be an admin"}, 401
    stmt = db.select(Card).order_by(Card.priority.desc(), Card.title)
    cards = db.session.scalars(stmt)
    return CardSchema(many=True).dump(cards)

    # return "all_cards route"

@cards_bp.route('/<int:id>/')
def one_card(id):
    stmt = db.select(Card).filter_by(id=id)
    card = db.session.scalar(stmt)
    return CardSchema().dump(card)
    