import pickle
from flask import Flask, jsonify
from abusive import Abusive
from text_preprocessing import Text

class Model:

	def __init__(self):
		self.Model = pickle.load(open('/home/rijalfm2528/mysite/log_model.sav','rb'))

	def hate_speech(self):
		text_processed = Text(self.text).final_text
		result = self.Model.predict([text_processed])[0]

		return [result, Text(self.text).new_text]

	def abusive(self):
		result = Abusive(self.text)

		return result.results

	def result(self,text=None):
		HS = ""
		ABUSIVE =[]
		if text:
			self.text = text
			res = self.hate_speech()
			HS = res[0]
			text = res[1]
			ABUSIVE = self.abusive()

			return [text, HS, ABUSIVE]

		return []
