from resources.auth import RegisterResource, LoginResource
from resources.cars import CarsResource

routes = (
    (RegisterResource, "/register"),
    (LoginResource, "/login"),
    (CarsResource, "/cars"),
)
