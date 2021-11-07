import json
import requests
import test_data


api_token = test_data.from_env("API_KEY")
apk_id = test_data.from_config("APP_ID")
package_name = test_data.from_config("PACKAGE_NAME")
udid = test_data.from_config("UDID")


def adb_bridge():
    req = "adb/{}/bridge".format(udid)
    res = send_request("post", req)
    test_data.device_ip_address = res["serial"]
    return res


def adb_install():
    req = "adb/{}/install?apk_id={}".format(udid, apk_id)
    return send_request("post", req)


def adb_lock():
    req = "adb/{}/lock".format(udid)
    res = send_request("post", req)
    test_data.device_address = res["message"].split(" ")[0]
    return res


def adb_uninstall():
    req = "adb/{}/uninstall?package_name={}".format(udid, package_name)
    return send_request("post", req)


def adb_unlock():
    req = "adb/{}/unlock".format(udid)
    return send_request("post", req)


def send_request(verb, req, data=None):
    # print('\u001b[36m' + verb + " | " + req + '\u001b[0m')  # DEBUGGING
    headers = {
        "Authorization": "Bearer {}".format(api_token)
    }
    req = "https://api-dev.headspin.io/v0/{}".format(req)
    if data == None:
        r = getattr(requests, verb)(req, headers=headers)
        return r.json()
    else:
        headers["content-type"] = "application/json"
        r = getattr(requests, verb)(req, headers=headers, data=data)
        return r.json()


def session_end():
    req = "sessions/{}".format(test_data.session_id)
    data = {
        "active": False
    }
    data = json.dumps(data)
    return send_request("patch", req, data)


def session_start():
    data = {
        "session_type": "capture",
        "device_address": test_data.device_address
    }
    print(data)
    data = json.dumps(data)
    res = send_request("post", "sessions", data)
    test_data.session_id = res["session_id"]
    return res
