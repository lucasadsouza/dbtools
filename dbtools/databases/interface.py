class DatabaseInterface():
  def fetch(self, query: str, values: tuple=()) -> tuple:
    raise NotImplementedError()

  def fetchone(self, query: str, values: tuple=()) -> tuple:
    raise NotImplementedError()

  def insert(self, query: str, values: tuple=()) -> tuple:
    raise NotImplementedError()

  def update(self, query: str, values: tuple=()) -> tuple:
    raise NotImplementedError()

  def exists(self, table: str, column: str, where: any) -> bool:
    raise NotImplementedError()
