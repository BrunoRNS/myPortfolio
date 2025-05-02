""" 
Project: server - My Portfolio
Author: Bruno Rian Nunes de Souza
License: GNU General Public License v3.0

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License, version 3, as published
by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.
If not, see <http://www.gnu.org/licenses/>.
"""

from abc import ABC, abstractmethod

### Abstract class for all exceptions in the link_stylesheets module


class LinkStylesheetsException(Exception, ABC):
    """Base class for all exceptions in the link_stylesheets module."""
    @abstractmethod
    def __init__(self, message: str, description: str, *args: object, **kwargs: object) -> None: ...

    @staticmethod
    def __make_message__(message: str, description: str) -> str:
        """Constructs a detailed error message."""
        return f"{message}\n{description}"


### Missing files errors

class ValidationError(LinkStylesheetsException):
    """Exception raised when the stylesheet dictionary is invalid."""
    def __init__(self, message: str = "Invalid stylesheet dictionary.", description: str = "", *args: object, **kwargs: object):
        raise Exception(self.__make_message__(message, description), *args, **kwargs)

class MissedscssException(LinkStylesheetsException):
    """Exception raised when missed scss files in the stylesheet dictionary."""
    def __init__(self, message: str = "SCSS files are missing. Please check the stylesheet context of the template.", description: str = "", *args: object, **kwargs: object):
        raise Exception(self.__make_message__(message, description), *args, **kwargs)

class MissedcssException(LinkStylesheetsException):
    """Exception raised when missed css files in the stylesheet dictionary."""
    def __init__(self, message: str = "CSS files are missing. Please check the stylesheet context of the template.", description: str = "", *args: object, **kwargs: object):
        raise Exception(self.__make_message__(message, description), *args, **kwargs)


### Missing template name error


class MissedtemplateException(LinkStylesheetsException):
    """Exception raised when missed template name in the stylesheet dictionary."""
    def __init__(self, message="Did you forget to add the template name?", description="", *args: object, **kwargs: object):
        raise Exception(self.__make_message__(message, description), *args, **kwargs)


### Type Errors


class NotdictException(LinkStylesheetsException):
    """Exception raised when a dictionary is expected but not provided."""
    def __init__(self, message="Expected a dictionary, but received a different type.", description="", *args: object, **kwargs: object):
        raise Exception(self.__make_message__(message, description), *args, **kwargs)

class NotlistException(LinkStylesheetsException):
    """Exception raised when a list is expected but not provided."""
    def __init__(self, message="Expected a list, but received a different type.", description="", *args: object, **kwargs: object):
        raise Exception(self.__make_message__(message, description), *args, **kwargs)

class NotstrException(LinkStylesheetsException):
    """Exception raised when a string is expected but not provided."""
    def __init__(self, message="Expected a string, but received a different type.", description="", *args: object, **kwargs: object):
        raise Exception(self.__make_message__(message, description), *args, **kwargs)