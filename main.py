from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True


@app.route("/signup", methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    password2 = request.form['password2']
    email = request.form['email']
    username_error = ''
    password_twice_error = ''
    password_error = ''
    password_match_error = ''
    email_error = ''
    error_count = 0

    if username == '':
        username_error = "Please enter a valid username."
        error_count += 1
#        return render_template('signup.html', username_error=username_error, username=username, email=email)
    if password == '' or password2 == '':
        password_twice_error = "Please enter your password twice."
        error_count += 1
#        return render_template('signup.html', error=password_twice_error, username=username, email=email)
    for char in username:
        if char == ' ':
            username_error = "Please enter a valid username."
            error_count += 1
#            return render_template('signup.html', error=error, username=username, email=email)
    for char in password:
        if char == ' ':
            password_error = "Please enter a valid password."
            error_count += 1
#            return render_template('signup.html', error=error, username=username, email=email)  
    u_len = len(username)
    p_len = len(password)
    e_len = len(email)
    if u_len > 20 or u_len < 3:
        username_error = "Please enter a valid username."
        error_count += 1
#        return render_template('signup.html', error=error, username=username, email=email)  
    if p_len > 20 or p_len < 3:
        password_error = "Please enter a valid password."
        error_count += 1
#        return render_template('signup.html', error=error, username=username, email=email) 
    if password != password2:
        password_match_error = "Your passwords do not match."
        error_count += 1
#        return render_template('signup.html', error=error, username=username, email=email)
    if e_len > 0:
        for char in email:
            if char == ' ':
                email_error = "Please enter a valid email."
                error_count += 1
#                return render_template('signup.html', error=error, username=username, email=email) 
            if e_len > 20 or e_len < 3:
                email_error = "Please enter a valid email."
                error_count += 1
#                return render_template('signup.html', error=error, username=username, email=email)
            x = 0
            y = 0
            for char in email:
                if char == '.':
                    x += 1
                if char == '@':
                    y += 1
            if x != 1 or y != 1:
                email_error = "Please enter a valid email."
                error_count += 1
#                return render_template('signup.html', error=error, username=username, email=email)
    if error_count == 0:
        return render_template('welcome.html', username=username)
    else:
        return render_template('signup.html', username=username, email=email, username_error=username_error, password_match_error=password_match_error, password_twice_error=password_twice_error, password_error=password_error, email_error=email_error)




@app.route("/")
def index():
    
    return render_template('signup.html')

app.run()
