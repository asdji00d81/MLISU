### Integrate HTML With Flask
### HTTP verb GET And POST

##Jinja2 template engine
'''
{%...%} conditions,for loops
{{    }} expressions to print output
{#....#} this is for comments
'''
from flask import Flask,redirect,url_for,render_template,request

app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template('index.html') # show first about index1.html

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=50:
        res="PASS"
    else:
        res='FAIL'
    exp={'score':score,'res':res} #uncheck this
    return render_template('result.html',result=exp)  # uncheck this  second
    #return render_template('results.html',result=res) # initially check this


@app.route('/success1/<int:score>')
def success1(score):
    return render_template('results.html',result=score)  #initially check this THEN CHECK FULLY

@app.route('/fail/<int:score>')
def fail(score):
    return "The Person has failed and the marks is "+ str(score)

### Result checker
@app.route('/results/<int:score>')
def results(score):
    result=""
    if score<50:
        result='fail'
    else:
        result='success'
    return redirect(url_for(result,score=score))

### Result checker submit html page
@app.route('/submit',methods=['POST','GET'])
def submit():
    marks=0
    if request.method=='POST':
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        data_science=float(request.form['datascience'])
        marks=(science+maths+c+data_science)/4
    res=""
    return redirect(url_for('success',score= marks)) #CHECK WITH SUCESS1 then SUCCESS
    #return redirect(url_for('results', score=marks)) # check this later 
    #return redirect(url_for('success1', score=marks))  # this is in html papge itself caluclation

if __name__=='__main__':
    app.run(debug=True)