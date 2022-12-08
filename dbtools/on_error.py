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
            tb = sys.exc_info()[2]
            message = traceback.format_exception_only(type(error), error)[0]

            traceback_message = traceback.format_tb(tb)[-1]
            traceback_message = f'{traceback_message}\n    {message}'

            print(traceback_message)

    return wrapped

  return decorated
