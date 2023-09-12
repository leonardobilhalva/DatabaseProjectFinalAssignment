import time
import psycopg2

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
        "SELECT nome_curso, SUM(evadidos) as total_evadidos FROM quantitativo_alunos WHERE ano >= 2023 - 5 GROUP BY nome_curso ORDER BY total_evadidos DESC LIMIT 5;")
    rows = cursor.fetchall()


def queryCourseEvasionTwo(cursor):

    cursor.execute(
        "SELECT nome_curso, SUM(evadidos) as total_evadidos FROM quantitativo_alunos WHERE ano >= 2023 - 13 GROUP BY nome_curso ORDER BY total_evadidos DESC LIMIT 5;")
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

        with open('files/dadosabertos_graduacao_processos_seletivos.csv', 'r') as file:
            cursor.copy_expert(
                sql="COPY Processo_Seletivos_Graduacao FROM stdin WITH CSV HEADER DELIMITER ';'", file=file)
        conn.commit()  # add data from csv to ProcessoSeletivosGraduacao and commit

        with open('files/dadosabertos_graduacao_quantitativo-de-alunos.csv', 'r') as file:
            cursor.copy_expert(
                sql="COPY Quantitativo_Alunos_Graduacao FROM stdin WITH CSV HEADER DELIMITER ';'", file=file)
        conn.commit()  # add data from csv to QuantitativoAlunosGraduacao and commit

        while True:  # execute queries here
            print('The last value inserted is: zero')
            queryGeneral(cursor)

            time.sleep(5)

    except Exception as e:
        print('Error:', str(e))

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:  # close cursor and connection they are defined
            conn.close()
