import json

class Settings:
    def __init__(self, json_path):
        self.json_path = json_path
        with open(self.json_path, 'r', encoding='utf8') as fp:
            self.json_data = json.load(fp)
            current_preset = self.json_data['current_preset']
            self.open_preset(current_preset)

    def open_preset(self, preset):
        preset_config = self.json_data['presets'][preset]

        self.ambient = preset_config['ambient_brightness']
        self.display = preset_config['display_brightness']
        self.threshold = preset_config['threshold']
        self.loop_interval = preset_config['loop_interval']
        self.update_interval = preset_config['update_interval']
        self.device = preset_config['device']

    def switch_preset(self, preset_name):
        self.json_data['current_preset'] = preset_name
        self.open_preset(preset_name)

    def get_dict_repr(self):
        return {
            'ambient': self.ambient,
            'display': self.display,
            'threshold': self.threshold,
            'loop_interval': self.loop_interval,
            'update_interval': self.update_interval,
            'device': self.device
        }

    def save_current(self):
        with open(self.json_path, 'w', encoding='utf8') as fp:
            current_preset = self.json_data['current_preset']
            preset_config = self.json_data['presets'][current_preset]

            preset_config['ambient_brightness'] = self.ambient
            preset_config['display_brightness'] = self.display
            preset_config['threshold'] = self.threshold
            preset_config['loop_interval'] = self.loop_interval
            preset_config['update_interval'] = self.update_interval
            preset_config['device'] = self.device

            json.dump(self.json_data, fp, indent=4)

if __name__ == '__main__':
    config = Settings('./webcam_adaptive_brightness/settings.json')
    config.save_current()