#!/usr/bin/env python
import yaml

class Config:
    def __init__(self):
        self._data = {}

    def load_file(self, config_file_path):
        maybe_data = {}

        with open(config_file_path, 'r') as config_file:
            maybe_data = yaml.safe_load(config_file)

        valid = self.validate(maybe_data)
        if valid:
            self._data = maybe_data
        else:
            # TODO (lujan): If we want to make a more robust config system, having more detailed diagnostics that say what validation rule failed would be dank.
            raise RuntimeError("Configuration file passed in was invalid")

    def get(self, query):
        keys = query.split('.')

        node = self._data
        for key in keys:
            node = node.get(key)

        return node

    @staticmethod
    def validate(config_data):
        if not 'auth' in config_data:
            return False
        if not 'token' in config_data['auth']:
            return False
        return True
