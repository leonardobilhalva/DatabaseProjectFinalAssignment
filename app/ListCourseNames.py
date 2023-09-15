import csv
import difflib


def extrairNome(nomeCompleto):
    partes = nomeCompleto.split('-')
    nome = partes[0].rstrip()

    return nome


def logestPrefixMatching(names):
    names = [name.lower() for name in names]

    prefixDict = {}
    for name in names:
        for i in range(len(name) + 1):
            prefix = name[:i]
            if prefix not in prefixDict:
                prefixDict[prefix] = []
            prefixDict[prefix].append(name)

    commonPrefixes = [prefix for prefix,
                      names in prefixDict.items() if len(names) > 1]

    result = set()
    for prefix in commonPrefixes:
        result.update(prefixDict[prefix])

    result = [name.capitalize() if name.isupper() else name for name in result]

    return result


def ListCourseNames():
    with open('files/dadosabertos_graduacao_processos_seletivos.csv', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv, delimiter=';')

        cursos = []

        for linha in leitor_csv:
            curso = linha['Curso']
            cursos.append(curso)

    with open('files/dadosabertos_graduacao_quantitativo-de-alunos.csv', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv, delimiter=';')

        for linha in leitor_csv:
            curso = linha['NomeCurso']
            cursos.append(curso)

    cursos = [extrairNome(curso) for curso in cursos]
    resultado = logestPrefixMatching(cursos)
    resultado.sort()

    # os tres problemas que temos que mudar na mão
    resultado.remove("com. social")
    resultado.remove("ciências jur/soc")
    resultado.remove("bach. i. em ciência e tecnologia")

    return resultado
