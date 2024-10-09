from flask import Flask,request,render_template,redirect
import sqlite3

app = Flask(__name__)
con = sqlite3.connect("user.db", timeout=10, check_same_thread=False)

con.execute("create table if not exists mydata(name text,username text,mobile_no integer,password text)")
cur = con.cursor()


@app.route("/signup",methods=["GET","POST"])
def signup():
    if request.method == "POST":
        name = request.form["name"]
        username = request.form["u_name"]
        mobile_no = request.form["m_no"]
        password = request.form["pass"]
        confirm_password = request.form["c_pass"]
        if password == confirm_password:
            con.execute("insert into mydata(name,username,mobile_no,password) values(?,?,?,?)",(name,username,mobile_no,password))
            con.commit()
            return redirect("/login")
        else:
            return render_template("signup.html")
    return render_template("signup.html")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":  
        luname = request.form['luname'] 
        lpass = request.form['lpass']
        cur.execute("select * from mydata")
        a = cur.fetchall()
        for i in a:
            if luname in i[1]:
                if lpass in i[3]:         
                    return render_template("success.html",name =i[0])
                else:
                    return render_template("login.html",message = "invalid password")
            else:
                return render_template("login.html", message = "invalid username")
        return render_template("login.html", message="Invalid login credentials")
            
    else:
        return render_template("login.html")
    
   
if __name__ == '__main__':
    app.run(debug=True, port = 7000)

