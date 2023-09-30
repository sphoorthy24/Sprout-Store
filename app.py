from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

def execute_query(query, params=None):
    mydb = mysql.connector.connect(
        host="localhost",
        user="Sphoorthy",
        password="Mikasa@910",
        database="arlinton_sprouts_store"
    )
    cursor = mydb.cursor()
    if params:
        cursor.execute(query, params)
    else:
        cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    mydb.commit()
    return result

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/display_item', methods=['POST'])
def display_item():
    item = request.form['item']
    # Execute an SQL query to retrieve data from the items table
    myresult = execute_query("SELECT * FROM item WHERE Iname=%s OR Iid=%s", (item, item,))
    if len(myresult) == 0:
        return "No item found."
    else:
        return render_template('item_details.html', rows=myresult)

@app.route('/add_item', methods=['POST'])
def add_item():
    Iname = request.form['Iname']
    Sprice = request.form['Sprice']
    Iid = request.form['IiD']
    # Execute an SQL query to insert a new row into the items table
    execute_query("INSERT INTO item (Iid, Iname, Sprice) VALUES (%s, %s, %s)", (Iid, Iname, Sprice,))
    return redirect(url_for('home'))

@app.route('/update_item', methods=['POST'])
def update_item():
    Iname = request.form['Iname']
    Sprice = request.form['Sprice']
    Iid = request.form['IiD']
    # Execute an SQL query to update an existing row in the items table
    execute_query("UPDATE item SET Iname=%s, Sprice=%s WHERE Iid=%s", (Iname, Sprice, Iid))
    return redirect(url_for('home'))

@app.route('/delete_item', methods=['POST'])
def delete_item():
    Iid = request.form['Iid']
    # Execute an SQL query to delete an existing row from the items table
    execute_query("DELETE FROM item WHERE Iid=%s", (Iid,))
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
