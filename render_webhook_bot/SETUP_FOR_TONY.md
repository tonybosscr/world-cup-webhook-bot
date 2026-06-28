# Render Setup For Tony

## Your live dashboard data source
Use:
- `https://tonybosscr.github.io/world-cup-testing/data/dashboard_data.json`

## Your mini app URL
Use:
- `https://tonybosscr.github.io/world-cup-testing/mini_app/`

## Render environment variables
Set these in Render:
- `TELEGRAM_BOT_TOKEN` = your regenerated token
- `TELEGRAM_WEB_APP_URL` = `https://tonybosscr.github.io/world-cup-testing/mini_app/`
- `DASHBOARD_DATA_URL` = `https://tonybosscr.github.io/world-cup-testing/data/dashboard_data.json`
- `TELEGRAM_WEBHOOK_SECRET` = any long random string

## After deploy
Open:
- `https://YOUR-RENDER-APP.onrender.com/setup-webhook`

That will register the webhook with Telegram.

## Result
Your bot commands should respond instantly:
- `/today`
- `/next`
- `/dashboard`
- `/summary`
