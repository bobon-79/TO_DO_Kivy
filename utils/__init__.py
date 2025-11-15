"""
The utils package.
"""
from kivy.app import App
from dataclasses import dataclass, field
from typing import ClassVar, Any
from pathlib import Path
import json, os

app = App.get_running_app()
""" Instance of the running App, or None if no App is running."""
from .preloadJS import PreloadJs

CREATE_META_TABLE = """
       CREATE TABLE IF NOT EXISTS meta (
         key   TEXT PRIMARY KEY,
         value TEXT
       )
       """

GET_META_VERSION = "SELECT value FROM meta WHERE key='schema_version'"


SET_META_VERSION = """
INSERT INTO meta(key,value)
VALUES('schema_version', ?)
ON CONFLICT(key) DO UPDATE SET value=excluded.value
"""
__all_ = ["PreloadJs", "app", "Path",
          "json", "os", "dataclass",
          "field", "ClassVar", "Any",
          "CREATE_META_TABLE", "GET_META_VERSION",
          "SET_META_VERSION"]
