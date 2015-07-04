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

