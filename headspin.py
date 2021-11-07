import requests
import test_data


def device_bridge():
    res = send_post("bridge")
    test_data.device_ip_address = res["serial"]
    return res


def app_install():
    apk_id = test_data.from_config("APP_ID")
    request = "install?apk_id={}".format(apk_id)
    return send_post(request)


def device_lock():
    return send_post("lock")


def app_uninstall():
    package_name = test_data.from_config("PACKAGE_NAME")
    request = "uninstall?package_name={}".format(package_name)
    return send_post(request)


def device_unlock():
    return send_post("unlock")


def send_post(request):
    print('\u001b[36m' + request + '\u001b[0m')
    api_token = test_data.from_env("API_KEY")
    headers = {
        "Authorization": "Bearer {}".format(api_token)
    }
    udid = test_data.from_config("UDID")
    request = "https://api-dev.headspin.io/v0/adb/{}/{}".format(udid, request)
    r = requests.post(request, headers=headers)
    return r.json()
