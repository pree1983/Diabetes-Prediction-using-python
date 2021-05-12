from flask import Flask,render_template,request,redirect
from flask_mysqldb import MySQL
import yaml
app = Flask(__name__)
#configure database
#db = yaml.safe_load('db.yaml')
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':

        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = mysql.connection.cursor()
        cur.execute("insert into users(name,email)values(%s,%s)",(name,email))
        mysql.connection.commit()
        cur.close()
        return redirect('/users')
    return render_template("index.html")
@app.route('/users')
def users():
    cur=mysql.connection.cursor()
    resultValue =cur.execute("select * from users")
    if resultValue >0:
       userDetails =cur.fetchall()
    return render_template('users.html', userDetails= userDetails)

if __name__ == "__main__":
    app.run(debug=True)