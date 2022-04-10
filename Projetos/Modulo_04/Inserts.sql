INSERT INTO escola.aluno
(cpf, nome, endereco, telefone, dt_nascimento)
VALUES('12345678911', 'Lucas Santos', 'Rua grupiara 100 - Morumbi', '34-3255-3577', '2000-11-13');

INSERT INTO escola.aluno
(cpf, nome, endereco, telefone, dt_nascimento)
VALUES('12345678445', 'Paulo Silva', 'Rua mexico 100 - Morumbi', '34-3232-1000', '2001-12-28');

INSERT INTO escola.aluno
(cpf, nome, endereco, telefone, dt_nascimento)
VALUES('55544422220', 'Leia Soares', 'Avenida Sao Paulo 500 - Umuarama', '34-3232-2000', '2003-05-14');

INSERT INTO escola.aluno
(cpf, nome, endereco, telefone, dt_nascimento)
VALUES('33322244455', 'Luan Silva', 'Avenida Floriano Peixoto 1000 - Brasil', '34-3232-3000', '2001-08-14');

INSERT INTO escola.aluno
(cpf, nome, endereco, telefone, dt_nascimento)
VALUES('11122244445', 'Cleiton Pereira', 'Avenida Rio de Janeiro 5788 - Centro', '34-3232-5544', '2001-07-14');

INSERT INTO escola.departamento
(codigo, nome)
VALUES(1, 'Ciências Biológicas');

INSERT INTO escola.departamento
(codigo, nome)
VALUES(2, 'Ciências Sociais Aplicadas');

INSERT INTO escola.departamento
(codigo, nome)
VALUES(3, 'Ciências Exatas');

INSERT INTO escola.departamento
(codigo, nome)
VALUES(4, 'Ciências Jurídicas');

INSERT INTO escola.professor
(matricula, nome, endereco, telefone, dt_nascimento, cod_depto)
VALUES(1010, 'Matheus Silva', 'Av Gomes 33 - Sao Gotardo', '34-32323550', '1980-10-20', 1);

INSERT INTO escola.professor
(matricula, nome, endereco, telefone, dt_nascimento, cod_depto)
VALUES(1015, 'Silvia Costa', 'Av Floriano 5553 - Segismundo', '34-44553322', '1990-05-14', 3);

INSERT INTO escola.professor
(matricula, nome, endereco, telefone, dt_nascimento, cod_depto)
VALUES(1020, 'Leonardo Brasil', 'Av Afonso Pena 3257 - Santa Monica', '34-55664483', '1991-06-30', 2);

INSERT INTO escola.professor
(matricula, nome, endereco, telefone, dt_nascimento, cod_depto)
VALUES(1030, 'Gabriel Brasil', 'Av Afonso Pena 2000 - Santa Monica', '34-55664483', '1991-06-15', 4);

INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(1, 'Botanica', 'Botanica', 1);

INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(2, 'Bioquimica', 'Bioquimica', 1);

INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(3, 'Fisiologia', 'Fisiologia', 1);

INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(4, 'Genetica', 'Genetica', 1);



INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(5, 'Administração Geral e Aplicada', 'Administração Geral e Aplicada', 2);

INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(6, 'Ciência e Gestão da Informação', 'Ciência e Gestão da Informação', 2);

INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(7, 'Contabilidade', 'Contabilidade', 2);

INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(8, 'Economia', 'Economia', 2);


INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(9, 'Estatística', 'Estatística', 3);

INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(10, 'Física', 'Física', 3);

INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(11, 'Informática', 'Informática', 3);

INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(12, 'Matemática', 'Matemática', 3);


INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(13, 'Direito Público', 'Direito Público', 4);

INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(14, 'Direito Civil e Processual Civil', 'Direito Civil e Processual Civil', 4);

INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(15, 'Direito Penal e Processual Penal', 'Direito Penal e Processual Penal', 4);

INSERT INTO escola.curso
(codigo, nome, descricao, cod_depto)
VALUES(16, 'Direito Privado', 'Direito Privado', 4);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(1, 'Sistemática Vegetal', 5, 1010);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(2, 'Morfologia e Fisiologia Vegetal', 5, 1010);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(3, 'Morfologia de Órgãos Reprodutivos', 10, 1010);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(4, 'Sistemática de Criptógamas', 15, 1010);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(5, 'Enzimologia', 15, 1010);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(6, 'Matemática II ', 15, 1020);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(7, 'Física', 15, 1020);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(8, 'Matemática I ', 15, 1020);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(9, 'Direito Constitucional', 45, 1030);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(10, 'Direitos Humanos', 15, 1030);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(11, 'Direito Tributário', 15, 1030);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(12, 'Direito Sanitário', 15, 1030);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(13, 'Matematica Empresarial', 15, 1015);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(14, 'Contabilidade Geral', 15, 1015);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(15, 'Microeconomia', 15, 1015);

