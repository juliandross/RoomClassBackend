DROP DATABASE IF EXISTS RoomClassDB;
CREATE DATABASE RoomClassDB CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE RoomClassDB;
-- Inserta Periodos
INSERT INTO academApi_period (perSemester) VALUES ('2024-1');
INSERT INTO academApi_period (perSemester) VALUES ('2024-2');

-- Inserta Subjects
INSERT INTO academApi_subject (subjectName, subjectDescription, subjectCredits, subjectSemester, is_active)
VALUES ('Matemáticas', 'Matemáticas básicas', 6, 1, TRUE);

INSERT INTO academApi_subject (subjectName, subjectDescription, subjectCredits, subjectSemester, is_active)
VALUES ('Física', 'Física general', 5, 1, TRUE);

-- Inserta un usuario en user_user (debes tener esta tabla creada por el modelo User)
INSERT INTO user_user (email, first_name, last_name, is_active, is_staff, rol, password, is_superuser)
VALUES ('profesor1@ejemplo.com', 'Ana', 'García', TRUE, FALSE, 'DOCENTE', '1234', FALSE);

INSERT INTO user_user (email, first_name, last_name, is_active, is_staff, rol, password,is_superuser )
VALUES ('profesor2@ejemplo.com', 'Luis', 'Martínez', TRUE, FALSE, 'DOCENTE', '1234', FALSE);

-- Inserta Teachers (hereda de user_user)
INSERT INTO academApi_teacher (user_ptr_id, teaType, teaTypeId, teaRecentTitle)
VALUES (1, 'Titular', 'T001', 'Doctorado en Matemáticas');

INSERT INTO academApi_teacher (user_ptr_id, teaType, teaTypeId, teaRecentTitle)
VALUES (2, 'Asociado', 'T002', 'Maestría en Física');

-- Inserta SubjectTeacherPeriod
INSERT INTO academApi_subjectteacherperiod (subject_id, teacher_id, period_id)
VALUES (1, 1, 1);

INSERT INTO academApi_subjectteacherperiod (subject_id, teacher_id, period_id)
VALUES (2, 2, 2);