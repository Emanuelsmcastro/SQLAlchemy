from sqlalchemy import Column, Integer, String, Float
from config.config_db import Base


class ModelProduct(Base):
    __tablename__ = 'product'
    id = Column(Integer, primary_key=True)
    uid = Column(String)
    name = Column(String)
    description = Column(String)
    rating = Column(Float)
