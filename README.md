 
# Django Test WebApp

Current Tool was developed as part of the Djangos learning process. Current Package was developed on the basis of the following Task: 

### Usecase:
	Es soll eine Softwarelösung erstellt werden, die Kontakte eines Teams verwaltet.

### Datenbankmodell:
    Mandatory:
		Attribute: Vorname, Nachname, Mailadresse
	Optional:
		weitere sinnvolle Attribute/Entitäten definieren und ein kleines Datenbankmodell modellieren
### Webapplikation
	Dazu ist eine Webapplikation erstellen:
        Einstiegsseite:
                       Übersicht bisher angelegter Kontakte (readonly)
                       Auswählen eines Datensatzes und Weiterleitung zur Detailseite
        Detailseite zum Datensatz:
                       Anlegen
                       Bearbeiten
                       Löschen
        Optional:
                       Validierung auf sinnvolle Mailadresse
        Abgrenzung:
                       keine Login-Funktion im ersten Schritt nötig
### REST-Schnittstelle
	Lesend:
		Liste von allen Kontakten ausgeben
	einen bestimmten Kontakt ausgeben
	Optional:
		Kontakt über REST-Schnittstelle schreiben

### UNIT-Tests (ausgewählte Bsp.):
	für Detailseiten der Webseite
	für das Schreiben in REST-Schnittstelle Technologie:
        Multitier Architektur
        Die Datenbank ist frei wählbar
        ein Teil der Umsetzung soll pythonbasiert erfolgen
        setzen Sie bitte sinnvoll Komponenten/Frameworks ihrer Wahl ein
        denken Sie an Logging und Fehlerbehandlung


___





---



___


<br/>
<br/>


<a name="toc"/>

## Table of Contents

1. [Dependencies Installation](#dependencies)

2. [Setting up](#settingup)


3. [Tutorials](#tutorials)
   -  Web Platform
   -  REST API
   -  Unit Tests

4. [Demarcation](#demarcation) 



<br/>



---
---
---
---

<br/>



<a name="dependencies"/>
<p style='text-align: right;'>  <sub> <a href="#toc">Back to top</a>
</sub> </p>

## 1. Dependencies


In order to run and to test current WebbApp you'll need the following installed Dependencies in addition to the source code:

* [Python 3.6.5 or later](https://www.python.org/download/releases>)
* [VirtualEnv](https://virtualenv.pypa.io/en/latest/)
* [Git](https://git-scm.com/download/mac)

*** all other dependencies would be installed automaticly durring the installation process of the current package



#### Dependencies Installation 
following installation commands should be seeing as just an idea how and could become incorrect with time. Important is, that all above listed Dependencies are installed, before you can start to SetUp the Tool. 

<sub>*$ - symbol ensure the begin of the command, which should be copy-pasted into the terminal window.*</sub>

##### On Linux (UbuntuOS 16.04.5 LTS)
0. open Terminal/Bash/Shell

1. Add other repositories

        $ sudo add-apt-repository ppa:jonathonf/python-3.6


2. Upgrade default linux tools

        $ sudo apt-get update
        $ sudo apt-get upgrade

3. Install additional SW

        $ sudo apt-get install python-setuptools python-dev  build-essential autoconf  pkg-config  git python-dev

4. Python Installation

        $ sudo apt install python3.6 python3-pip 
        $ sudo -H pip3 install --upgrade pip setuptools
        $ alias python=python3.6
        $ alias pip=pip3


5. VirtualEnv

        $ sudo -H python -m pip install virtualenv



<br/>

##### On Windows (Win10)
  (this tool could be invoked just up from the Windows10 Version)


    1. Microsoft Visual C++ Compiler for Python 2.7
       (https://www.microsoft.com/en-us/download/details.aspx?id=44266)
    2. Enable in Features - "Windows Subsystem for Linux"
        (https://docs.microsoft.com/en-us/windows/wsl/install-win10)
    3. Enable in Settings - "Developer Mode"
        (https://www.wikihow.com/Enable-Developer-Mode-in-Windows-10)
    4. Install Ubuntu 16.04 from the Windows Store
        (https://devtidbits.com/2017/11/09/ubuntu-linux-on-windows-10-how-to/)
    5. goes to Ubuntu Bash 
    6. goes now above to the part with instructions for Linux
    *** root path to Ubuntu Directory on Windows: C:\Users\<username>\AppData\Local\Packages\CanonicalGroupLimited.UbuntuonWindows_79rhkp1fndgsc\LocalState\rootfs\home




<br/>

##### On macOS (10.13.6)
0. open Terminal
1. Install brew

        $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

2. Install Python


        $ brew install python3
        $ sudo python3 -m ensurepip

        $ pip3 install --upgrade pip setuptools wheel
        $ alias pip=pip3
        $ alias python=python



    
3.  VirtualEnv

            $ sudo -H python -m pip install virtualenv
            



<br/>



---
---
---
---

<br/>

<a name="settingup"/>
<p style='text-align: right;'>  <sub> <a href="#toc">Back to top</a>
</sub> </p>

## 2. Setting up

<sub>*Set background color of your terminal to dark (ex. black, dark blue etc.)*</sub>


##### 1. Package Installation 
goes to the directory, where you want to locate current package (for example:)

    $ open Terminal
    $ cd  ~/Desktop
    $ mkdir django_test
    $ cd django_test
    $ virtualenv -p /usr/local/bin/python3 env
    $ git clone https://github.com/savin-berlin/test_webapp.git
    $ . env/bin/activate
    $ pip install -e .


##### 2. Run Django Server  

goes to the directory, where "manage.py" is located

	$ cd test_webapp/root_app

run Server

	$ python manage.py runserver 


##### 3. Configuration

superuser credentials:

	Username: admin
	PW: qohpUp-1wibqe-dukjir

 - Admin Site: http://127.0.0.1:8000/admin/
 - Main Page: http://127.0.0.1:8000/
 - Contacts Overview: http://127.0.0.1:8000/contacts/


##### 3. REST API


###### 4. UNIT-Tester





<br/>



---
---
---
---

<br/>



<a name="tutorials"/>
<p style='text-align: right;'>  <sub> <a href="#toc">Back to top</a>
</sub> </p>

## 3. Tutorials

### Web Platform


### REST API


### Unit Tests




<br/>



---
---
---
---

<br/>



<a name="demarcation"/>
<p style='text-align: right;'>  <sub> <a href="#toc">Back to top</a>
</sub> </p>

## 4. Demarcation


1. Web Platform 
	On the "Contacts Overview!"-Page (http://127.0.0.1:8000/contacts/) in the "Actions" area the "Delete"-Button was implemented as unsecure "GET-Request" without csrf_token  but at the Contact-Edit-Page (http://127.0.0.1:8000/contact/edit-contact) the same Button was implemented as "POST-Request" with csrf_token. 

2. Extern DataBase (SQLite)
	Please ignore current path and all with them connected methods and functions 
	"root_app/team_manager/db". This was done just for learning goals and currently not in the active deployment. 
	

