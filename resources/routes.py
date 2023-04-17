from resources.auth import RegisterResource, LoginResource
from resources.cars import CarsResource
from resources.repairs import RepairsResource, RepairResource

routes = (
    (RegisterResource, "/register"),
    (LoginResource, "/login"),
    (CarsResource, "/cars"),
    (RepairsResource, "/repairs"),
    (RepairResource, "/repair/<int:pk>")
)
