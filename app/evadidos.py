import time
import psycopg2
import matplotlib.pyplot as plt
import numpy as np

# query para usar
# SELECT count(*) as matriculados, ano, semestre, curso FROM processo_seletivos_graduacao WHERE curso like 'Admin%' GROUP BY curso, ano, semestre ORDER BY ano, semestre
# SELECT ano,periodo,sum(evadidos) AS evadidos FROM quantitativo_alunos_graduacao WHERE nome_curso like 'CIÊNCIA DA COMPUTAÇÃO' GROUP BY nome_curso,ano,periodo ORDER BY ano,periodo;

db_name = 'projetobd'
db_user = 'postgres'
db_pass = 'postgres'
db_host = 'localhost'
db_port = '5432'

def evadidos(cursor, curso):
    cursor.execute(
        "SELECT sum(evadidos) AS evadidos FROM quantitativo_alunos_graduacao WHERE nome_curso = '%s' GROUP BY nome_curso,ano,periodo ORDER BY ano,periodo;"%(curso))
    rows = cursor.fetchall()
    return rows

def semestres(cursor):
    cursor.execute(
        "SELECT ano,periodo FROM quantitativo_alunos_graduacao GROUP BY ano,periodo ORDER BY ano,periodo;")
    rows = cursor.fetchall()
    return rows

def plot(cursos, semestres):
    x = np.arange(len(semestres))  # the label locations
    width = 0.25  # the width of the bars
    multiplier = 0

    fig, ax = plt.subplots(layout='constrained')
    fig.set_size_inches(20, 6)
    for attribute, measurement in cursos.items():
        offset = width * multiplier
        rects = ax.bar(x + offset, measurement, width, label=attribute)
        ax.bar_label(rects, padding=3)
        multiplier += 1

    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Nro de Evadidos')
    ax.set_title('Estudantes Evadidos por Curso')
    ax.set_xticks(x + width, semestres)
    ax.legend(loc='upper left', ncols=3)
    # ax.set_ylim(0, 250)

    plt.savefig('save1.png', dpi=300, bbox_inches='tight')


if __name__ == '__main__':
    print('Application started')
    conn = None
    cursor = None

    try:
        conn = psycopg2.connect(
            database=db_name, user=db_user, password=db_pass, host=db_host, port=db_port
        )
        cursor = conn.cursor()  # connect to database and create a cursor

        raw_cursos = ["CIÊNCIA DA COMPUTAÇÃO", "ENGENHARIA CIVIL", "CIÊNCIAS JURÍDICAS E SOCIAIS"]
        semestres = ["%s/%s"%(s[0],s[1]) for s in semestres(cursor)]
        cursos = {}
        for curso in raw_cursos:
            data = [e[0] for e in evadidos(cursor, curso)]
            cursos[curso] = data
        print(cursos)
        plot(cursos,semestres)


        
    except Exception as e:
        print('Error:', str(e))

    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:  # close cursor and connection they are defined
            conn.close()
