import datetime, re
import sqlite3 as sqlite
from contextlib import closing

from dbtools.databases.interface import DatabaseInterface


def bool_converter(value: int) -> bool:
  return bool(int)


def date_iso_adapter(value: datetime.datetime) -> str:
  return value.isoformat()

def datetime_iso_adapter(value: datetime.datetime) -> str:
  return value.isoformat()

def date_converter(value: bytes) -> datetime.date:
  return datetime.date.fromisoformat(value.decode())

def datetime_converter(value: bytes) -> datetime.datetime:
  tz = re.search(r'(?P<tzinfo>Z|[+-]\d{2}(?::?\d{2})?)?$', value.decode(), re.MULTILINE)

  if tz == None:
    tz = datetime.timezone.utc

  else:
    tz = tz.groupdict()['tzinfo']
    hours = -int(tz[:3]) if tz[0] == '-' else int(tz[:3])
    tz = datetime.timezone(datetime.timedelta(hours=hours))

  return datetime.datetime.fromisoformat(value.decode()).replace(tzinfo=tz)


class SQLiteDB(DatabaseInterface):
  def __init__(self, database_path: str):
    self.database_path = database_path

    sqlite.register_adapter(datetime.date, date_iso_adapter)
    sqlite.register_adapter(datetime.datetime, datetime_iso_adapter)

    sqlite.register_converter('boolean', bool_converter)
    sqlite.register_converter('date', date_converter)
    sqlite.register_converter('datetime', datetime_converter)

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
