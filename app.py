from flask import Flask, render_template
import json
import os

app = Flask(__name__)

@app.route('/')
def home():
    all_images = []
    with open('dungeons.json') as all_dungeons:
        data = json.load(all_dungeons)
        for dungeon in data:
            all_images.append(data[dungeon]["image"])
    return render_template('home.html', all_images=all_images)

@app.route('/dungeon/<string:dungeon>')
def dungeon(dungeon):
    with open('dungeons.json') as all_dungeons:
        dungeon = dungeon.replace("_", " ").replace(".jpg", "")
        data = json.load(all_dungeons)
        data = data[dungeon]
        print(data)
        image = data["image"]
    return render_template('dungeon.html', image=image, dungeon=dungeon, data=data)
if __name__ == '__main__':
    app.secret_key = "as"
    app.run(debug=True)
