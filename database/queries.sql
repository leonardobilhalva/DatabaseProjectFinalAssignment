SELECT ano, processo_seletivo, curso, nr_vagas FROM processo_seletivos_graduacao;

SELECT nome_curso, SUM(evadidos) AS total_evadidos
FROM quantitativo_alunos_graduacao
GROUP_BY nome_curso
ORDER BY total_evadidos DESC
LIMIT 5;

SELECT nome_curso, ano, periodo, ((evadidos*100/vinculados)) AS pct_evadidos
FROM quantitativo_alunos_graduacao
WHERE ((evadidos*100/vinculados)) < 100
ORDER BY pct_evadidos DESC
LIMIT 5;

SELECT nome_curso,ano,periodo,sum(evadidos) AS evadidos
FROM quantitativo_alunos_graduacao
GROUP BY nome_curso,ano,periodo
ORDER BY ano,periodo;
