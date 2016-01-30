# Windooooows, getting started

### First Time Stuff

1. Install **Python 3.4** (including pip) from the [python site](https://www.python.org/downloads/release/python-343/) and make sure it's on your PATH by adding "C:/Python34/" to your PATH environmental variable or checking the option in the installation wizard.
2. Install **NodeJS** (including npm) from [here](https://nodejs.org/en/download/)
3. Clone this repository
4. Open a Powershell as administrator and run the following to allow running powershell scripts `Set-ExecutionPolicy RemoteSigned`
4. Open a Powershell as a regular user at the root of the repository
5. Run the following commands to create the python sandbox and install the python dependencies
   as described by the file `requirements`:

```
python -m venv .virtualenv
.virtualenv\Scripts\activate.ps1
python -m pip install -r requirements
```

6. Run the following commands to install the node sandbox with the dependencies as described by the
   `package.json`:

```
npm install
npm install -g gulp
```

7. Download and install MySQL [from here](http://dev.mysql.com/downloads/windows/installer/5.7.html). Install the server, the python connector and the workbench.

8. Setup a database by executing the following query (e.g. in the workbench):

   ```
    create database csrdelft_django; grant all privileges on csrdelft_django.* to csrdelft@localhost identified by 'bl44t';
   ```
   
9. Download and install PyCharm (pro edition, using your TU e-mail account):

10. Configure pycharm. When you open the project it should pick up the virtual python env that we
   created. You should verify this at `Run > Edit Configurations > Python Interpreter`.
   In `Settings > Language and Frameworks > Django` you should set the django root to `src`
   and the settings file to `src/csrdelft/settings.py`.

## The Python Venv

All python dependencies and tools are LOCAL to the project.
This way we never clash with other python packages on your system.
You do have to remember to *activate* the virtual python environment everytime you run a python command (e.g. pip) for the project.

   ```
    python -m venv .virtualenv
   ```

The environment is active until you close the shell.

## Updating the project

Changes in the `package.json` indicate that node dependencies have changed. You can install the new/updated deps with npm `npm install` from the reposistory root.

Changes in the `requirements` indiciate that the python dependencies have changed. Update with `python -m pip install -r requirements`. Note that for all python commands, you first have to activate the python virtual environment.

## Usual Build Steps 

- Run the build for the client side files

   ```
    gulp
   ```

  This will start watching for changes and rebuild automatically when it detects a file change.
  
- You can run django commands using the `manage.py` python script in `src`. Usually you want to start the development server:

   ```
    python manage.py runserver
   ```

  You should now be able to visit `localhost:8000` (and `localhost:8000/admin/`) in your browser.


## Push Notifications

1. Install Redis

2. Open `src/notifications` and run `npm install`, followed by `npm start`.

## Post installation

You should create a Django user to be able to login at the admin panel (the following commands are
all manage.py commands):

    createsuperuser

The app also assumes that *every* django user has a C.S.R. user profile associated with it.
We can link these using the Django models if we open a python shell:

    shell_plus
    > (... imports automatically)
    > p = Profiel.objects.get(uid='<your-uid>')
    > u = User.objects.get(username='<the super user name you just created>')
    > p.user = u
    > p.save()
    > exit()

The above is valid python and uses the Django models to execute 2 SELECT and an UPDATE sql-query.

Now you can login and browse around.

## Some run options

To speed up the test runs you should edit your default test run configuration in
`Run > Edit Configurations > Defaults > Django tests` and set `Options: --keepdb`.

You can also add a run configuration for the Django development server such that you can easily
start it (press `+`, choose *Django Server* and click apply).

## More handy plugins for Intellij

- CSS Support
- Git Integration
- HTML Tools
- NodeJS
- IdeaVim (yeah!)
