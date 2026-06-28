import os
from flask import Flask, request, jsonify

from commands import today_text, next_text, dashboard_text, summary_text
from helpers import fetch_dashboard_data, send_message, set_webhook

app = Flask(__name__)
BOT_TOKEN = os.getenv('TELEGRAM_BOT_TOKEN', '').strip()
WEBHOOK_SECRET = os.getenv('TELEGRAM_WEBHOOK_SECRET', '').strip()


@app.get('/')
def home():
    return jsonify({'ok': True, 'service': 'world-cup-telegram-webhook'})


@app.get('/setup-webhook')
def setup_webhook_route():
    if not BOT_TOKEN:
        return jsonify({'ok': False, 'error': 'Missing TELEGRAM_BOT_TOKEN'}), 500
    base_url = request.host_url.rstrip('/')
    webhook_url = f"{base_url}/webhook"
    result = set_webhook(BOT_TOKEN, webhook_url, WEBHOOK_SECRET or None)
    return jsonify({'ok': True, 'webhook_url': webhook_url, 'telegram_result': result})


@app.post('/webhook')
def webhook():
    if WEBHOOK_SECRET:
        incoming = request.headers.get('X-Telegram-Bot-Api-Secret-Token', '')
        if incoming != WEBHOOK_SECRET:
            return jsonify({'ok': False, 'error': 'Invalid secret'}), 403

    if not BOT_TOKEN:
        return jsonify({'ok': False, 'error': 'Missing TELEGRAM_BOT_TOKEN'}), 500

    payload = request.get_json(silent=True) or {}
    msg = payload.get('message', {})
    text = (msg.get('text') or '').strip().lower()
    chat_id = (msg.get('chat') or {}).get('id')
    if not chat_id:
        return jsonify({'ok': True, 'ignored': True})

    try:
        data = fetch_dashboard_data()
    except Exception as e:
        send_message(BOT_TOKEN, str(chat_id), f"*Error*\nCould not fetch dashboard data: {str(e)}")
        return jsonify({'ok': True, 'handled': True})

    if text.startswith('/today'):
        send_message(BOT_TOKEN, str(chat_id), today_text(data))
    elif text.startswith('/next'):
        send_message(BOT_TOKEN, str(chat_id), next_text(data))
    elif text.startswith('/dashboard'):
        send_message(BOT_TOKEN, str(chat_id), dashboard_text(data))
    elif text.startswith('/summary'):
        send_message(BOT_TOKEN, str(chat_id), summary_text(data))
    else:
        send_message(
            BOT_TOKEN,
            str(chat_id),
            '*Available commands*\n/today\n/next\n/dashboard\n/summary'
        )

    return jsonify({'ok': True, 'handled': True})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', '5000')))
