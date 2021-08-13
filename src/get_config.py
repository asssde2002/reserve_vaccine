import os
import io
import configparser

CONFIG = configparser.ConfigParser()

def get_config(CONFIG_DIR='.'):
    config_file = "{}/development.cfg".format(CONFIG_DIR)
    if os.path.isfile("{}/production.cfg".format(CONFIG_DIR)):
        config_file = "{}/production.cfg".format(CONFIG_DIR)
    CONFIG.read(config_file)
    return CONFIG