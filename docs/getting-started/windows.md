# Windooooows, getting started

1. Install **Python 3** (including pip) from the python site
2. Install **NodeJS** (including npm)
3. Clone this repository
4. Open Powershell at the root of the repository
5. Run the following commands to create the python sandbox and install the python dependencies
   as described by the file `requirements`:

    python -m venv .virtualenv
	  .virtualenv\Scripts\activate.ps
	  python -m pip install -r requirements

6. Run the following commands to install the node sandbox with the dependencies as described by the
   `package.json`:

	  npm install
	  npm install -g gulp

7. Run the build for the client side files

    gulp

8. Download and install MySQL

9. Setup a database by executing the following query (e.g. in the workbench):

    create database csrdelft_django; grant all privileges on csrdelft_django.* to csrdelft@localhost identified by 'bl44t';

10. Download and install PyCharm (pro edition, using your TU e-mail account):

11. Configure pycharm. When you open the project it should pick up the virtual python env that we
   created. You should verify this at `Run > Edit Configurations > Python Interpreter`.
   In `Settings > Language and Frameworks > Django` you should set the django root to `src`
   and the settings file to `src/csrdelft/settings.py`.

12. You can now run django tasks `Tools > Run manage.py Task`. Execute the following in the prompt
    that opens:

    migrate
	  runserver

13. You should now be able to visit `localhost:8000` (and `localhost:8000/admin/`) in your browser
    (might get an error on browsing because the notifications server isn't running yet).

To use the push notifications, you also need:

14. Install Redis

15. Open `src/notifications` and run `npm install`, followed by `npm start`.

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
