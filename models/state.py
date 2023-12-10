<<<<<<< HEAD
#!/usr/bin/python3
"""Module for State
"""
from models.base_model import BaseModel


class State(BaseModel):
    """Class for State
    Arguments:
        name (str)
    """
    name = ""
=======
#!/user/bin/python3
"""
Module to hold class state
"""


from .base_model import BaseModel


class state(BaseModel):
    """
    class representing a state
    """

    name = ""

    def _init_(self, *args, **kwargs):
        if len(kwargs) > 0:
            super().__init__(**kwargs)
        else:
            super().__init__()
>>>>>>> 458f2a7e3e862a9d1c300022b34b0ac81e8a0a51
