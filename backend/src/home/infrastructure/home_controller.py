from backend.src.shared.utils.api_response import ApiResponse
from backend.src.shared.base.controller.base_controller import BaseController
from backend.src.home.application.get_home_use_case import GetHomeUseCase



class HomeController(BaseController):
    # def __init__(self, get_home_use_case):
    #     self.get_home_use_case = get_home_use_case

    @staticmethod
    async def get_home():
        data = GetHomeUseCase.execute
        return ApiResponse.json({"data":data}, "Home")
