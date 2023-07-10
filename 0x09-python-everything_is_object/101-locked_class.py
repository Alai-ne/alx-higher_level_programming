#!/usr/bin/python3
"""Defines a locked class."""
class LockedClass:

    """
    Prevent  The user from instatiating new LockedClass attributes for anything But attributes called 'first_name'
    """

    __slots__ = ["first_name"]
