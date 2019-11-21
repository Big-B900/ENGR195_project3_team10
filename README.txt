



to install required packages (I think, if not look at error messages)

SETUP:
Recommended: make virtual env
to make a virtualenv
$virtualenv env

activate virtualenv:
$source env/bin/activate

install packages
$pip install tensorflow==1.15
$pip install SimpleCV

//updates
$pip install fabric

in .../env/lib/python3.6/site-packages/paramiko/client.py
add in a line before line 628:

	password = 'engr195'






EACH TIME YOU RUN:
navigate to ~/project 3:
$cd project3

activate virtualenv:
$source env/bin/activate

run code here
$...

deactivate virtualenv
$deactivate

SECTION FOR WORKING WITH FABRIC
to run code with fabric on other device, go to the folder with fabfile.py
make sure to be connected to the other device

run
$fab --prompt-for-login-password <function>
where function is the name of the function to run on the other device

example
$fab --prompt-for-login-password update

//update for hardcoded passwords

use:
$fab function
ex: 
$fab update




credits for the classifier: 

Daniel Lawson: https://github.com/daniellawson9999/Trash-App-Classifier
Alwin Yen: https://github.com/alwinyen/trashapp-pi
