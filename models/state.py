#!/user/bin/python3
"""
Module to hold class State
"""


from .base_model import BaseModel


class state(BaseModel):
    """
    class representing a State
    """

    name = ""

    def _init_(self, *args, **kwargs):
        if len(kwargs) > 0:
            super()._init_(**kwargs)
        else:
            super()._init_()
