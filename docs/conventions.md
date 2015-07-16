# Stek code conventions

Prevent fights, do as we do (when it comes to arbitrary style decisions...):

## Codestyle

- class names are CamelCase and capitalized: `ProfielSerializer`
- function names are snake case and lowercase: `get_profiel_serializer()`
- properties are snake case and lowercase: `profiel_serializer_attr`
- tabsize is 2 spaces (insert spaces not tab characters)

## Django

- Whatever the name of a primary key on a model, django will always create an alias on the model
  called `pk` that refers to it. Use this in the `serializers` so we get a consistent naming
  of primary keys in the api.
  Related keys are accessible on a django model by the `<relation>_id` field and should be named
  accordingly in the serializer (e.g. `user_id`, `forum_id` for the user and forum related objects
  respectively)

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
