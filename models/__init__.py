#!/usr/bin/python3
"""initialise the storage model """
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
