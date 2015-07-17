# Django

This describes the largest and most important part of the stek server side.

## Processing a typical request

Let's follow the path of a http request that knocks on Django's methaphorical door:

1) **knock knock**
2) **Middleware**: this is a stack of processors that modify the request.
   This varies from parsing the HTTP request to getting the session data from storage and
   anything else that you want to happen for any request (which middleware is enabled is configured
   in `settings.py`).
   Usually you don't deal with the middleware directly.
3) **Router**: this is the thing that decides which requests goes where from now on.
   You can find the configured routes in `urls.py` (possibly including other url configs).
   It's mostly a matter of pattern matching on the request url and forwarding the request to the
   specified handler.
4) **Request handler** (or view function): the actual handler might be generated or handled
   by some class, but in the end the handler is just a function tied to an URL.
   It reads some data from the request object, executes a bunch of queries and then renders a
   response. A response can be html (rendered using Django's template system) or JSON, or ...
5) **Middleware**: Yes! Again! Middleware is two-directional, so any response will be passed back
   through the middleware stack in reverse order.
6) **Client**


### Code organization

Django projects are split vertically into apps. Each app has it's own models, views and such.
Ofcourse apps can import code from other app (although it's good to keep these dependencies linear).
The 'enabled' apps for a running site are configured in `settings.py`.
This list includes for example the django `auth` and `admin` apps, but also the `forum` and
`maaltijden` apps.

The files in these app modules should speak for themselves: `models.py`, `api.py`/`views.py`, etc.

## Database

The database is an integral part of every Django app.
The structure is declared by the Django models.
But the models are also your accesspoint to writing queries.
Djang querysets are extremely powerful, mostly because relationships are so easily traversible.
Keep in mind though that everytime you access a field that represents a related object, django
is querying the database in the background!

Interesting material on models and querying that I recommend are here [model
reference](https://docs.djangoproject.com/en/1.8/topics/db/models/).
Pay special attention to:

- "Lookups that span relationships"
- "Querysets are lazy"
- "Related objects" (especially the 'reverse relationships')

I cannot stress enough that **this** is the important part to learn.
There is an awesome library at your fingertips, but you have to read-up to find the best bits.

Changes in the model reflect changes in the database structure, so the two are coupled via
**migrations**.
Everytime you have a set of coherent changes to your model you can generate a migration that will
update the database structure.
Think of them as "git commits" for your database.
Ideally migrations are fully revertible, but this is not always the case.

The Django docs on **migrations** are [here](https://docs.djangoproject.com/en/1.8/topics/migrations/).

## More reading

Django has excellent documentation that can be accessed from
[here](https://www.djangoproject.com/start/).
I highly recommend that you follow the django tutorial which will touch upon every important part.
If you're in a hurry you can read and then lookup the corresponding parts in the stek code, instead
of writing your own tutorial project code. It 'll give you a feel for what's there.

The Django docs on **migrations** are [here](https://docs.djangoproject.com/en/1.8/topics/migrations/).

# Specific Django Topics

### Permissions management

The stek has a complicated permission system.
We roughly divide the options in 3 categories (in increasing order of nastiness):

1) *static permissions*: a user gets permission because it was directly assigned to him
   or because he is in a (django-auth-framework-) group that has the permission assigned to it.
2) *dynamic permissions*: a user gets permissions because it has some kind of property
   (e.g. member of a commissie/verticale)
3) *object specific permissions*: a user gets permission based on an object property

We prefer static permissions wherever possible, because we can check them efficiently
(static lookup) and we can manage them easily (django admin, assign/delete permissions).

Static permissions are not always an option because the could result in a high level of required
maintainance. Imagine for example if we'd want to give permission based on kring-membership.
We'd have to create django auth groups for every kring every year and keep track of who's in what
kring.
In those cases we can use a `django-permission` permission logic (third party package we use).
A bunch of them are defined in [here](https://github.com/csrdelft/balins-adventure/blob/master/src/base/perms.py).

Sometimes we actually have permissions that are specific to the target object.
For example: whether a user has access to a forum part depends not only on user properties
but also on the properties of the forum part.
Sometimes this can be molded into one of the above forms (which should be preferred), but sometimes
it's just a necessary evil.
For these permissions we also use `django-permission`.

#### Efficiency

The first 2 categories of permissions are efficient in the sense that I can determine whether
a user has permission with either a simple lookup or a lookup + some logic.
The object specific permission is much less efficient because I first need an instance of the object
before I can determine whether the user has permission.
If the target is a single object, this is not really problematic, but it does not scale
if I want to retrieve a list of objects that the user has permission on, because I'd first have
to get **all** objects and then filter them in the server; and there might be a lot of them...

#### Making things more efficient

We prefer **declarative** permissions in `perms.py`, but as mentioned, object specific permissions
can be inefficient in it's usage.
This is mostly because in general the object specific permission logic is executed in python, and
cannot be translated to an SQL query that does the filtering.
However, sometimes you can actually manually create a queryset to represent the objects that a user
has permission on.
If this is the case you'll find these querysets on the model under names such as `get_viewable_by(user)`.
These functions should return a django QuerySet such that they can be used in the `get_queryset`
methods of the api viewsets.
