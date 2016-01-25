=============================================
MDM-DATA
=============================================
reprsenta los nodos origen y destino de la 
sincronizacion (mdm-master-data:ek2, mdm-slave1-data:ek1)


=============================================
INFORMACION TECNICA - SCAFFOLD
=============================================
- se trata de una app en django que escribe a sqlite
- dscargar python 2.7
- instalar virtualenv
- crear virtualenv dj19
	cd c:\.work\virtualenv
	virtualenv dj19
	cd C:\.apps\e_aj.Apps\.ws\ARQ\trunk\02_Proyectos\0028_Aj_Baseline_Ciclo01\03_construccion\mdm_base
	C:\.work\virtualenv\dj19\Scripts\activate
- scaffold
	pip install django==1.9
	django-admin startproject _app
	renombrar a mdm_app_master
	python manage.py startapp ek2
	python manage.py startapp ek1
	python manage.py makemigrations

- geneerar scripts
	python manage.py sqlmigrate ek1 0001 > _script_ek1.sql
	python manage.py sqlmigrate ek2 0001 > _script_ek2.sql

	

=============================================
INFORMACION TECNICA - EJECUCION 
=============================================
- instalar prerrequisitos
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py createsuperuser (
		-> name: admin
		-> mail: ahurtado.dj@gmail.com
		-> pwd: meconio3

- subir aplicaciones

De momento se tiene configurado que
la misma aplicacion se duplique y emule los nodos origen y destino, por lo cual 
debe sacar una copia del proyecto del tal forma que queden 2 directorios así:

	+----------------+---------+---------+
	|   aplicacion   | emula-a | puerto  |
	+----------------+---------+---------+
	| mdm_app_master |   ek2   |  8000   |
	| mdm_app_slave1 |   ek1   |  8001   |
	+----------------+---------+---------+

para ello
cd C:\.apps\e_aj.Apps\.ws\ARQ\trunk\02_Proyectos\0028_Aj_Baseline_Ciclo01\03_construccion\mdm_base
copy mdm_app_master mdm_app_slave1
	
- luego subir las aplicaciones

subir master: 	
	ejecutar los pasos indicados en el archivo readme del proyecto mdm_server_symmetricds, relativos a la configuracion de master

	cd mdm_app_master
	python manage.py runserver 0.0.0.0:8000
	cd ..

subir slave1: 	
	ejecutar los pasos indicados en el archivo readme del proyecto mdm_server_symmetricds, relativos a la configuracion de slave1

	cd mdm_app_slave1
	python manage.py runserver 0.0.0.0:8001
	cd ..

subir sincronizacion
	ejecutar los pasos indicados en el archivo readme del proyecto mdm_server_symmetricds, relativos a subir el sincronizador
	
=============================================
INFORMACION TECNICA - ADMINISTRACION
=============================================
	para poder administrar las estructuras existentes en el modelo
	master (actualmente, una db en sqlite, hsql o access)

	- descargar editor: 	
		sqlitebrowser http://sqlitebrowser.org/ (* recomendado)
		
		
	si ya se ha ejecutado symmetricds por primera vez, se peuden observar
	las estructuras de sincronizacion (tablas con prefijo sym_)
	
	NOTA: luego de instalados y estar ejecutando estos proyectos, ejecutar las actividades
	referenciadas en la aplicacion symmetric_ds
	
	
=============================================
Modelo Destino
=============================================




=============================================
Otros (no probado): 
=============================================

- si se pasa a una db en h2 (que emula la estructura de ekogui):
	- descargar la version h2 multiplataforma	
	- descomprimir en 
		C:\.work\h2-2015-10-11	
		cd C:\.work\h2-2015-10-11
		bin\h2.bat		(inicia la consola)
		
		luego acceder a http://192.168.40.193:8082/  (usuario sa/sa)
	
- correr sqlite standalone
	sqlite: 
	- descargar de sqlite
		-> sqliteshell + sqlitedll_x64
		-> descomprimir en C:\.work\sqlite3-3090200
		-> iniciar sqlite3.exe desde comandos
- otro browser sqlite
	sqlite-manager: https://dibosa.wordpress.com/dossier/administracion-grafica-de-sqlite-con-sqlite-manager/
