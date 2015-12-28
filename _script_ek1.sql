BEGIN;
--
-- Create model Tercero
--
CREATE TABLE "ek1_tercero" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "ter_tipo" varchar(1) NOT NULL, "ter_tipodoc" varchar(2) NOT NULL, "ter_ident" varchar(64) NOT NULL, "ter_nom" varchar(255) NOT NULL, "ter_ap1" varchar(255) NULL, "ter_ap2" varchar(255) NULL, "ter_telefono" varchar(20) NULL, "ter_email" varchar(20) NULL, "x_sync_corr1" varchar(255) NULL);

COMMIT;
