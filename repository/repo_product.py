from sqlalchemy.orm import Session
from config import config_db
from models.models import ModelProduct
from schema.schema_product import SchemaProduct


class RepositoryProducts:

    def __init__(self, session: Session = config_db.SessionLocal()) -> ModelProduct:
        self._session = session

    def insert_product(self, product: SchemaProduct):
        product_to_insert = ModelProduct(id=product.id,
                                         uid=product.uid,
                                         name=product.name,
                                         description=product.description
                                         )
        self._session.add(product_to_insert)
        self._session.commit()
        self._session.refresh(product_to_insert)
        return product_to_insert
