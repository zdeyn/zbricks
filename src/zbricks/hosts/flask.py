from typing import Optional
from flask import Flask
from ..core import zBrick, Attachable

class zFlask(Flask, zBrick):
    def attach(self, brick : Attachable, label: Optional[str] = None):
        brick._attach_to(self, label)