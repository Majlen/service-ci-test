import psycopg2

cur = None
conn = None

def setup_module():
	global conn, cur
	conn = psycopg2.connect(dbname="test", user="test", password="test", host="postgres")
	cur = conn.cursor()
	cur.execute("CREATE TABLE handle (handle VARCHAR(16), resource_id INTEGER)")
	cur.execute("INSERT INTO handle (handle, resource_id) VALUES ('11025/13829', 25142)")
	conn.commit()

def test_sql_select():
	cur.execute("SELECT handle FROM handle WHERE resource_id = 25142")
	result = cur.fetchone()
	assert result[0] == '11025/13829'

def teardown_module():
	cur.close()
	conn.close()
