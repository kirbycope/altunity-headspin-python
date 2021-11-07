import configparser
from dotenv import load_dotenv
import os


def init():
    global altUnityDriver; altUnityDriver = None
    global device_ip_address; device_ip_address = None
    global time_start; time_start = None
    global time_end; time_end = None


def from_config(key):
    config = configparser.ConfigParser()
    config.read("headspin.ini")
    return config["DEFAULT"][key]


def from_env(key):
    load_dotenv()
    return os.environ[key]
