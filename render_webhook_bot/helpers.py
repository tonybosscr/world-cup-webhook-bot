import os
import requests


def dashboard_url():
    return os.getenv('DASHBOARD_DATA_URL', 'https://tonybosscr.github.io/world-cup-testing/data/dashboard_data.json').strip()


def web_app_url():
    return os.getenv('TELEGRAM_WEB_APP_URL', '').strip()


def fetch_dashboard_data():
    r = requests.get(dashboard_url(), timeout=30)
    r.raise_for_status()
    return r.json()


def reply_markup():
    url = web_app_url()
    if not url:
        return None
    return {
        'inline_keyboard': [
            [
                {'text': '📊 Open Dashboard', 'web_app': {'url': url}},
                {'text': '🗓 Predictions Today', 'web_app': {'url': url}},
            ]
        ]
    }


def send_message(bot_token: str, chat_id: str, text: str):
    url = f"https://api.telegram.org/bot{bot_token}/sendMessage"
    payload = {
        'chat_id': chat_id,
        'text': text,
        'parse_mode': 'Markdown',
        'disable_web_page_preview': True,
    }
    markup = reply_markup()
    if markup:
        payload['reply_markup'] = markup
    r = requests.post(url, json=payload, timeout=30)
    r.raise_for_status()
    return r.json()


def set_webhook(bot_token: str, webhook_url: str, secret: str = None):
    url = f"https://api.telegram.org/bot{bot_token}/setWebhook"
    payload = {'url': webhook_url}
    if secret:
        payload['secret_token'] = secret
    r = requests.post(url, json=payload, timeout=30)
    r.raise_for_status()
    return r.json()