INSERT INTO escola.disciplina
(codigo, nome, qtd_creditos, matricula_prof)
VALUES(16, 'Lingua Portuguesa', 15, 1015);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(1, 1);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(1, 2);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(1, 3);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(2, 1);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(2, 4);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(2, 2);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(3, 2);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(3, 4);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(4, 2);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(4, 4);


INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(5, 6);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(5, 7);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(5, 6);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(5, 8);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(6, 8);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(7, 6);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(7, 8);


INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(8, 6);


INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(8, 7);


INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(8, 8);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(9, 7);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(9, 8);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(10, 7);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(10, 6);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(11, 7);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(11, 6);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(12, 7);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(12, 6);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(13, 9);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(13, 10);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(13, 11);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(13, 12);


INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(14, 10);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(14, 11);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(14, 12);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(15, 11);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(15, 12);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(16, 11);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(16, 12);

INSERT INTO escola.curso_disciplinas
(cod_curso, cod_disciplina)
VALUES(16, 16);



INSERT INTO escola.prereq
(cod_cod_disc, cod_cod_disc_depen)
VALUES(2, 1);

INSERT INTO escola.prereq
(cod_cod_disc, cod_cod_disc_depen)
VALUES(3, 1);

INSERT INTO escola.prereq
(cod_cod_disc, cod_cod_disc_depen)
VALUES(3, 2);

INSERT INTO escola.prereq
(cod_cod_disc, cod_cod_disc_depen)
VALUES(4, 1);

INSERT INTO escola.prereq
(cod_cod_disc, cod_cod_disc_depen)
VALUES(4, 3);



INSERT INTO escola.prereq
(cod_cod_disc, cod_cod_disc_depen)
VALUES(5, 4);

INSERT INTO escola.prereq
(cod_cod_disc, cod_cod_disc_depen)
VALUES(5, 3);

INSERT INTO escola.prereq
(cod_cod_disc, cod_cod_disc_depen)
VALUES(6, 8);

INSERT INTO escola.prereq
(cod_cod_disc, cod_cod_disc_depen)
VALUES(7, 8);

INSERT INTO escola.prereq
(cod_cod_disc, cod_cod_disc_depen)
VALUES(9, 10);

INSERT INTO escola.prereq
(cod_cod_disc, cod_cod_disc_depen)
VALUES(11, 10);



INSERT INTO escola.matriculas_curso
(data_matricula, cod_curso, cpf_aluno)
VALUES(CURRENT_TIMESTAMP, 1, '11122244445');


INSERT INTO escola.matriculas_curso
(data_matricula, cod_curso, cpf_aluno)
VALUES(CURRENT_TIMESTAMP, 2, '12345678445');


INSERT INTO escola.matriculas_curso
(data_matricula, cod_curso, cpf_aluno)
VALUES(CURRENT_TIMESTAMP, 3, '12345678911');


INSERT INTO escola.matriculas_curso
(data_matricula, cod_curso, cpf_aluno)
VALUES(CURRENT_TIMESTAMP, 8, '33322244455');


INSERT INTO escola.matriculas_curso
(data_matricula, cod_curso, cpf_aluno)
VALUES(CURRENT_TIMESTAMP, 12, '55544422220');



INSERT INTO escola.matriculas_disciplinas
(data_matricula, cpf_aluno, cod_disc)
VALUES(CURRENT_TIMESTAMP, '11122244445', 1);

INSERT INTO escola.matriculas_disciplinas
(data_matricula, cpf_aluno, cod_disc)
VALUES(CURRENT_TIMESTAMP, '11122244445', 2);

INSERT INTO escola.matriculas_disciplinas
(data_matricula, cpf_aluno, cod_disc)
VALUES(CURRENT_TIMESTAMP, '12345678445', 4);

INSERT INTO escola.matriculas_disciplinas
(data_matricula, cpf_aluno, cod_disc)
VALUES(CURRENT_TIMESTAMP, '12345678911', 4);

INSERT INTO escola.matriculas_disciplinas
(data_matricula, cpf_aluno, cod_disc)
VALUES(CURRENT_TIMESTAMP, '33322244455', 8);

INSERT INTO escola.matriculas_disciplinas
(data_matricula, cpf_aluno, cod_disc)
VALUES(CURRENT_TIMESTAMP, '33322244455', 7);

INSERT INTO escola.matriculas_disciplinas
(data_matricula, cpf_aluno, cod_disc)
VALUES(CURRENT_TIMESTAMP, '55544422220', 7);

INSERT INTO escola.matriculas_disciplinas
(data_matricula, cpf_aluno, cod_disc)
VALUES(CURRENT_TIMESTAMP, '55544422220', 6);

