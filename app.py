from flask import Flask, render_template, redirect, url_for
from form_client import FormClient

app = Flask(__name__)

app_title='Gym app'

app.config['SECRET_KEY'] = 'llave_secreta'

@app.route('/')
@app.route('/index.html')
def start():
    app.logger.debug('Estamos en el path inicvial')
    datauser = FormClient()
    #return render_template('index.html', app_t=app_title, clients=client_db, form=client_form)
    return render_template('index.html', app_t=app_title,form=datauser)

@app.route('/showform/<name>')
def showform(name):
    return render_template("showform.html",datauser=name)

@app.route('/save', methods=['POST'])
def save():
    datauser = FormClient()
    if datauser.validate_on_submit():
        name = datauser.name.data
        password = datauser.password.data
        if name == 'mike' and password =='holamundo':
            return redirect(url_for('showform',name=name))
        else:
            error = 'User not found'
            return redirect(url_for('start',message=error))
    return redirect(url_for('start'))
    

if __name__ == '__main__':
    app.run(debug=True)