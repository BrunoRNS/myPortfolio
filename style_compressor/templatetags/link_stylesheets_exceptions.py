### Missing files errors

class MissedscssException(object, FileNotFoundError):
    """Exception raised when missed scss files in the stylesheet dictionary."""

    def __init__(self, message: str = "SCSS files are missing. Please check the stylesheet context of the template.", description: str = "", *args: object, **kwargs: object):
        
        self.message = message + "\n\n" + description
        super().__init__(self.message, *args, **kwargs)

class MissedcssException(object, FileNotFoundError):
    """Exception raised when missed css files in the stylesheet dictionary."""

    def __init__(self, message: str = "CSS files are missing. Please check the stylesheet context of the template.", description: str = "", *args: object, **kwargs: object):
        
        self.message = message + "\n\n" + description
        super().__init__(self.message, *args, **kwargs)

### Missing template name error

class MissedtemplateException(object, Exception):
    """Exception raised when a stylesheet is not found."""
    def __init__(self, message="Did you forget to add the template name?", *args: object, **kwargs: object):

        self.message = message
        super().__init__(self.message, *args, **kwargs)
        
### Type Errors

class NotdictException(TypeError):
    """Exception raised when a dictionary is expected but not provided."""
    def __init__(self, message="Expected a dictionary, but received a different type."):
        self.message = message
        super().__init__(self.message)

class NotlistException(TypeError):
    """Exception raised when a list is expected but not provided."""
    def __init__(self, message="Expected a list, but received a different type."):
        self.message = message
        super().__init__(self.message)

class NotstrException(TypeError):
    """Exception raised when a string is expected but not provided."""
    def __init__(self, message="Expected a string, but received a different type."):
        self.message = message
        super().__init__(self.message)