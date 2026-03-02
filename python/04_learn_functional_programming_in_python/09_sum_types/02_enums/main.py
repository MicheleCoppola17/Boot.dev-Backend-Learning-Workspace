"""
Assignment
Create an Enum called Doctype with values:

PDF
TXT
DOCX
MD
HTML
"""
from enum import Enum

class Doctype(Enum):
    PDF = 1
    TXT = 2
    DOCX = 3
    MD = 4
    HTML = 5