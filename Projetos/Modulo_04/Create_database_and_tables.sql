CREATE DATABASE escola;

CREATE TABLE escola.aluno (
 id serial,
 cpf varchar(11),
 nome varchar(50),
 endereco varchar(100),
 telefone varchar(15),
 dt_nascimento date,
 primary key (cpf)
);

CREATE TABLE escola.departamento (
codigo int,
nome varchar(50),
primary key (codigo)
);

CREATE TABLE escola.professor (
matricula int,
nome varchar(50),
endereco varchar(100),
telefone varchar(15),
dt_nascimento date,
cod_depto int,
primary key (matricula),
foreign key (cod_depto) references escola.departamento(codigo)
);

CREATE TABLE escola.curso (
codigo int,
nome varchar(50),
descricao varchar(150),
cod_depto int,
primary key (codigo),
foreign key (cod_depto) references escola.departamento(codigo)
);

CREATE TABLE escola.disciplina (
codigo int,
nome varchar(50),
qtd_creditos int,
matricula_prof int,
primary key (codigo),
foreign key (matricula_prof) references escola.professor(matricula)
);

CREATE TABLE escola.curso_disciplinas (
cod_curso int,
cod_disciplina int,
foreign key (cod_curso) references escola.curso(codigo),
foreign key (cod_disciplina) references escola.disciplina(codigo)
);

CREATE TABLE escola.matriculas_curso (
data_matricula timestamp default now(),
cod_curso int,
cpf_aluno varchar(11),
foreign key (cod_curso) references escola.curso(codigo),
foreign key (cpf_aluno) references escola.aluno(cpf)
);

CREATE TABLE escola.matriculas_disciplinas (
data_matricula timestamp default now(),
cpf_aluno varchar(11),
cod_disc int,
foreign key (cod_disc) references escola.disciplina(codigo),
foreign key (cpf_aluno) references escola.aluno(cpf)
);

CREATE TABLE escola.prereq (
cod_cod_disc int,
cod_cod_disc_depen int,
foreign key (cod_cod_disc) references escola.disciplina(codigo),
foreign key (cod_cod_disc_depen) references escola.disciplina(codigo)
);

