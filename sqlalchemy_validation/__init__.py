"""
SQLAlchemy Validation

Example:

from sqlalchemy_validation import Model, Column

class User(Base):
    __tablename__ = "users"
    name = Column(mysql.VARCHAR(20), primary_key=True,
                  regexp=re.compile(r"[-._0-9a-z]{4,10}"))
    email = Column(mysql.VARCHAR(50), nullable=False, unique=True)
    age = Column(mysql.INTEGER, default=20, nullable=False)
    status = Column(mysql.ENUM("active", "leaved"), nullable=False)
"""

from .model import Model, MetaClass, metadata, BaseModel
from .column import Column
from .attribute import validate_attribute
from .error import *
from .validate_column import ColumnValidator
from .util import validate, validates, convert_model_to_dict
