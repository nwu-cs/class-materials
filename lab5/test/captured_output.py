import sys
from contextlib import contextmanager
from io import StringIO

@contextmanager
def captured_output():
    """Capture standard out or standard error into a string

    Example:
         with captured_output() as (out, err):
            self.cmd.default('invalidfoo')

        self.assertEqual("E 00\n*", out.getvalue().strip())
    """
    new_out, new_err = StringIO(), StringIO()
    old_out, old_err = sys.stdout, sys.stderr
    try:
        sys.stdout, sys.stderr = new_out, new_err
        yield sys.stdout, sys.stderr
    finally:
        sys.stdout, sys.stderr = old_out, old_err
