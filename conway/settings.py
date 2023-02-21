import yaml


class Settings:
    
    def __init__(self, path):
        self._path = path
        self._config = dict()
        self._setup()
    
    def _setup(self):
        with open(self._path, 'r') as file:
            config = yaml.safe_load(file)
        self._config = config['game']
    
    def get(self, key):
        value = self._config.get(key)
        if isinstance(value, list):
            value = tuple(value)
        return value
        