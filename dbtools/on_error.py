import functools, traceback, sys


def on_error(exceptions: Exception):
  def decorated(f: callable):
    @functools.wraps(f)
    def wrapped(*args, **kwargs):
      try:
        return f(*args, **kwargs)

      except Exception as e:
        for error in exceptions:
          if issubclass(error, type(e)):
            error = error(str(e))

      raise error

    return wrapped

  return decorated
