import os

from . import turbo, curie

models = {
    'turbo': turbo.predict,
    'curie': curie.predict
}

current_model_name = os.getenv('CURRENT_MODEL')
current_model = models.get(current_model_name)

if current_model is None:
    print(f'Invalid model name: {current_model_name}')
