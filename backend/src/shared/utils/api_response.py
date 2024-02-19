
class ApiResponse:
    STATUS_OK = 200
    STATUS_CREATED = 201
    STATUS_BAD_REQUEST = 400
    STATUS_UNAUTHORIZED = 401
    STATUS_NOT_FOUND = 404
    STATUS_INTERNAL_SERVER_ERROR = 500

    @staticmethod
    def json(data :dict, message : str ="", status_code: int = STATUS_OK) ->dict:
        return {
            "data": data,
            "status_code": status_code,
            "message": message
        }
    
    @staticmethod
    def error(data : dict, status_code : int = STATUS_NOT_FOUND) -> dict:
        return {
            "data": data,
            "status_code": status_code,
        }
