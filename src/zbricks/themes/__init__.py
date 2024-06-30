from typing import Any, Optional
from ..core import zBrick
import os

class Theme(zBrick):
    pass

class DefaultTheme(Theme):
    def _attach_to(self, host: Any, label: Optional[str] = None):
        # print(f"Theme: Attaching {self} to {host}")
        file_path = os.path.dirname(os.path.abspath(__file__))
        print(f"\n Theme: file_path = {file_path}")
        theme_path = os.path.abspath(os.path.join(file_path, 'templates'))
        host.jinja_loader.searchpath.insert(0, theme_path)