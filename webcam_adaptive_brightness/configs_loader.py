#!/usr/bin/python
# -*- coding: utf-8 -*-
import toml
import os

class Configs:
    def __init__(self, configs_path):
        self.configs_path = configs_path
        self.load_configs()

    def load_configs(self):
        with open(self.configs_path, 'r') as fp:
            self.configs = toml.load(fp)

    def get_configs(self):
        return self.configs

    def get_settings(self):
        return self.configs['settings']

    def get_setting(self, setting_name):
        return self.configs['settings'].get(setting_name, None)

    def set_setting(self, setting_name, setting_value):
        self.configs['settings'][setting_name] = setting_value

    def save_configs(self, new_configs_dict):
        with open(self.configs_path, 'w') as fp:
            toml.dump(new_configs_dict, fp)
            self.configs = new_configs_dict

if __name__=='__main__':
    settings = Configs(os.path.abspath(os.path.dirname(__file__)+'/configs.toml'))
    print(settings.get_configs())
