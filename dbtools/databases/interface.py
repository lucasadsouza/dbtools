from dbtools.querybuilder.query import Query

class DatabaseInterface():
  def fetch(self, query: Query) -> tuple:
    raise NotImplementedError()

  def fetchone(self, query: Query) -> tuple:
    raise NotImplementedError()

  def insert(self, query: Query) -> tuple:
    raise NotImplementedError()

  def update(self, query: Query) -> tuple:
    raise NotImplementedError()

  def exists(self, table: str, **items: any) -> bool:
    raise NotImplementedError()
