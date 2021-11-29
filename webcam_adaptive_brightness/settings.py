import json

class settings:
    def __init__(self, json_path):
        with open(json_path, 'r', encoding='utf8') as fp:
            data = json.load(fp)
            init_preset = data['current_preset']
            configs = data[init_preset]

            self.min_ambient = configs['ambient_brightness']['min']
            self.max_ambient = configs['ambient_brightness']['max']
            self.min_display = configs['display_brightness']['min']
            self.max_display = configs['display_brightness']['max']
            self.threshold = configs['threshold']

    def save_current(self, json_path, configs):
        with open(json_path, 'w', encoding='utf8') as fp:
            pass
