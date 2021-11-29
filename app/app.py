import re
from flask import Flask, render_template, request

app = Flask(__name__)

result = dict() # 입력 정보 유지를 위한 global 선언

@app.route('/')
def student():
   return render_template('main.html')

@app.route('/result', methods=['GET', 'POST'])
def detail():
   global result # global 선언된 result를 바로 result 화면에 넘겨주기 위함
   if request.method == 'POST':
      return render_template("result.html",result = result)

@app.route('/detail', methods = ['POST', 'GET'])
def result():
   global result
   if request.method == 'POST':
      result = dict()
      result['Name'] = request.form.get('Name')
      result['StudentNumber'] = request.form.get('StudentNumber')
      result['Gender'] = request.form.get('Gender')
      result['Major'] = request.form.get('Major')
      return render_template("detail.html",result = result)

if __name__ == '__main__':
   app.run(host="0.0.0.0", debug=True, port=80)
