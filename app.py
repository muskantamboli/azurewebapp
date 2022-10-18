#importing the needed packages and modules
from flask import Flask, render_template, request, redirect
import textwrap
import pyodbc
app = Flask(__name__)
 
server = 'newserver789.database.windows.net'
database = 'sprint'
# username = 'azureuser'
# password = 'Azure@2022'
# cnxn = pyodbc.connect(
#     'DRIVER={ODBC Driver 17 for SQL Server}; \
#     SERVER='+ server +'; \
#     DATABASE='+ database +';\
#     Trusted_Connection=yes;'
# )

connection_string = 'Driver={ODBC Driver 17 for SQL Server};Server=tcp:newserver789.database.windows.net,1433;Database=sprint;Uid=adminuser;Pwd=Azure@2022;Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;'

cnxn: pyodbc.Connection = pyodbc.connect(connection_string)


#create a new cursor object from the connection
cur: pyodbc.Cursor = cnxn.cursor()





#Configure db
#db = yaml.load(open('db.yaml'))
# app.config['MYSQL_HOST'] = 'localhost'
# app.config['MYSQL_USER'] = 'root'
# app.config['MYSQL_PASS'] = ''
# app.config['MYSQL_DB'] = 'sprint'

# mysql = MySQL(app)

@app.route('/', methods=['GET','POST'])
def hello():
    if request.method == 'POST':
        #Fetch form data
        userDetails = request.form
        name = userDetails['name']
        email = userDetails['email']
        cur = cnxn.cursor()
        insert_query= textwrap.dedent('''INSERT INTO users(name, email) VALUES(?, ?);''')
        values = (str(name),str(email))
        cur.execute(insert_query,values)
        cnxn.commit()
        cur.close()
        return redirect('/users')
    return render_template('index.html')
 
@app.route('/users')
def users():
    cur = cnxn.cursor()
    cur.execute('SELECT * FROM users')
    # for row in cur:
    #     print(row)
    
    
    userDetails = cur.fetchall()
    print(userDetails)
    return render_template('users.html',userDetails=userDetails)

if __name__ == '__main__':
    app.run(debug=True, host='localhost')
