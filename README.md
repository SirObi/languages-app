# languages-app
Flask app for sharing your passion for languages with others

## Prerequisites

Language: this app is written in Python 2.

Required modules:  
`pip install Flask`  
`pip install SQLAlchemy`

 In order to run the app, you'll need to install a Linux-based virtual machine (VM).
 This will provide you with the necessary environment.  
 
 ## Install the virtual machine  
 1. First, download and install Virtual Box: https://www.virtualbox.org/wiki/Downloads  
 2. Then, download and install Vagrant: https://www.vagrantup.com/downloads.html  
 3. Finally, select a folder on your PC from which you'd like to run the app.  
 4. Fork and clone the following repository into the folder you've just selected:   https://github.com/udacity/fullstack-nanodegree-vm  
 5. Navigate to the repository you've just created and cd to the subdirectory called "vagrant".  
 6. At this step, fork and clone the repository containing this README file into the "vagrant" directory.  
 7. From the terminal, run ```vagrant up```.  
 The virtual machine is now being installed - it may take a while.


## Set up database
1. Set up the SQLite database:
`python database_setup.py`  
2. Run the following script to populate the database:
`python populate_database.py`  

## Obtain Client ID and secret from Google APIs Console 
This app uses third-party authentication and authorization (OAuth) provided by Google.  
Therefore, you need to register the app with Google first:  
1. Set up a new project for the app at https://console.developers.google.com.  
2. Go to the app's page in the Google APIs Console — https://console.developers.google.com/apis  
3. Choose Credentials from the menu on the left.  
4. Create an OAuth Client ID.  
5. This will require you to configure the consent screen..  
6. When you're presented with a list of application types, choose Web application.  
7. You can then set the authorized JavaScript origins (f.x. to http://localhost:5000) 
8. You will then be able to download a JSON file containing your client ID and client secret.  
9. Change the name of the file to `client_secrets.json` and place it in the directory  
which contains the `languages.py` file.  

## Start up vagrant and run the app  
If you haven't already done so, cd to the directory /fullstack-nanodegree-vm and then run:  
`vagrant up`  
`vagrant ssh`  
`cd /vagrant`  

cd to the directory which contains `languages.py`.  
`python languages.py`  

Open up your browser and go to the following URL:  
`http://localhost:5000`

