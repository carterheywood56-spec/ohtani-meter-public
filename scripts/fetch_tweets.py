#!/usr/bin/env python3
"""自分のXアカウントの最新投稿を取得してMarkdownで保存する"""

import os
import json
import requests
from datetime import datetime, timezone, timedelta
from requests_oauthlib import OAuth1

# .envから環境変数を読み込む
from dotenv import load_dotenv
load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

API_KEY = os.environ['X_API_KEY']
API_KEY_SECRET = os.environ['X_API_KEY_SECRET']
ACCESS_TOKEN = os.environ['X_ACCESS_TOKEN']
ACCESS_TOKEN_SECRET = os.environ['X_ACCESS_TOKEN_SECRET']

JST = timezone(timedelta(hours=9))

def fetch_my_tweets(max_results=20):
    auth = OAuth1(API_KEY, API_KEY_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # まず自分のuser_idを取得
    me_url = 'https://api.twitter.com/2/users/me'
    me_res = requests.get(me_url, auth=auth)
    me_res.raise_for_status()
    user_id = me_res.json()['data']['id']
    username = me_res.json()['data']['username']

    # タイムラインを取得
    timeline_url = f'https://api.twitter.com/2/users/{user_id}/tweets'
    params = {
        'max_results': max_results,
        'tweet.fields': 'created_at,public_metrics',
        'exclude': 'retweets,replies',
    }
    res = requests.get(timeline_url, auth=auth, params=params)
    res.raise_for_status()
    tweets = res.json().get('data', [])

    return username, tweets

def save_as_markdown(username, tweets):
    lines = [f'# @{username} 投稿一覧', f'取得日時: {datetime.now(JST).strftime("%Y-%m-%d %H:%M")} JST', '']
    for t in tweets:
        created = datetime.fromisoformat(t['created_at'].replace('Z', '+00:00')).astimezone(JST)
        metrics = t.get('public_metrics', {})
        lines.append(f'## {created.strftime("%Y-%m-%d %H:%M")}')
        lines.append(t['text'])
        lines.append(f'- いいね: {metrics.get("like_count", 0)}  RT: {metrics.get("retweet_count", 0)}  返信: {metrics.get("reply_count", 0)}')
        lines.append('')

    out_path = os.path.join(os.path.dirname(__file__), '..', 'docs', 'tweets_log.md')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f'保存しました: {out_path}')
    print(f'取得件数: {len(tweets)}件')

if __name__ == '__main__':
    username, tweets = fetch_my_tweets(max_results=20)
    save_as_markdown(username, tweets)
