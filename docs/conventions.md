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
