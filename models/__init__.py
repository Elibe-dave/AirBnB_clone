#!/usr/bin/python3
"""Initializes the package."""
from models.engine.file_storage import FileStorage

# Create an instance of FileStorage and reload data
storage = FileStorage()
storage.reload()
