CREATE TABLE IF NOT EXISTS `Sala_de_aula` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`alunos` int AUTO_INCREMENT NOT NULL DEFAULT '30',
	`professores` int AUTO_INCREMENT NOT NULL DEFAULT '15',
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `Aluno` (
	`id` int AUTO_INCREMENT NULL,
	`nome` varchar(255) NULL DEFAULT '5',
	`idade` int  NULL,
	`turma` varchar(100)  NULL,
	`nota_media` decimal(10,0)  NULL,
	`cidade` varchar(100)  NULL,
	PRIMARY KEY (`id`)
);

CREATE TABLE IF NOT EXISTS `professor` (
	`id` int AUTO_INCREMENT NOT NULL UNIQUE,
	`nome` char(5) NOT NULL,
	`turma` varchar(255) NOT NULL DEFAULT '3',
	PRIMARY KEY (`id`)
);

ALTER TABLE `Sala_de_aula` ADD CONSTRAINT `Sala_de_aula_fk2` FOREIGN KEY (`professores`) REFERENCES `professor`(`id`);
ALTER TABLE `Aluno` ADD CONSTRAINT `Aluno_fk0` FOREIGN KEY (`id`) REFERENCES `Sala_de_aula`(`id`);
