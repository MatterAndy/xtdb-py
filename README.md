# XTDB Python

An ORM for XTDB.



## Installation

```bash
poetry install
```

## Usage


```python
import os
from dataclasses import dataclass, field

from xtdb.orm import Base
from xtdb.query import Query
from xtdb.session import XTDBSession


@dataclass
class TestEntity(Base):
    name: str = field(default_factory=str)


@dataclass
class SecondEntity(Base):
    age: int = field(default_factory=int)
    test_entity: TestEntity = field(default_factory=TestEntity)


session = XTDBSession(os.environ["XTDB_URI"])

entity = TestEntity(name="test")
session.put(entity)
session.commit()

query = Query(TestEntity).where(TestEntity, name="test")
result = session.query(query)

assert result == [[{"TestEntity/name": "test", "type": "TestEntity", "xt/id": entity._pk}]]
```
