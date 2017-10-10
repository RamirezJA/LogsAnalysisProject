import psycopg2

DB_NAME = "news"

def dbconnect():
    db = psycopg2.connect("dbname=news")
    cur = db.cursor()
    return db, cur


def top_articles():
    db, cur = dbconnect()
    cur.execute("SELECT articles.title, count(log.path) as amount FROM articles, log WHERE log.path Like concat('%', articles.slug, '%') GROUP BY articles.title ORDER BY amount desc limit 3;")
    results = cur.fetchall()
    print "1. Three most popular articles of all time"
    print "-" * 50
    for line in results:
        print line
    db.close()


def top_authors():
    db, cur = dbconnect()
    cur.execute("SELECT authors.name, count(log.status) as total FROM authors, articles, log WHERE articles.author = authors.id and log.status = '200 OK' and log.path like concat('%', articles.slug, '%') GROUP BY authors.name ORDER BY total desc;")
    results = cur.fetchall()
    print "\n2. Who are the most popular article authors of all time?"
    print "-" * 50
    for line in results:
        print line
    db.close()

    
def top_error():
    db, cur = dbconnect()
    cur.execute("SELECT to_char(http_cuatros.date, 'MM/DD/YYYY'), round((http_cuatros.numbers*1.0 / add_all.numbers*1.0)*100, 2) per FROM http_cuatros, add_all WHERE http_cuatros.date = add_all.date and (http_cuatros.numbers*1.0 / add_all.numbers*1.0)*100 > 1 ORDER BY per desc;")
    results = cur.fetchall()
    print "\n3. On which days did more than 1% of requests lead to errors?"
    print "-" * 50
    for line in results:
        print "On " + str(line[0]) + " had " + str(line[1]) + "% of errors"
    db.close()

    
top_articles()
top_authors()
top_error()