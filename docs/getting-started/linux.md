# Unix, getting started

1. Use your package manager to install `python`, `node`, `mysql` and `redis`
2. Clone this repository
3. Open a terminal at the root of the repository
4. Run the following commands to create the python and node sandboxes and install the local
   dependencies.

    make install
	  source .virtualenv/bin/activate
	  pip install -r requirements

5. Install gulp globally using npm: `sudo npm install -g gulp`

6. Run the build for the client side files `gulp`

7. Setup a database:

    mysql -u root -p -e "create database csrdelft_django; grant all privileges on csrdelft_django.* to csrdelft@localhost identified by 'bl44t';"

8.  You can now migrate the database (make sure the virtualenv is activated as before) and
    run the development server; from the `src/` run:

    python manage.py migrate
	  python manage.py runserver

9.  You should now be able to visit `localhost:8000` (and `localhost:8000/admin/`) in your browser
    (might get an error on browsing because the notifications server isn't running yet).

To use the push notifications, you also need to start redis and the node notifications server:

10. Start the redis deamon (depends on your distribution: google if unsure)

11. Open `src/notifications` and run `npm install`, followed by `npm start`

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

## Running tests

`make test` doh

## IDE

The windows getting-started guide explains how to set up PyCharm
