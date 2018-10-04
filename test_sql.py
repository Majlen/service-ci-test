import psycopg2

cur = None
conn = None

def setup_module():
	global conn, cur
	conn = psycopg2.connect(dbname="test", user="test", password="test", host="postgres")
	cur = conn.cursor()

def test_sql_select():
	cur.execute("select handle from handle where resource_id = 25142")
	result = cur.fetchone()
	assert result[0] == '11025/13829'

def teardown_module():
	cur.close()
	conn.close()
