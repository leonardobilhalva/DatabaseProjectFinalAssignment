-- DROP TABLE IF EXISTS QuantitativoAlunosGraduacao;

CREATE TABLE IF NOT EXISTS QuantitativoAlunosGraduacao (
    CodCurso INT,
    NomeCurso TEXT,
    Ano INT,
    Periodo INT,
    Vinculados INT,
    Matriculados INT,
    Ingressantes INT,
    Diplomados INT,
    Evadidos INT -- Remove the comma here
);

CREATE TABLE IF NOT EXISTS ProcessoSeletivosGraduacao (
    Ano INT,
    ProcessoSeletivo TEXT,
    Curso TEXT,
    SiglaModalidadeVaga TEXT,
    ModalidadeVaga TEXT,
    Semestre INT,
    NrVagas INT -- Remove the comma here
);
