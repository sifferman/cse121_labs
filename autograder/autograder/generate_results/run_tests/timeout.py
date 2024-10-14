import signal

# source: https://stackoverflow.com/a/49567288
class TimeoutError(Exception):
    pass

class TimeoutTimer:
    def __init__(self, seconds, error_message=None):
        if error_message is None:
          error_message = f'test timed out after {seconds}s.'
        self.seconds = seconds
        self.error_message = error_message

    def handle_timeout(self, signum, frame):
        raise TimeoutError(self.error_message)

    def __enter__(self):
        signal.signal(signal.SIGALRM, self.handle_timeout)
        signal.alarm(self.seconds)

    def __exit__(self, exc_type, exc_val, exc_tb):
        signal.alarm(0)
