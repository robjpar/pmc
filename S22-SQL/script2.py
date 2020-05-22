import psycopg2

db_cred = 'dbname=database1 user=postgres password=postgres host=localhost port=5432'


def create_table():
    conn = psycopg2.connect(db_cred)
    cur = conn.cursor()
    cur.execute(
        'CREATE TABLE IF NOT EXISTS store (item TEXT, quantity INTEGER, price REAL)')
    conn.commit()
    conn.close()


create_table()


def insert(item, quantity, price):
    conn = psycopg2.connect(db_cred)
    cur = conn.cursor()
    cur.execute('INSERT INTO store VALUES (%s, %s, %s)',
                (item, quantity, price))
    conn.commit()
    conn.close()


insert('Wine Glass', 10, 5.5)
insert('Water Glass', 15, 6.7)
insert('Coffee Cup', 9, 3.4)


def view():
    conn = psycopg2.connect(db_cred)
    cur = conn.cursor()
    cur.execute('SELECT * FROM store')
    rows = cur.fetchall()
    conn.close()
    return rows


def delete(item):
    conn = psycopg2.connect(db_cred)
    cur = conn.cursor()
    cur.execute('DELETE FROM store WHERE item = %s', (item, ))
    conn.commit()
    conn.close()


delete('Wine Glass')


def update(quantity, price, item):
    conn = psycopg2.connect(db_cred)
    cur = conn.cursor()
    cur.execute('UPDATE store SET quantity = %s, price = %s WHERE item = %s', (
        quantity, price, item))
    conn.commit()
    conn.close()


update(11, 6.1, 'Water Glass')

print(view())
