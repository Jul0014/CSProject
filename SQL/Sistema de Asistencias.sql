CREATE TABLE "personas" (
	"dni" varchar(8) PRIMARY KEY,
	"nombres" varchar(60) not null,
	"apellido_paterno" varchar(30) not null,
	"apellido_materno" varchar(30) not null,
	"fecha_nacimiento" date not null,
	"correo_institucional" varchar(100) not null,
	"password" varchar(15) not null
);

CREATE TABLE "profesores" ( --10 personas
	"dni" varchar(8) PRIMARY KEY,
	"especialidad" varchar(100)
);

CREATE TABLE "alumnos" (
	"dni" varchar(8) PRIMARY key
);

CREATE TABLE "administradores" ( --10 personas
	"dni" varchar(8) PRIMARY KEY
);

CREATE TABLE "asignaturas" (
	"codigo" integer PRIMARY key generated by default as identity 
	(start with 1 increment by 1),
	"nombre" varchar(60) not null,
	"semestre" integer,
	"carrera" varchar(60)
);

CREATE TABLE "horarios" (
	"codigo" integer PRIMARY KEY generated by default as identity 
	(start with 1 increment by 1),
	"hora_inicio" time not null,
	"hora_fin" time not null,
	"dia" varchar(2) not null
); 

CREATE TABLE "salones" (
	"codigo" integer PRIMARY KEY generated by default as identity 
	(start with 100 increment by 1),
	"pabellon" char not null,
	"numero" integer not null
);

create table "cursos"(
	"codigo" integer primary KEY generated by default as identity 
	(start with 1 increment by 1),
	"asignatura" integer not null,
	"profesor" varchar(8) not null,
	"horario" integer not null
);

create table "dictados"(
	"codigo" integer primary KEY generated by default as identity 
	(start with 1 increment by 1),
	"curso" integer not null,
	"salon" integer not null,
	"tema" varchar(200) 
);

CREATE TABLE "matriculas" (
	"codigo" integer PRIMARY KEY generated by default as identity 
	(start with 1 increment by 1),
	"alumno" varchar(8) not null,
	"curso" integer not null,
	"estado" integer not null
);

CREATE TABLE "asistencias" (
	"codigo" integer primary KEY generated by default as identity 
	(start with 1 increment by 1),
	"estado" boolean not null,
	"fecha_asistencia" timestamp not null,
	"matricula" integer not null
);

create table "justificaciones" (
	"codigo" integer PRIMARY KEY generated by default as identity 
	(start with 1 increment by 1),
	"asistencia" integer not null,
	"titulo" varchar(100),
	"descripción" varchar(500) not null,
	"archivo" BYTEA
);

CREATE TABLE "participaciones" (
	"asistencia" integer not null,
	"cantidad" integer
);

ALTER TABLE "profesores" ADD FOREIGN KEY ("dni") REFERENCES "personas" ("dni");

ALTER TABLE "alumnos" ADD FOREIGN KEY ("dni") REFERENCES "personas" ("dni");

ALTER TABLE "administradores" ADD FOREIGN KEY ("dni") REFERENCES "personas" ("dni");

ALTER TABLE "justificaciones" ADD FOREIGN KEY ("asistencia") REFERENCES "asistencias" ("codigo");

ALTER TABLE "matriculas" ADD FOREIGN KEY ("alumno") REFERENCES "alumnos" ("dni");

ALTER TABLE "matriculas" ADD FOREIGN KEY ("curso") REFERENCES "cursos" ("codigo");

ALTER TABLE "dictados" ADD FOREIGN KEY ("curso") REFERENCES "cursos" ("codigo");

ALTER TABLE "dictados" ADD FOREIGN KEY ("salon") REFERENCES "salones" ("codigo");

ALTER TABLE "participaciones" ADD FOREIGN KEY ("asistencia") REFERENCES "asistencias" ("codigo");

ALTER TABLE "cursos" ADD FOREIGN KEY ("asignatura") REFERENCES "asignaturas" ("codigo");

ALTER TABLE "cursos" ADD FOREIGN KEY ("profesor") REFERENCES "profesores" ("dni");

ALTER TABLE "cursos" ADD FOREIGN KEY ("horario") REFERENCES "horarios" ("codigo");

ALTER TABLE "asistencias" ADD FOREIGN KEY ("matricula") REFERENCES "matriculas" ("codigo");