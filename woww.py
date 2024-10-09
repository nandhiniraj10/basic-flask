from flask import * 


app=Flask(__name__)


@app.route('/')
def index():
    return render_template('forme.html')

'''@app.route('/submit_form', methods=['POST'])
def submit_form():
    course = request.form.get('course')
    skillpercentage = request.form.get('skill percentage')
    return render_template('result.html', course=course, skillpercentage=skillpercentage)'''

@app.route('/submit', methods=['POST'])
def  submit():
    return "sucessfully submited!"   



if __name__=="__main__":
    app.run(debug=True) 