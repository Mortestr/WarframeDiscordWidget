import os
import json
import time
import requests
import sys
import threading
from urllib.parse import urlparse, parse_qs
from PIL import Image, ImageDraw
import pystray

BASE_DIR = os.path.dirname(sys.executable) if getattr(sys, 'frozen', False) else os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(BASE_DIR, "config.json")

def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def fetch_warframe_stats(api_key):
    if api_key.startswith("http"):
        parsed = urlparse(api_key)
        token = parse_qs(parsed.query)["publicToken"][0]
    else:
        token = api_key
        
    url = "https://stats.alecaframe.com/api/stats/public"
    headers = {"User-Agent": "Mozilla/5.0", "Referer": f"https://stats.alecaframe.com/stats/?publicToken={token}"}
    resp = requests.get(url, params={"token": token}, headers=headers, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    points = data.get("generalDataPoints", [])
    if not points: raise Exception("no Stats found")
    latest = points[-1]
    
    return {
        "trades_count": len(data.get("trades", [])),
        "balance_plat": latest.get("plat", 0),
        "balance_credits": latest.get("credits", 0),
        "balance_ducats": latest.get("ducats", 0),
        "balance_aya": latest.get("aya", 0),
        "balance_endo": latest.get("endo", 0),
    }

def update_discord_widget(cfg, stats):
    url = f"https://discord.com/api/v9/applications/{cfg['discord_application_id']}/users/{cfg['discord_user_id']}/identities/0/profile"
    headers = {"Authorization": f"Bot {cfg['discord_bot_token']}", "Content-Type": "application/json"}
    
    payload = {"data": {"dynamic": [
        {"type": 1, "name": "Endo", "value": f"{stats['balance_endo']:,}"},
        {"type": 1, "name": "Platinum", "value": f"ㅤ{stats['balance_plat']:,}p"},
        {"type": 1, "name": "Credits", "value": f"{stats['balance_credits']:,}"},
        {"type": 1, "name": "Aya", "value": f"ㅤ{stats['balance_aya']:,}"},
        {"type": 1, "name": "Ducats", "value": f"ㅤ{stats['balance_ducats']:,}"},
        {"type": 1, "name": "Trades", "value": f"ㅤ{stats['trades_count']:,}"}
    ]}}
    
    requests.patch(url, headers=headers, json=payload, timeout=10).raise_for_status()

def run_bot(icon):
    icon.visible = True
    while True:
        try:
            cfg = load_config()
            stats = fetch_warframe_stats(cfg["alecaframe_token"])
            update_discord_widget(cfg, stats)
            time.sleep(cfg.get("update_interval_minutes", 5) * 60)
        except Exception as e:
            print(f"Fehler: {e}")
            time.sleep(60)

def create_image():
    image = Image.new('RGB', (64, 64), color=(88, 101, 242))
    return image

def main():
    icon = pystray.Icon("WarframeWidget", create_image(), "Warframe Stats", menu=pystray.Menu(
        pystray.MenuItem("Exit", lambda i: i.stop())
    ))
    threading.Thread(target=run_bot, args=(icon,), daemon=True).start()
    icon.run()

if __name__ == "__main__":
    main()