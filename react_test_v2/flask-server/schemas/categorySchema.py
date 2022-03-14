from flask_marshmallow import Marshmallow
from schemas.ma import ma

class CategorySchema(ma.Schema):
    class Meta:
        fields = ('cat_id', 'cat_nom', 'cat_desp')
