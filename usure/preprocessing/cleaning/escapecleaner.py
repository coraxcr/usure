import re
from .cleaner import Cleaner


class EscapeCleaner(Cleaner):

    def __init__(self):
        self._escape_pattern = re.compile("(\\\\n)|(\\\\\")")

    def clean(self, text: str) -> str:
        result = self._escape_pattern.sub(" ", text)
        return result
