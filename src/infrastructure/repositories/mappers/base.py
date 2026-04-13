from typing import TypeVar
from pydantic import BaseModel

from infrastructure.models.base import BaseOrm

DBModelType = TypeVar("SchemaType", bound=BaseOrm)
SchemaType = TypeVar("SchemaType", bound=BaseModel)


class BaseDataMapper:
    db_model: type[DBModelType] = None
    schema: type[SchemaType] = None

    @classmethod
    def map_to_domain_entity(cls, model_data):
        return cls.schema.model_validate(model_data, from_attributes=True)

    @classmethod
    def map_to_persistence_entity(cls, schema_data):
        return cls.db_model(**schema_data.model_dump())
