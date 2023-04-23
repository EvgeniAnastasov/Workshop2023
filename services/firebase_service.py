import pyrebase
from decouple import config


class FirebaseService:
    def __init__(self):
        self.firebase_config = {
            "apiKey": config("FIREBASE_API_KEY"),
            "authDomain": config("FIREBASE_AUTH_DOMAIN"),
            "projectId": config("FIREBASE_PROJECT_ID"),
            "storageBucket": config("FIREBASE_STORAGE_BUCKET"),
            "messagingSenderId": config("FIREBASE_MESSAGING_SENDER_ID"),
            "appId": config("FIREBASE_APP_ID"),
            "measurementId": config("FIREBASE_MEASUREMENT_ID"),
            "databaseURL": ""
        }

        firebase = pyrebase.initialize_app(self.firebase_config)
        self.storage = firebase.storage()

    def upload_image(self, photo_name, local_path_to_store_photo):
        path_on_cloud = f"images/{photo_name}"
        self.storage.child(path_on_cloud).put(local_path_to_store_photo)

        return self.storage.child(path_on_cloud).get_url(None)
