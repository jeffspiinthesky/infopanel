from datetime import datetime
import feedparser
from flask import Flask, render_template, request
from pynput.keyboard import Key, Controller
import sqlite3
from subprocess import run

BBC_FEED = "http://feeds.bbci.co.uk/news/rss.xml?edition=uk"
MAX_NEWS_ENTRIES = 5

app = Flask(__name__)

def get_db_connection():
    connection = sqlite3.connect('database.db')
    connection.row_factory = sqlite3.Row
    return connection

def get_status():
    connection = get_db_connection()
    status = connection.execute('SELECT * FROM status').fetchall()
    connection.close()
    return status

def build_status_list(status_list_db):
    status_list = []
    current_time = datetime.now()
    for status_db in status_list_db:
        status = {}
        status['code'] = status_db['code']
        status['message'] = status_db['message']   
        status['vpn'] = status_db['vpn']
        status_timestamp_str = status_db['timestamp']
        status_timestamp = datetime.strptime(status_timestamp_str, '%Y-%m-%d %H:%M:%S')
        elapsed_time = current_time - status_timestamp
        elapsed_seconds = round(elapsed_time.total_seconds(),0)
        status['timestamp'] = elapsed_seconds
        if elapsed_seconds > 180 and elapsed_seconds < 360:
            status['time_bg_colour'] = '#FFFF00'
        elif elapsed_seconds > 360:
            status['time_bg_colour'] = '#FF0000'
        else:
            status['time_bg_colour'] = '#00FF00'
        if elapsed_seconds >= 3600 and elapsed_seconds < 86400:
            status['time_unit'] = 'h'
            status['timestamp'] = round(elapsed_seconds / 3600, 2)
        elif elapsed_seconds >= 86400:
            status['time_unit'] = 'd'
            status['timestamp'] = round(elapsed_seconds / 86400, 2)
        elif elapsed_seconds >= 60 and elapsed_seconds < 3600:
            status['time_unit'] = 'm'
            status['timestamp'] = round(elapsed_seconds / 60, 2)
        else:
            status['time_unit'] = 's'
            status['timestamp'] = elapsed_seconds
        if status['code'] == 200:
            status['status_bg_colour'] = '#00FF00'
        else:
            status['status_bg_colour'] = '#FF0000'
        status_list.append(status)
    return status_list

def get_news_list():
    news_feed = {}
    news_feed['news_list'] = [] 
    feed = feedparser.parse(BBC_FEED)
    # Check for feed parsing errors
    if feed.bozo:
        print(f"Error parsing feed: {feed.bozo_exception}")
        return
    
    # Print feed title and link
    news_feed['feed_title'] = feed.feed.title
    news_feed['feed_link'] = feed.feed.link
    news_feed['image'] = feed.feed.image.url
    
    # Limit to 5 items
    entries = feed.entries[:MAX_NEWS_ENTRIES]

    # Iterate through feed entries
    for entry in entries:
        news_item = {}
        news_item['title'] = entry.title
        news_item['link'] = entry.link
        news_item['description'] = entry.description
        if 'media_thumbnail' in entry:
            news_item['thumbnail'] = entry.media_thumbnail[0]['url']
        else:
            news_item['thumbnail'] = None
        news_feed['news_list'].append(news_item)
    return news_feed

@app.route('/')
def index():
    status_list_db = get_status()

    return render_template('index.html', status_list=build_status_list(status_list_db), news_feed=get_news_list())

@app.route('/info/test.php')
def vpn_status():
    vpn = request.args.get('vpn')
    timestamp = int(request.args.get('timestamp'))
    message = request.args.get('message')
    code = request.args.get('code')
    connection = get_db_connection()

    status = connection.execute('INSERT INTO status (code, message, timestamp, vpn) VALUES (?, ?, ?, ?) ON CONFLICT(vpn) DO UPDATE SET code=?,message=?,timestamp=? where vpn=?', (code, message, datetime.fromtimestamp(timestamp), vpn,code, message, datetime.fromtimestamp(timestamp), vpn))
    connection.commit()
    connection.close()
    return "", 200

@app.route('/keypress')
def process_keypress():
    keyboard = Controller()
    key_to_press = request.args.get('key')
    if key_to_press != '':
        if key_to_press == 'n' or key_to_press == 'p':
            keyboard.press(key_to_press)
        elif key_to_press == '5':
            with keyboard.pressed(Key.ctrl_l):
                keyboard.press('r')
        elif key_to_press == 'R':
            run(["/usr/sbin/reboot"])

    return "", 200

@app.route('/vpndata')
def render_status():
    status_list_db = get_status()

    return render_template('status.html', status_list=build_status_list(status_list_db))

@app.route('/newsdata')
def render_news():
    return render_template('news.html', news_feed=get_news_list())