from flask import render_template
from flask import *                                           # This is a single-line comment in Python.
                                                  
app=Flask(__name__)



@app.route("/")                                 
def home(): 
    return "Web Server Gateway Interfaceeeeeeeeeeeeeeeeeee"
#app.add_url_rule("/","home",home)


@app.route("/tml")                        #without inherit
def index():
    courses=["C","C++","JAVA","PYTHON","HTML","CSS"]
    return render_template("index1.html",name= "tamil",courses=courses)

@app.route("/file")                       #with inherit
def flow(): 
    return render_template("index2.html")

@app.route("/about")
def about(): 
    return render_template("about.html")

@app.route("/layout")
def layout(): 
    return render_template("layout.html")  

    
@app.route("/table")
def table(): 
    return render_template("table.html")

@app.route("/form1")                     #html form
def form(): 
    return render_template("form1.html")
    return "Web Server Gateway"

@app.route("/bootstrap")
def boots(): 
     return render_template("boots.html")

#dynamic route:
@app.route("/users/<name>")
def users(name): 
    return"<h2>hi {}</h2>".format(name[-5:-2])
    return"<h2>hi {}</h2>".format(name[40])
    return"<h2>hi {}</h2>".format(name.upper())
    return"<h2>hi {}</h2>".format(name[0:2])


# USER GET VALUE,IF ELSE,FOR LOOP: 
 
@app.route("/condition")
def ss():
    ranges=[{"languages":"python","author":"guido bvan ro"},{"languages":"html","author":"beners lee"},
            {"languages":"flask","author":"arminronacher"}]
    return render_template("conditional.html",author="Armin Ronacher",post=ranges,arminRanacher=True)     
     
#type2 inherit:

'''@app.route("/")
def inherit(): 
    return render_template("base1.html")

@app.route("/inheridance1")
def inherit1(): 
    return render_template("home.html")

@app.route("/inheridance2")
def inherit2(): 
    return render_template("user.html")

@app.route("/inheridance3")
def inherit3(): 
    return render_template("contact.html")'''

#redirecter:
''' @app.route("/home")
def home1(): 
    return render_template('filter.html',a="hai!...hello")

@app.route("/about")
def againhome(): 
    return redirect("/home")                             #go to first url_page (home page)

@app.route("/visit")
def agnhome(): 
    return redirect(url_for("home1"))   '''          #if using function name mentinon that url_f   or,for first urlpage

#eg=2:
''' @app.route("/home2")
def house(): 
    return render_template('filter2.html',MVT="model views template")

@app.route("/module")
def againhouse(): 
    return redirect("/home2")

@app.route("/watch")
def agnhouse(): 
    return redirect(url_for("house"))   

@app.route("/welcome")
def welcome(): 
    return redirect(url_for("house"))  '''

@app.route("/doctor")
def doctor(): 
    return render_template("/apololayout.html")

@app.route("/nurse")
def nurse(): 
    return render_template("/apoloindex.html")  

@app.route("/patient") 
def patient(): 
    return render_template("/apoloabout.html") 
































if __name__=="__main__":
    app.run(debug=True)     #port num can change oueself,defalt is 5000,port =4000










 

