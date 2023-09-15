import time
import psycopg2
import Seed

db_name = 'database'
db_user = 'username'
db_pass = 'secret'
db_host = 'localhost'
db_port = '5432'


def queryGeneral(cursor):

    cursor.execute(
        "SELECT * FROM processo_seletivos_graduacao WHERE curso like 'Admin%'")
    rows = cursor.fetchall()


def queryCourseEvasionOne(cursor):

    cursor.execute(
        "SELECT nome_curso, SUM(evadidos) as total_evadidos FROM quantitativo_alunos_graduacao WHERE ano >= 2023 - 5 GROUP BY nome_curso ORDER BY total_evadidos DESC LIMIT 5;")
    rows = cursor.fetchall()


def queryCourseEvasionTwo(cursor):

    cursor.execute(
        "SELECT nome_curso, SUM(evadidos) as total_evadidos FROM quantitativo_alunos_graduacao WHERE ano >= 2023 - 13 GROUP BY nome_curso ORDER BY total_evadidos DESC LIMIT 5;")
    rows = cursor.fetchall()


def queryCourseGradutadedAlumns(cursor):

    cursor.execute(
        "SELECT nome_curso, SUM(diplomados) as total_diplomados FROM quantitativo_alunos_graduacao GROUP BY nome_curso ORDER BY total_diplomados DESC LIMIT 5;")
    rows = cursor.fetchall()


def queryCourseEntrants(cursor):

    cursor.execute(
        "SELECT nome_curso, SUM(ingressantes) as total_ingressantes FROM quantitativo_alunos_graduacao GROUP BY nome_curso ORDER BY total_ingressantes DESC LIMIT 5;")
    rows = cursor.fetchall()


def queryCourseEvasionThree(cursor):

    cursor.execute(
        "SELECT nomecurso, ((evadidos/vinculados)*100) as porcentagem_evadidos FROM quantitativo_alunos_graduacao ORDER BY porcentagem_evadidos DESC LIMIT 5;")
    rows = cursor.fetchall()


if __name__ == '__main__':
    print('Application started')
    conn = None  # Initialize conn and cursor variables
    cursor = None

    try:
        conn = psycopg2.connect(
            database=db_name, user=db_user, password=db_pass, host=db_host, port=db_port
        )
        cursor = conn.cursor()  # connect to database and create a cursor

        cursor.execute("SELECT * FROM Processo_Seletivos_Graduacao")
        queryResult = cursor.fetchall()
        cursor.execute("SELECT * FROM Quantitativo_Alunos_Graduacao")
        queryResult += cursor.fetchall()
        if len(queryResult) == 0:
            print("Executing table seeding")
            Seed.Seed(cursor, conn)

    except Exception as e:
        print('Error:', str(e))

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:  # close cursor and connection they are defined
            conn.close()
