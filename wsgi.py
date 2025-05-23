from flask import Flask, render_template
import os
import random

app = Flask(__name__)

def get_random_video():
    video_dir = os.path.join(app.static_folder, 'content/videos')
    video_files = [f for f in os.listdir(video_dir) if f.endswith('.mp4')]
    return random.choice(video_files)


@app.route('/')
def home():
    random_video = get_random_video()
    return render_template('base.html', video_filename=random_video)

@app.route('/repertoire')
def repertoire():
    random_video = get_random_video()
    return render_template('repertoire.html', video_filename=random_video)



@app.route('/repertoire/<string:wine_name>')
def wine(wine_name):
    random_video = get_random_video()
    return render_template('wine.html', wine_name=wine_name, video_filename=random_video)

@app.route('/agenda')
def agenda():
    random_video = get_random_video()
    return render_template('agenda.html', video_filename=random_video)


@app.route('/about')
def about():
    random_video = get_random_video()
    return render_template('about.html', video_filename=random_video)

@app.route('/contact')
def contact():
    random_video = get_random_video()
    return render_template('contact.html', video_filename=random_video)

@app.route('/join')
def join():
    random_video = get_random_video()
    return render_template('contact.html', video_filename=random_video)


if __name__ == '__main__':
    app.run(debug=True)