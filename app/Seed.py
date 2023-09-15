import csv
import psycopg2
import ListCourseNames


def encontrar_melhor_correspondencia(prefixo, lista_de_palavras):
    melhor_correspondencia = None
    melhor_pontuacao = 0

    for palavra in lista_de_palavras:
        pontuacao = 0
        for i in range(min(len(prefixo), len(palavra))):
            if prefixo[i] == palavra[i]:
                pontuacao += 1
            else:
                break

        if pontuacao > melhor_pontuacao:
            melhor_correspondencia = palavra
            melhor_pontuacao = pontuacao

    return melhor_correspondencia


def Seed(cursor, conn):

    listCourseNames = ListCourseNames.ListCourseNames()

    with open('files/dadosabertos_graduacao_processos_seletivos.csv', newline='', encoding='utf-8') as file:
        csvReader = csv.DictReader(file, delimiter=';')
        for line in csvReader:
            originalCourse = line['Curso'].lower()

            if originalCourse == "com.social":
                newCourseName = "comunicação social"
            elif originalCourse == "ciências jur/soc":
                newCourseName = "ciências jurídicas e sociais"
            elif originalCourse == "bach. i. em ciência e tecnologia":
                newCourseName = "interdisciplinar em ciência e tecnologia"
            else:
                newCourseName = encontrar_melhor_correspondencia(
                    originalCourse, listCourseNames)

            cursor.execute('''
                    INSERT INTO Processo_Seletivos_Graduacao (ano, processo_seletivo, Curso, sigla_modalidade_vaga, modalidade_vaga, semestre, nr_vagas) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s)
                ''', (line['Ano'], line['ProcessoSeletivo'], newCourseName, line['SiglaModalidadeVaga'], line['ModalidadeVaga'], line['Semestre'], line['NrVagas']))
            conn.commit()

    with open('files/dadosabertos_graduacao_quantitativo-de-alunos.csv', newline='', encoding='utf-8') as file:
        csvReader = csv.DictReader(file, delimiter=';')
        for line in csvReader:
            originalCourse = line['NomeCurso'].lower()

            if originalCourse == "com.social":
                newCourseName = "comunicação social"
            elif originalCourse == "ciências jur/soc":
                newCourseName = "ciências jurídicas e sociais"
            elif originalCourse == "bach. i. em ciência e tecnologia":
                newCourseName = "interdisciplinar em ciência e tecnologia"
            else:
                newCourseName = encontrar_melhor_correspondencia(
                    originalCourse, listCourseNames)

            cursor.execute('''
                INSERT INTO quantitativo_alunos_graduacao (Cod_Curso, Nome_Curso, Ano, Periodo, Vinculados, Matriculados, Ingressantes, Diplomados, Evadidos)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                ''', (line['CodCurso'], newCourseName, line['Ano'], line['Periodo'], line['Vinculados'], line['Matriculados'], line['Ingressantes'], line['Diplomados'], line['Evadidos']))
            conn.commit()
