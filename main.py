from config import config_db
from schema.schema_product import SchemaProduct
from repository.repo_product import RepositoryProducts
from uuid import uuid4


config_db.create_db()

product_choco = SchemaProduct(name='Choco',
                              description='Bom',
                              uid=str(uuid4()))

new_product = RepositoryProducts().insert_product(product_choco)

_schema_product = SchemaProduct(id=new_product.id,
                                uid=new_product.uid,
                                name=new_product.name,
                                description=new_product.description)
print(_schema_product)
