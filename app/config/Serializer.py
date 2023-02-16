# Serialization 
# This file is part of the Flask-AppBuilder app

from flask_appbuilder import Model
from flask_appbuilder.models.mixins import AuditMixin, FileColumn, ImageColumn

class MyModel(Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(150), unique = True, nullable=False)
    description = db.Column(db.Text)

class MyModelView(ModelView):
    datamodel = SQLAInterface(MyModel)
    list_columns = ['name', 'description']

    