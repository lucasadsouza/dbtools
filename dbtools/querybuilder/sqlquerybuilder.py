from dbtools.querybuilder.interface import QueryBuilderInterface


class SQLQueryBuilder(QueryBuilderInterface):
  query = ''

  # Constants:
  NULL = 'NULL'

  # SELECT Constants:
  ALL = '*'

  # ORDER_BY Constants:
  DESC = 'DESC'
  ASC = 'ASC'

  # STATEMENT Constants:
  IS = 'IS'
  IS_NOT = 'IS NOT'
  AND = 'AND'
  AND_NOT = 'AND NOT'
  OR = 'OR'
  OR_NOT = 'OR NOT'
  NOT = 'NOT'
  ON = 'ON'

  def join(self, values: list or list, quote_mark: bool=False) -> str:
    temp_list = []
    for value in values:
      if quote_mark and type(value) == str:
        value = f'"{value}"'

      if type(value) == int or type(value) == float:
        value = str(value)

      temp_list.append(value)

    return ', '.join(temp_list)

  def get_query(self):
    return f'{self.query};'

  # Primary:
  def SELECT(self, *columns: str or int) -> object:
    self.query = f'SELECT {self.join(columns)}'

    return self

  def INSERT_INTO(self, table: str, columns: list[str]=[]) -> object:
    self.query = f'INSERT INTO {table}'

    if columns:
      self.query += f'({self.join(columns)})'

    return self

  def UPDATE(self, table: str) -> str:
    self.query = f'UPDATE {table}'

    return self

  def DELETE_FROM(self, table: str) -> str:
    self.query = f'DELETE FROM {table}'

    return self

  def EXISTS(self, query: str) -> object:
    raise NotImplementedError('EXISTS not implemented.')

  # Secundary:
  def FROM(self, table: str) -> object:
    self.query = f'{self.query} FROM {table}'

    return self

  def SET(self, column: str, value: str or int or float or bytes) -> object:
    if type(value) == str:
      value = f'"{value}"'

    self.query = f'{self.query} SET {column}={value}'

    return self

  def VALUES(self, *values: str or int or float or bytes) -> object:
    self.query = f'{self.query} VALUES({self.join(values, True)})'

    return self

  # Terciary:
  def WHERE(self, *statements: str or int or float or bytes or tuple) -> object:
    self.query = f'{self.query} WHERE {self.STATEMENT(*statements)}'

    return self

  def ORDER_BY(self, *columns: str) -> object:
    self.query = f'{self.query} ORDER BY {self.join(columns)}'

    return self

  def INNER_JOIN(self, *statements: str or int or float or bytes or tuple) -> object:
    raise NotImplementedError('INNER_JOIN not implemented.')

  # Conditions:
  def EQUALS(self, column: str, value: str or int or float or bytes) -> str:
    if type(value) == str:
      value = f"'{value}'"

    return f'{column}={value}'

  def NOT_EQUAL(self, column: str, value: str or int or float or bytes) -> str:
    raise NotImplementedError('NOT_EQUAL not implemented.')

  def GREATER(self, column: str, value: str or int or float or bytes) -> str:
    raise NotImplementedError('GREATER not implemented.')

  def LESS(self, column: str, value: str or int or float or bytes) -> str:
    raise NotImplementedError('LESS not implemented.')

  def GREATER_OR_EQUAL(self, column: str, value: str or int or float or bytes) -> str:
    raise NotImplementedError('GREATER_OR_EQUAL not implemented.')

  def LESS_OR_EQUAL(self, column: str, value: str or int or float or bytes) -> str:
    raise NotImplementedError('LESS_OR_EQUAL not implemented.')

  def BETWEEN(self, column: str, first_value: str or int or float or bytes, second_value: str or int or float or bytes) -> str:
    raise NotImplementedError('BETWEEN not implemented.')

  def LIKE(self, column: str, pattern: str) -> str:
    raise NotImplementedError('LIKE not implemented.')

  def NOT_LIKE(self, column: str, pattern: str) -> str:
    raise NotImplementedError('NOT_LIKE not implemented.')

  def IN(self, column: str, values_list: list[str or int or float or bytes]) -> str:
    raise NotImplementedError('IN not implemented.')

  def NOT_IN(self, column: str, values_list: list[str or int or float or bytes]) -> str:
    raise NotImplementedError('NOT_IN not implemented.')

  # Others:
  def ASC(self) -> object:
    self.query = f'{self.query} ASC'

    return self

  def DESC(self) -> object:
    self.query = f'{self.query} DESC'

    return self

  def AS(self, name: str, alias: str) -> str:
    raise NotImplementedError('AS not implemented.')

  # Not chainable:
  def STATEMENT(self, *statements: str or int or float or bytes or tuple) -> str:
    query = ''

    for statement in statements:
      if type(statement) == tuple:
        tuple_query = ''
        for tuple_statement in statement:
          tuple_query = f'{tuple_query} {tuple_statement}'

        statement = f'({tuple_query.strip()})'

      query = f'{query} {statement}'

    return query.strip()

  def PRAGMA_TABLE_INFO(self, table: str) -> str:
    return f'PRAGMA_TABLE_INFO("{table}")'
