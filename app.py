from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage
import pandas as pd
import json
from flask import send_file
app = Flask(__name__)

@app.route('/upload')
def upload_file():
   return render_template('index.html')
	
@app.route('/uploader', methods = ['GET', 'POST'])
def upload_file2():
   if request.method == 'POST':
      f = request.files['file']
      df = json.load(f)
      df = pd.json_normalize(df)
      df1 = pd.DataFrame(df)
      df2 = df1.to_csv('sample2.csv', header=False,index=False)
      path = r"sample2.csv"
      return send_file(path, as_attachment=True)
		
if __name__ == '__main__':
   app.run(debug = True)