import falcon
from services.api.core.predict import Resource

api = application = falcon.API()

predict_model = Resource()
api.add_route('/predict', predict_model)
