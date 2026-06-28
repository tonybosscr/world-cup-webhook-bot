def today_text(data):
    preds = data.get('predictions_today', [])
    if not preds:
        return '*🗓 Today\'s Predictions*\nNo predictions available right now\.'
    lines = ['*🗓 Today\'s Predictions*']
    for p in preds[:8]:
        lines.append(f"• *{p['home_team']} vs {p['away_team']}* → {p['predicted_outcome']} \({p['confidence']:.1%}\)")
    return '\n'.join(lines)


def next_text(data):
    preds = data.get('predictions_today', [])
    if not preds:
        return '*⏭ Upcoming Match*\nNo upcoming prediction available\.'
    p = preds[0]
    return (
        '*⏭ Upcoming Match Prediction*\n'
        f"*{p['home_team']} vs {p['away_team']}*\n"
        f"Pick: {p['predicted_outcome']} \({p['confidence']:.1%}\)\n"
        f"Board: {p['home_team']} {p['home_win_prob']:.1%} • Draw {p['draw_prob']:.1%} • {p['away_team']} {p['away_win_prob']:.1%}"
    )


def dashboard_text(data):
    return '*📊 Dashboard*\nUse the button below to open the live dashboard\.'


def summary_text(data):
    summary = data.get('summary', {})
    latest = summary.get('latest') or {}
    return (
        '*📈 Latest Summary*\n'
        f"Tracked runs: {summary.get('runs', 0)}\n"
        f"Average accuracy: {summary.get('avg_pick_accuracy', 0):.1%}\n"
        f"Latest evaluated matches: {latest.get('evaluated_matches', 0)}"
    )
