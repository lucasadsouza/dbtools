from dbtools.querybuilder.query import Query


class QueryBuilderInterface():
  query: str
  values: list

  # Constants:
  NULL: str

  # SELECT Constants:
  ALL: str

  # ORDER_BY Constants:
  DESC: str
  ASC: str

  # STATEMENT Constants:
  IS: str
  IS_NOT: str
  AND: str
  AND_NOT: str
  OR: str
  OR_NOT: str
  NOT: str
  ON: str

  # CREATE TABLE arguments:
  PRIMARY_KEY: str
  AUTO_INCREMENT: str
  NOT_NULL: str
  UNIQUE: str

  def join(self, values: list, quote_mark: bool=False) -> str:
    raise NotImplementedError('join not implemented.')

  def get_query(self) -> Query:
    raise NotImplementedError('get_query not implemented.')

  # Primary:
  def SELECT(self, *column_names: str or int) -> object:
    raise NotImplementedError('SELECT not implemented.')

  def CREATE_TABLE(self, table_name: str, columns: dict) -> object:
    raise NotImplementedError('CREATE_TABLE not implemented.')

  def INSERT_INTO(self, table: str, columns: list[str]=[]) -> object:
    raise NotImplementedError('INSERT_INTO not implemented.')

  def UPDATE(self, table: str) -> object:
    raise NotImplementedError('UPDATE not implemented.')

  def DELETE_FROM(self, table: str) -> object:
    raise NotImplementedError('DELETE_FROM not implemented.')

  def EXISTS(self, query: Query) -> str:
    raise NotImplementedError('EXISTS not implemented.')

  # Secundary:
  def FROM(self, table: str) -> object:
    raise NotImplementedError('FROM not implemented.')

  def SET(self, **items: any) -> object:
    raise NotImplementedError('SET not implemented.')

  def VALUES(self, *values: any) -> object:
    raise NotImplementedError('VALUES not implemented.')

  # Terciary:
  def WHERE(self, *statements: str or int or float or tuple) -> object:
    raise NotImplementedError('WHERE not implemented.')

  def ORDER_BY(self, *columns: str) -> object:
    raise NotImplementedError('ORDER_BY not implemented.')

  def INNER_JOIN(self, *statements: str or int or float or tuple) -> object:
    raise NotImplementedError('INNER_JOIN not implemented.')

  # Conditions:
  def EQUALS(self, column: str, value: str or int or float) -> str:
    raise NotImplementedError('EQUALS not implemented.')

  def NOT_EQUAL(self, column: str, value: str or int or float) -> str:
    raise NotImplementedError('NOT_EQUAL not implemented.')

  def GREATER(self, column: str, value: str or int or float) -> str:
    raise NotImplementedError('GREATER not implemented.')

  def LESS(self, column: str, value: str or int or float) -> str:
    raise NotImplementedError('LESS not implemented.')

  def GREATER_OR_EQUAL(self, column: str, value: str or int or float) -> str:
    raise NotImplementedError('GREATER_OR_EQUAL not implemented.')

  def LESS_OR_EQUAL(self, column: str, value: str or int or float) -> str:
    raise NotImplementedError('LESS_OR_EQUAL not implemented.')

  def BETWEEN(self, column: str, first_value: str or int or float, second_value: str or int or float) -> str:
    raise NotImplementedError('BETWEEN not implemented.')

  def LIKE(self, column: str, pattern: str) -> str:
    raise NotImplementedError('LIKE not implemented.')

  def NOT_LIKE(self, column: str, pattern: str) -> str:
    raise NotImplementedError('NOT_LIKE not implemented.')

  def IN(self, column: str, values_list: list[str or int or float]) -> str:
    raise NotImplementedError('IN not implemented.')

  def NOT_IN(self, column: str, values_list: list[str or int or float]) -> str:
    raise NotImplementedError('NOT_IN not implemented.')

  # Datatypes:
  def INTEGER(self, length: int) -> str:
    raise NotImplementedError('INTEGER not implemented.')

  def TEXT(self, length: int) -> str:
    raise NotImplementedError('TEXT not implemented.')

  # Others:
  def ASC(self) -> object:
    raise NotImplementedError('ASC not implemented.')

  def DESC(self) -> object:
    raise NotImplementedError('DESC not implemented.')

  def AS(self, name: str, alias: str) -> str:
    raise NotImplementedError('AS not implemented.')

  # Not chainable:
  def STATEMENT(self, statements: str or int or float or tuple) -> str:
    raise NotImplementedError('STATEMENT not implemented.')

  def PRAGMA_TABLE_INFO(self, table: str) -> str:
    raise NotImplementedError('PRAGMA_TABLE_INFO not implemented.')
