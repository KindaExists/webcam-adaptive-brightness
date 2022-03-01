#!/usr/bin/python
# -*- coding: utf-8 -*-
import toml
import os

class Configs:
    def __init__(self, configs_path):
        self.configs_path = configs_path
        self.load_configs()

    def load_configs(self):
        try:
            with open(self.configs_path, 'r') as fp:
                self.configs = toml.load(fp)
        except FileNotFoundError:
            self.create_new_configs_file()

    def create_new_configs_file(self):
        new_config = {}
        new_config['settings'] = {}
        new_settings = new_config['settings']

        new_settings['update_interval'] = 10.0
        new_settings['threshold'] = 0.0
        new_settings['samples_per_update'] = 1
        new_settings['ambient_percentages'] = [0.0, 100.0]
        new_settings['screen_percentages'] = [0.0, 100.0]
        new_settings['device_name'] = False
        new_settings['preview_enabled'] = False

        self.save_configs(new_config)

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

