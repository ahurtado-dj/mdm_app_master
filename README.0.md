=============================================
MDM-DATA
=============================================
reprsenta los nodos origen y destino de la 
sincronizacion (mdm-master-data:ek2, mdm-slave1-data:ek1)


- una app en django que escribe a sqlite
- dscargar python 2.7
- instalar virtualenv
- crear virtualvn dj19
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

- instalar
	pip install -r requirements.txt
	python manage.py migrate
	python manage.py createsuperuser (
		-> name: admin
		-> mail: ahurtado-dj@gmail.com
		-> pwd: meconio3
	python manage.py runserver
	

=============================================
subir aplicaciones
=============================================
La misma aplicacion se sube como master y como slave1

saque una copia del proyecto del tal forma que queden:
	(mdm_app_master)
	(mdm_app_slave1)

cd C:\.apps\e_aj.Apps\.ws\ARQ\trunk\02_Proyectos\0028_Aj_Baseline_Ciclo01\03_construccion\mdm_base

subir master: 	

cd mdm_app_master
python manage.py runserver 0.0.0.0:8000
cd ..

subir slave1: 	

cd mdm_app_slave1
python manage.py runserver 0.0.0.0:8001
cd ..



	
	
	
	
	


=============================================
Modelo Origen
=============================================
- una db en sqlite, hsql o en access

	sqlite: 
	- descargar de sqlite
		-> sqliteshell + sqlitedll_x64
		-> descomprimir en C:\.work\sqlite3-3090200
		-> iniciar sqlite3.exe desde comandos
		
	- descargar editor: 	
		sqlitebrowser http://sqlitebrowser.org/
		sqlite-manager: https://dibosa.wordpress.com/dossier/administracion-grafica-de-sqlite-con-sqlite-manager/
	
=============================================
Modelo Destino
=============================================

- de momento se tiene configurado en otto modulo de la misma app (ek1)

- si se pasa a una db en h2 (que emula la estructura de ekogui):
	
- descargar la version h2 multiplataforma	
- descomprimir en 
	C:\.work\h2-2015-10-11
	
	cd C:\.work\h2-2015-10-11
	bin\h2.bat		(inicia la consola)
	
	luego acceder a http://192.168.40.193:8082/  (usuario sa/sa)
	