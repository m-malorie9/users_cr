from flask_app import app

from flask import render_template, redirect, request, session

from flask_app.models.user import User

#for controllers have app routes for front end posting
@app.route('/users')
def users():
    #users = User.get_all()
    return render_template('users.html', users = User.get_all())#<- users = users 

@app.route('/users/new')
def create_user():
    return render_template('create.html')

@app.route('/users/create', methods = ["POST"])
def create():
    User.create_new_user(request.form)
    return redirect('/users')

#to call a class method use line 10 & 19, to get input from form use request.form

@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {
        'id':id
    }
    user = User.get_one_user(data)
    return render_template('edit.html', user = user)

@app.route('/users/<int:id>/update', methods = ["POST"])
def update_user(id):
    data = {
        'id':id,
        'first_name':request.form['first_name'],
        'last_name':request.form['last_name'],
        'email':request.form['email']
    }
    User.update_new_user(data)
    return redirect('/users')

@app.route('/users/<int:id>/delete')
def delete_user(id):
    data = {
        'id':id
    }
    user = User.delete_user(data)
    return redirect('/users')

@app.route('/users/<int:id>/show')
def show_user(id):
    data = {
        'id': id
    }
    user = User.get_one_user(data)
    return render_template("show.html", user = user)