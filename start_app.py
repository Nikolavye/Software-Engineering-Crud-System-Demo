from flask import Flask, render_template, request

import mysql_database

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')


@app.route('/itemsform')
def show_item_form():
    return render_template('itemsform.html')


@app.route('/itemscreated', methods=['POST'])
def add_item():
    print('item created page')
    print(request.form)
    name = request.form.get('items_name')
    quantity = request.form.get('items_quantity')
    price = request.form.get('items_price')
    print(name, quantity, price)
    sql = f"""insert into items(name, quantity ,price) values('{name}', {quantity}, {price})"""
    print(sql)
    mysql_database.insert_update(sql)
    sql = 'SELECT * FROM items'
    res = mysql_database.query(sql)
    return render_template('allitems.html', items=res)


@app.route('/allitems')
def show_all_items():
    sql = 'SELECT * FROM items'
    res = mysql_database.query(sql)
    return render_template('allitems.html', items=res)


@app.route('/singleitem/<id>')
def show_single_item(id):
    sql = f'SELECT * FROM items WHERE id = {id}'
    res = mysql_database.query(sql)
    return render_template('singleitem.html', item=res[0])


@app.route('/deleteitem/<id>')
def delete_item(id):
    sql = f'delete from items where id = {id}'
    mysql_database.insert_update(sql)
    sql = 'SELECT * FROM items'
    res = mysql_database.query(sql)
    return render_template('allitems.html', items=res)


@app.route('/updateitem/<id>', methods=['POST'])
def show_update_item(id):
    name = request.form.get('items_name')
    quantity = request.form.get('items_quantity')
    price = request.form.get('items_price')
    print(name, quantity, price)
    sql = f"""UPDATE items
                SET name = '{name}', quantity= {quantity}, price = {price}
                WHERE id={id};"""
    mysql_database.insert_update(sql)
    sql = 'SELECT * FROM items'
    res = mysql_database.query(sql)
    return render_template('allitems.html', items=res)


if __name__ == '__main__':
    app.run(debug=True)
