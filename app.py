from flask import render_template
from flask import Flask, request, jsonify
from model import Model
from nltk import word_tokenize
import os

Model = Model()

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
	if request.form:
		text = request.form['text']
		res = Model.result(text)
		if len(res) > 0:
			print(word_tokenize(res[0]))
			print(res)
			abusive_list = res[2].keys()
			return render_template('index.html', source=text, text=word_tokenize(res[0]), HS=str(res[1]), abusive_dict=res[2], abusive=abusive_list)

	return render_template('index.html')



if __name__ == '__main__':
	app.run(debug = True)