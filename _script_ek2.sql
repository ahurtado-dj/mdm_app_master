BEGIN;
--
-- Create model Persona
--
CREATE TABLE "ek2_persona" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "tipo_persona" varchar(1) NOT NULL, "tipo_identificacion" varchar(2) NOT NULL, "identificacion" varchar(64) NOT NULL, "nombres" varchar(255) NOT NULL, "apellidos" varchar(255) NULL, "fecha_nacimiento" date NULL, "celular" varchar(20) NULL, "email_personal" varchar(20) NULL);

COMMIT;
