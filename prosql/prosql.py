import pymysql


def connMySQL(database, table):
    conn = pymysql.connect(host="localhost",
                           user="root",
                           password="syncdb123!",
                           database=database,
                           charset="utf8",
                           cursorclass=pymysql.cursors.DictCursor

                           )

    cursor = conn.cursor()
    sql = "select `COLUMN_NAME`,`DATA_TYPE` from information_schema.columns where table_schema = '{}' and TABLE_NAME= '{}'" \
        .format(database, table)
    print(sql)
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)


def giveSugar(results):
    for result in results:
        column_name = result["COLUMN_NAME"]
        suger = result["DATA_TYPE"].lower()
        if suger in ("int", "tinyint"):
            pass
        elif suger in ("char", "varchar"):
            print("char")
        elif suger in ("float", "double"):
            print("double")


if __name__ == '__main__':
    database = 'ruoze'
    table = "user"
    connMySQL(database, table)
