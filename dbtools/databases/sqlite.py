import sqlite3 as sqlite
from contextlib import closing

from dbtools.databases.interface import DatabaseInterface


def bool_adapter(value: bool) -> int:
  return 1 if bool else 0

def bool_converter(value: int) -> bool:
  return bool(int)


class SQLiteDB(DatabaseInterface):
  def __init__(self, database_path: str):
    self.database_path = database_path

    sqlite.register_converter('boolean', bool_converter)

    self.connection = sqlite.connect(self.database_path, detect_types=sqlite.PARSE_DECLTYPES)

  def fetch(self, query: str, values:tuple=()) -> tuple:
    with closing(self.connection.cursor()) as cursor:
      cursor.execute(query, values)
      response = cursor.fetchall()

    return response

  def fetchone(self, query: str, values:tuple=()) -> tuple:
    with closing(self.connection.cursor()) as cursor:
      cursor.execute(query, values)
      response = cursor.fetchone()

    return response

  def insert(self, query: str, values:tuple=()):
    with closing(self.connection.cursor()) as cursor:
      cursor.execute(query, values)
      self.connection.commit()

  def update(self, query: str, values:tuple=()):
    with closing(self.connection.cursor()) as cursor:
      cursor.execute(query, values)
      self.connection.commit()

  def exists(self, table: str, column: str, value: any) -> bool:
    if self.fetchone(f'SELECT EXISTS(SELECT 1 FROM {table} WHERE {column} = ?);', (value,))[0]:
      return True

    else:
      return False
