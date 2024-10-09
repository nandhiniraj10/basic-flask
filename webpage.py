from flask import Flask,render_template,request

ap=Flask(__name__)
details=[['Abdul','Aziz','abdul@gmail','aziz']]

@ap.route('/')
def about():
    return render_template('w1about.html')

@ap.route('/contact')
def contact():
    return render_template('w1contact.html')

@ap.route('/signup')
def signup():
    return render_template('w1signup.html')

@ap.route('/login')
def login():
    return render_template('w1login.html',err='')

@ap.route('/success',methods=['POST','GET'])
def success():
    if request.method=='POST':
        id=request.form.get('lid')
        pas=request.form.get('lpd')
        count=0
        for i in details:
            if i[2]==id and i[3]==pas:
                count+=1
                return render_template('w1success.html',f=i[0],l=i[1])
        if count==0:
            return render_template('w1login.html',err='Invalid Email or Password')

@ap.route('/created',methods=['POST','GET'])
def created():
    if request.method=='POST':
        f=request.form.get('fn')
        l=request.form.get('ln')
        
        id=request.form.get('sid')
        pas1=request.form.get('spd')
        pas2=request.form.get('spd1')
        count=0
        for i in details:
            if i[2]==id:
                count+=1
                break
        if count==1:
            return render_template('w1signup.html',msg='Email ID already exists !',)
        if pas1==pas2:        
                x=[]
                x.append(f)
                x.append(l)
                x.append(id)
                x.append(pas1)
                details.append(x)
                return render_template('w1created.html',f=f,l=l)
        else:
            return render_template('w1signup.html',msg='Create valid password !',f=f,l=l,e=id)

                
                
            
            


if __name__=='__main__':
    ap.run(debug=True)