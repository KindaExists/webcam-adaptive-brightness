import json

class Settings:
    def __init__(self, json_path):
        self.json_path = json_path
        with open(self.json_path, 'r', encoding='utf8') as fp:
            self.json_data = json.load(fp)

            # Not yet implemented, for future improvements
            self.preview_enabled = self.json_data["preview_enabled"]
            self.on_startup = self.json_data["on_startup"]

            current_preset = self.json_data['current_preset']
            self.load_preset(current_preset)

    def open_preset(self, preset):
        preset_config = self.json_data['presets'][preset]

        self.ambient            = preset_config['ambient_brightness']
        self.threshold          = preset_config['threshold']
        self.samples_per_update = preset_config['samples_per_update']
        self.update_interval    = preset_config['update_interval']
        self.device             = preset_config['device']

    def load_preset(self, preset_name):
        self.json_data['current_preset'] = preset_name
        self.open_preset(preset_name)

    def get_dict_repr(self):
        return {
            'preview_enabled' : self.preview_enabled,
            'on_startup' : self.on_startup,

            'ambient'           : self.ambient,
            'threshold'         : self.threshold,
            'samples_per_update': self.samples_per_update,
            'update_interval'   : self.update_interval,
            'device'            : self.device
        }

    def save_current(self):
        with open(self.json_path, 'w', encoding='utf8') as fp:
            self.json_data["preview_enabled"] = self.preview_enabled
            self.json_data["on_startup"] = self.on_startup

            current_preset = self.json_data['current_preset']
            preset_config = self.json_data['presets'][current_preset]

            preset_config['ambient_brightness'] = self.ambient
            preset_config['threshold']          = self.threshold
            preset_config['samples_per_update'] = self.samples_per_update
            preset_config['update_interval']    = self.update_interval
            preset_config['device']             = self.device

            json.dump(self.json_data, fp, indent=4)
