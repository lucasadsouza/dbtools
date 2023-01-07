import datetime, re
import sqlite3 as sqlite
from contextlib import closing

from dbtools.databases.interface import DatabaseInterface
from dbtools.querybuilder.sqlquerybuilder import SQLQueryBuilder
from dbtools.querybuilder.query import Query
from dbtools.on_error import on_error


qb = SQLQueryBuilder()


"""
CONVERTERS & ADAPTERS
"""
def bool_converter(value: int) -> bool:
  return bool(int(value))

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


"""
EXCEPTIONS
"""

class Error(sqlite.Error):
  """Wrapper for sqlite.Error Exception"""

class OperationalError(sqlite.OperationalError):
  """Raised for errors related to the database's operations."""

class InterfaceError(sqlite.InterfaceError):
  """Raised for errors related to the database's interface errors."""

dbtools_sqlite_exceptions = [Error, OperationalError, InterfaceError]


class SQLiteDB(DatabaseInterface):
  def __init__(self, database_path: str):
    self.database_path = database_path

    sqlite.register_adapter(datetime.date, date_iso_adapter)
    sqlite.register_adapter(datetime.datetime, datetime_iso_adapter)

    sqlite.register_converter('boolean', bool_converter)
    sqlite.register_converter('date', date_converter)
    sqlite.register_converter('datetime', datetime_converter)

    self.connection = sqlite.connect(self.database_path, detect_types=sqlite.PARSE_DECLTYPES)

  @on_error(dbtools_sqlite_exceptions)
  def fetch(self, query: Query) -> tuple:
    with closing(self.connection.cursor()) as cursor:
      cursor.execute(query.query, query.values)
      response = cursor.fetchall()

    return response

  @on_error(dbtools_sqlite_exceptions)
  def fetchone(self, query: Query) -> tuple:
    with closing(self.connection.cursor()) as cursor:
      cursor.execute(query.query, query.values)
      response = cursor.fetchone()

    return response

  @on_error(dbtools_sqlite_exceptions)
  def insert(self, query: Query):
    with closing(self.connection.cursor()) as cursor:
      cursor.execute(query.query, query.values)
      self.connection.commit()

  @on_error(dbtools_sqlite_exceptions)
  def update(self, query: Query):
    with closing(self.connection.cursor()) as cursor:
      cursor.execute(query.query, query.values)
      self.connection.commit()

  def exists(self, table: str, **items: any) -> bool:
    where_statement = []
    for idx, (column, value) in enumerate(items.items()):
      where_statement.append(qb.EQUALS(column, value))

      if idx + 1 < len(items):
        where_statement.append(qb.AND)

    if self.fetchone(qb.SELECT(qb.EXISTS(qb.SELECT(1).FROM(table).WHERE(*where_statement).get_query())).get_query())[0]:
      return True

    else:
      return False
