-DROP TABLE IF EXISTS QuantitativoAlunosGraduacao;

CREATE TABLE IF NOT EXISTS quantitativo_alunos_graduacao (
    Cod_Curso INT,
    Nome_Curso TEXT,
    Ano INT,
    Periodo INT,
    Vinculados INT,
    Matriculados INT,
    Ingressantes INT,
    Diplomados INT,
    Evadidos INT -- Remove the comma here
);

CREATE TABLE IF NOT EXISTS processo_seletivos_graduacao (
    Ano INT,
    Processo_Seletivo TEXT,
    Curso TEXT,
    Sigla_Modalidade_Vaga TEXT,
    Modalidade_Vaga TEXT,
    Semestre INT,
    Nr_Vagas INT -- Remove the comma here
);
