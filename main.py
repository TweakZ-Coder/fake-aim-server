from http.server import BaseHTTPRequestHandler, HTTPServer
import json

aim_data = {
    "aimlock": 1,
    "recoil": 0,
    "spread": 0,
    "aim_assist": 100,
    "target_mode": "head",
    "fire_delay": 0,
    "tracking_speed": 9999,
    "stability": 999,
    "auto_shoot": 1,
    "no_shake": 1,
    "quick_scope": 1,
    "magnet_mode": "strong"
}

custom_endpoints = [
    "/aim.json",
    "/aim/aim/ffaim.json",
    "/aim/aim/target.json",
    "/aim/aimbot/aim.json",
    "/aim/aimbot/aimconfig.json",
    "/aim/assist/target.json",
    "/aim/json/config.json",
    "/aim/lock/settings.json",
    "/aim/track/aimconfig.json",
    "/aim/track/settings.json",
    "/api/aim/aimconfig.json",
    "/api/aimbot/ffaim.json",
    "/api/assist/ffaim.json",
    "/api/assist/settings.json",
    "/api/assist/target.json",
    "/api/track/aimconfig.json",
    "/api/track/ffaim.json",
    "/api/v1/aim/config",
    "/assets/aim/settings.json",
    "/cheat/aim/setting",
    "/client/aim/aimlock.json",
    "/client/aim/target.json",
    "/client/assist/aimlock.json",
    "/client/assist/settings.json",
    "/client/track/aimlock.json",
    "/cloud/aim/settings.json",
    "/cloud/aim/target.json",
    "/cloud/aimbot/aimlock.json",
    "/cloud/aimbot/data",
    "/cloud/aimbot/settings.json",
    "/cloud/aimbot/target.json",
    "/cloud/lock/aim.json",
    "/cloud/lock/ffaim.json",
    "/cloud/track/aimconfig.json",
    "/cloud/track/settings.json",
    "/cloud/track/target.json",
    "/config/aim/ffaim.json",
    "/config/aim/lock",
    "/config/aimbot/settings.json",
    "/config/aimbot/target.json",
    "/config/assist/aim.json",
    "/config/track/ffaim.json",
    "/config/track/settings.json",
    "/data/aim/lock.json",
    "/data/assist/aimconfig.json",
    "/data/assist/aimlock.json",
    "/data/assist/ffaim.json",
    "/data/assist/settings.json",
    "/data/lock/aim.json",
    "/data/lock/ffaim.json",
    "/data/lock/target.json",
    "/esp/config/aim.json",
    "/ff/aim/aimconfig.json",
    "/ff/aim/aimlock.json",
    "/ff/aim/settings.json",
    "/ff/aimbot/aimconfig.json",
    "/ff/aimbot/target.json",
    "/ff/track/aimlock.json",
    "/freefire/aimlock/data",
    "/game/aimbot/aim.json",
    "/game/assist/target.json",
    "/game/lock/aimconfig.json",
    "/game/track/ffaim.json",
    "/mobile/aim/aimlock.json",
    "/mobile/aim/ffaim.json",
    "/mobile/aim/settings.json",
    "/mobile/aim/target.json",
    "/mobile/aimbot/settings.json",
    "/mobile/aimbot/target.json",
    "/mobile/assist/target.json",
    "/mobile/lock/aim.json",
    "/mobile/lock/aimconfig.json",
    "/mobile/lock/target.json",
    "/mobile/track/ffaim.json",
    "/raw/aim/data.json",
    "/v1/aim/aimconfig.json",
    "/v1/aim/ffaim.json",
    "/v1/aimbot/ffaim.json",
    "/v1/aimbot/settings.json",
    "/v1/assist/aimlock.json",
    "/v1/lock/aimconfig.json",
    "/v1/track/ffaim.json",
    "/v2/aim/aim.json",
    "/v2/aim/ffaim.json",
    "/v2/aimbot/aim.json",
    "/v2/aimbot/aimconfig.json",
    "/v2/aimbot/ffaim.json",
    "/v2/aimlock/settings",
    "/v2/lock/aimlock.json",
    "/v2/track/aimconfig.json",
    "/v2/track/target.json",
    "/v3/aim/settings",
    "/v3/aim/target.json",
    "/v3/aimbot/ffaim.json",
    "/v3/aimbot/target.json",
    "/v3/assist/aimlock.json",
    "/v3/assist/ffaim.json",
    "/v3/assist/settings.json",
    "/v3/lock/settings.json",
    "/v3/track/aimlock.json"
]

class AimHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path in custom_endpoints:
            print(f"[+] Truy cáº­p tá»«: {self.client_address[0]} --> {self.path}")
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps(aim_data).encode())
        else:
            self.send_response(404)
            self.end_headers()

ip = "0.0.0.0"
port = 7001

try:
    server = HTTPServer((ip, port), AimHandler)
    print(f"[â] Server Äang cháº¡y táº¡i http://{ip}:{port}")
    server.serve_forever()
except OSError as e:
    print(f"[â] Lá»i khÃ´ng thá» khá»i Äá»ng server táº¡i cá»ng {port}: {e}")