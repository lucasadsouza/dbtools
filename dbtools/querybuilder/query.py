class Query():
  def __init__(self, query: str, values: list[any]=None):
    self.query = query
    self.values = tuple(values)
