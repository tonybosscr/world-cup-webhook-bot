# Render Webhook Bot Package

This is a separate instant-response Telegram webhook bot for Render.

## What it does
- responds instantly to `/today`, `/next`, `/dashboard`, `/summary`
- reads latest published prediction data from your GitHub Pages JSON
- sends Telegram replies with dashboard button

## Environment variables
- `TELEGRAM_BOT_TOKEN`
- `TELEGRAM_WEB_APP_URL`
- `DASHBOARD_DATA_URL`
- `TELEGRAM_WEBHOOK_SECRET`

## Recommended data URL
For your repo:
- `https://tonybosscr.github.io/world-cup-testing/data/dashboard_data.json`

## Deploy on Render
1. Create a new Web Service on Render.
2. Upload this package or connect the repo folder.
3. Set the environment variables.
4. Deploy.
5. Copy the public Render URL.
6. Set the Telegram webhook using the provided setup route.
