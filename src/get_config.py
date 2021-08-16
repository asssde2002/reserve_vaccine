import os
import io
import configparser

CONFIG = configparser.ConfigParser()

def get_config(CONFIG_DIR='.'):
    config_file = f"{CONFIG_DIR}/development.cfg"
    if os.path.isfile(f"{CONFIG_DIR}/production.cfg"):
        config_file = f"{CONFIG_DIR}/production.cfg"
    CONFIG.read(config_file)
    return CONFIG