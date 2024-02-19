

class GetHomeUseCase:

    def __init__(self):
        pass

    @staticmethod
    async def execute():
        return {
            "message": "Welcome to the home page"
        }