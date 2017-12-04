from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
	out = "<h1> Examples </h1>\n"
	for f in os.listdir('data'):
		[name, fileType] = f.split('.')
		if fileType == "geojson":
			out += '<p><a href="map/' + name + '">' + name + '</a></p>\n'
	return out
@app.route('/map/<mapName>')
def map(mapName = None):
	mapData = ""
	mapFile = open("data/" + mapName + ".geojson", 'r').read()
	return render_template('map.html', mapData = mapFile).replace("&#39;", "'").replace("&#34;", "'")
