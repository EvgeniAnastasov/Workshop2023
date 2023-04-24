from resources.auth import RegisterResource, LoginResource
from resources.cars import CarsResource, CarResource
from resources.repairs import RepairsResource, RepairResource

routes = (
    (RegisterResource, "/register"),
    (LoginResource, "/login"),

    (CarsResource, "/cars"),
    (CarResource, "/car/<int:pk>"),

    (RepairsResource, "/repairs"),
    (RepairResource, "/repair/<int:pk>")
)
