from altunityrunner import *
from datetime import timedelta
import time
import configparser
import test_data


def before_scenario(context, scenario):
    """ This runs before each scenario. """
    test_data.init()
    test_data.time_start = time.time()
    AltUnityPortForwarding.forward_android()
    test_data.altUnityDriver = AltUnityDriver()


def after_scenario(context, scenario):
    """ This runs after each scenario. """
    test_data.driver.quit()
    test_data.altUnityDriver.stop()
    AltUnityPortForwarding.remove_forward_android()
    test_data.time_end = time.time()
    time_taken = str(timedelta(seconds=test_data.time_end - test_data.time_start))
    print("\n" + '\033[94m' + "  Total Test Time: " + time_taken + '\033[0m')


def read_from_config(key):
    """ Read the value of the given key from the configuration file. """
    config = configparser.ConfigParser()
    config.read("altunity.ini")
    return config["DEFAULT"][key]
