"""
The utils package.
"""
from __future__ import annotations
from kivy.app import App
from dataclasses import dataclass, field
from typing import ClassVar,Any
from pathlib import Path
import json, os

app = App.get_running_app()
""" Instance of the running App, or None if no App is running."""
from .preloadJS import PreloadJs

__all_=["PreloadJs", "app", "Path",
        "json", "os", "dataclass",
        "field", "ClassVar", "Any"]