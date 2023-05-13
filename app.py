from flask import Flask,render_template,request

app =Flask(__name__)

@app.route('/',methods=['GET','POST'])
def bmical():
    bmi=''
    if request.method=="POST":
        w=int(request.form['weight'])
        h=float(request.form['height'])
        bmi=str(w/(h*h))
    return render_template('index.html',bmi=bmi)

app.run(debug=True)