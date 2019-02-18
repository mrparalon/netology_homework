class BannedDeletedUser(BaseException):
    """
    Exception raised if error code 18 recieved:
    User was deleted or banned
    """
    pass

class PermissionDenied(BaseException):
    """
    Exception raised if error code 7 recieved:
    Permission to perform this action is denied
    """
    pass
