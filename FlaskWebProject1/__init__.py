"""
The flask application package.
"""

from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

import FlaskWebProject1.views


activity_scores = {
    'Beer Pong': [],
    'Golf': [],
    'HammaStick': [],
    'MVP': []
}


def calculate_total_score(player_scores):
    total_score = 0
    for activity_scores in player_scores.values():
        total_score += sum(activity_scores)
    return total_score


def sort_players_by_total_score():
    sorted_players = []
    for i in range(1, 13):
        player_scores = {}
        for activity in activity_scores:
            day1_score = int(request.form[f'{activity}_Day 1_Player {i}'])
            day2_score = int(request.form[f'{activity}_Day 2_Player {i}'])
            player_scores[activity] = [day1_score, day2_score]
        player_name = f'Player {i}'
        total_score = calculate_total_score(player_scores)
        sorted_players.append((player_name, total_score))
    sorted_players.sort(key=lambda x: x[1], reverse=True)
    return sorted_players


@app.route('/')
def index():
    activities = ['Beer Pong', 'Golf', 'HammaStick', 'MVP']
    """Renders the activity page."""
    return render_template('index.html', activities=activities)


@app.route('/submit_scores', methods=['POST'])
def submit_scores():
    for activity in activity_scores:
        for i in range(1, 13):
            day1_score = int(request.form[f'{activity}_Day 1_Player {i}'])
            day2_score = int(request.form[f'{activity}_Day 2_Player {i}'])
            activity_scores[activity].append((f'Player {i}', [day1_score, day2_score]))
    sorted_players = sort_players_by_total_score()
    return redirect(url_for('leaderboard'))


@app.route('/leaderboard')
def leaderboard():
    sorted_players = sort_players_by_total_score()
    return render_template('leaderboard.html', sorted_players=sorted_players)


if __name__ == '__main__':
    app.run(debug=True)



