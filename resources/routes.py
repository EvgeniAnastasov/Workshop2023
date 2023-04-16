from resources.auth import RegisterResource, LoginResource
from resources.cars import CarsResource
from resources.repairs import RepairsResource

routes = (
    (RegisterResource, "/register"),
    (LoginResource, "/login"),
    (CarsResource, "/cars"),
    (RepairsResource, "/repairs")
)
