from datetime import datetime


class Hello(object):
    def __init__(self, message: str) -> None:
        self.message: str = message

    def __str__(self) -> str:
        return f'{datetime.now()}:\t{self.message} and I fucking hate that!'
