import subprocess
from altunityrunner import *
from datetime import timedelta
import time
import headspin
import test_data


def before_scenario(context, scenario):
    """ This runs before each scenario. """
    test_data.init()
    test_data.time_start = time.time()
    start_session()


def after_scenario(context, scenario):
    end_session()
    test_data.time_end = time.time()
    time_taken = str(
        timedelta(seconds=test_data.time_end - test_data.time_start))
    print("\n" + '\033[94m' + "  Total Test Time: " + time_taken + '\033[0m')


def end_session():
    if test_data.altUnityDriver != None:
        test_data.altUnityDriver.stop()
        AltUnityPortForwarding.remove_forward_android()


def start_session():
    headspin.app_uninstall()
    headspin.app_install()
    headspin.device_lock()
    headspin.device_bridge()
    headspin.device_unlock()
    adb_connect()
    adb_monkey()
    AltUnityPortForwarding.forward_android()
    test_data.altUnityDriver = AltUnityDriver()


def adb_connect():
    adb_shell("adb connect " + test_data.device_ip_address)
    time.sleep(1)


def adb_disconnect():
    adb_shell("adb disconnect " + test_data.device_ip_address)


def adb_monkey():
    package_name = test_data.from_config("PACKAGE_NAME")
    adb_shell(
        "adb shell monkey -p {} -c android.intent.category.LAUNCHER 1".format(package_name))


def adb_shell(cmd):
    subprocess.call(cmd, shell=True)
