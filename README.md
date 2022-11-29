# DBTools

A module to handle database connections with a wrapper for the database modules and offers an easy to use querybuilder for SQL statements.

## Features:
- SQLite wrapper (on going)
- SQL Query Builder (on going)

## Quick Example:
**SQLite**
```python
import dbtools


qb = dbtools.querybuilder.SQLQueryBuilder()

DogsDatabase(dbtools.databases.SQLiteDB):
  def __init__(self, database_path: str):
    super().__init__(database_path)

  def fetch_dog(self, name: str):
    return self.fetchone(qb.SELECT(qb.ALL).FROM('dogs').WHERE(qb.EQUALS('name', name)).get_query())

  def fetch_dogs(self):
    return self.fetch(qb.SELECT(qb.ALL).FROM('dogs').get_query())

  def new_dog(self, name: str, age: int):
    self.insert(qb.INSERT_INTO('dogs').VALUES(name, age))


dogsdb = DogsDatabase('database/dogs.db')

dogsdb.new_dog('Pluto', 9)

print(dogsdb.fetch_dog('Pluto'))
# output: ('Pluto', 9)
```

_* It is updated according personal uses._
