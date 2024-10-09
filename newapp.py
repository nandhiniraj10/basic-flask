from flask import Flask, render_template, request, redirect, url_for
from  flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///C:/Users/nandh/Downloads/CRUD - Copy (2)/CRUD - Copy/newapp.pytest.db'
db = SQLAlchemy(app)

# Define a model for the database
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    def __repr__(self):
        return '<User id=%s, name=%s, email=%s>' % (self.id, self.name, self.email)
        # return '<User id=%r, name=%r, email=%r>' % (self.id, self.name, self.email)
        # return '<User %r>' % self.name

# Create the database tables
with app.app_context():
    db.create_all()


# Define routes for the app
@app.route('/')
def index():
    # Get all users from the database
    users = User.query.all()
    # Render the index.html template with the users data
    return render_template('index.html', users=users)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        # Get the form data from the request
        name = request.form['name']
        email = request.form['email']
        # Create a new user object with the form data
        user = User(name=name, email=email)
        # Add the user to the database session and commit
        db.session.add(user)
        db.session.commit()
        # Redirect to the index page
        return redirect(url_for('index'))
    else:
        # Render the create.html template
        return render_template('create.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    # Get the user from the database by id
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        # Update the user attributes with the form data
        user.name = request.form['name']
        user.email = request.form['email']
        # Commit the changes to the database
        db.session.commit()
        # Redirect to the index page
        return redirect(url_for('index'))
    else:
        # Render the update.html template with the user data
        return render_template('update1.html', user=user)

@app.route('/delete/<int:id>')
def delete(id):
    # Get the user from the database by id
    user = User.query.get_or_404(id)
    # Delete the user from the database session and commit
    db.session.delete(user)
    db.session.commit()
    # Redirect to the index page
    return redirect(url_for('index'))

# Run the app if this file is executed
if __name__ == '__main__':
    app.run(debug=True)
    
    

