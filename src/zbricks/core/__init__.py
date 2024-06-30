from typing import Any, Optional, Type, Protocol, Union
from flask import Flask

class AttachableMixin:
    def _attach_to(self, host: Any, label: Optional[str] = None):
        print(f"Attaching {self} to {host}")
        raise NotImplementedError(f"{self} cannot be attached to {host} as {label}")
    
class Attachable(Protocol):
    def _attach_to(self, host: Any, label: Optional[str] = None):
        ...

class zBrick(AttachableMixin):
    def __init__(self, *args, **kwargs):
        print()
        print(f"zBrick.__init__({args}, {kwargs})")
        super().__init__(*args, **kwargs)
    
    def attach(self, brick : Attachable, label: Optional[str] = None):
        brick._attach_to(self, label)

