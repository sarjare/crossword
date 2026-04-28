import urllib.request
import json
import ssl

url = "https://firestore.googleapis.com/v1/projects/cyberverse-8697e/databases/(default)/documents/teams/test_team_999?key=AIzaSyDMm2erMuAv9q_4Ln_Yu5j2hnNMm23W4AM"

data = {
    "fields": {
        "name": {"stringValue": "TEST_TEAM"}
    }
}

req = urllib.request.Request(url, method="PATCH", data=json.dumps(data).encode("utf-8"), headers={"Content-Type": "application/json"})
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

try:
    with urllib.request.urlopen(req, context=ctx) as response:
        print("SUCCESS:", response.read().decode())
except urllib.error.HTTPError as e:
    print("HTTP ERROR:", e.code, e.read().decode())
except Exception as e:
    print("ERROR:", e)
