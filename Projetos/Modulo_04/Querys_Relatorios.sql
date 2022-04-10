select c.nome as curso, a.* 
from aluno a 
inner join matriculas_curso mc 
	on a.cpf = mc.cpf_aluno
inner join curso c 
	on c.codigo = mc.cod_curso 

	
	
select c.nome as curso
, d.nome as disciplina
from curso c 
inner join curso_disciplinas cd 
	on c.codigo = cd.cod_curso 
inner join disciplina d 
	on d.codigo = cd.cod_disciplina 
order by 1, 2



select a.cpf, a.nome, d.nome as disciplina 
from aluno a 
inner join matriculas_disciplinas md  
	on a.cpf = md.cpf_aluno 
inner join disciplina d 
	on d.codigo = md.cod_disc 
order by 1, 3



select p.nome as professor, d.nome as disciplina 
from professor p 
inner join disciplina d 
on d.matricula_prof = p.matricula 
order by 1, 2



select d.nome as disciplina
, d2.nome as dependencia 
from disciplina d 
inner join prereq p 
	on p.cod_cod_disc = d.codigo 
inner join disciplina d2 
	on d2.codigo = p.cod_cod_disc_depen 
order by 1, 2



select  c.nome as curso,
avg(floor(DATEDIFF(sysdate(), a.dt_nascimento)/365)) as media_idade
from aluno a 
inner join matriculas_curso mc 
	on mc.cpf_aluno = a.cpf
inner join curso c 
	on c.codigo = mc.cod_curso 
group by 1



select d.nome as departamento 
, c.nome as curso
from departamento d 
inner join curso c on c.cod_depto = d.codigo 
order by 1, 2

