# Writing Django services

So in chapter 2 we took an overview of Django and it's parts.
Let's zoom in on the part that you'll be working on most of the time (hopefully): *writing services*.

I'm not going to go through it in steps with all the code here, because there is plenty of that in
the [Django docs](https://docs.djangoproject.com/en/1.8/topics/http/views/). But we can take a close
look at writing typical stek services.

## Rest API

Because we want to work towards a one page application where the client does most of the heavy work
of rendering data into HTML, our services are mostly JSON services.

It's easy enough to write a function that implements a rest service in django: we just need
a function that takes a request object and returns a `HttpResponse` that contains some json.
Typically this looks like:

    # the service
    def get_something(request):
      # query the data
      somethings = Something.objects.all()

      # map the dasta to json
      json = some_function_that_convert_to_json(somethings)

      return HttpResponse(json)

    # the url binding
    urls = ('', url('sometings/', get_something))

The part that needs most codelines here is mostly serializing the "somethings", because I have to
convert a possibly complex datastructure into a json object.
(And the reverse is even more work: parsing a jsong structure, validating it and creating an
instance, e.g. from posting form data).

BUT, since a lot of information is known about our objects (models...) we can actually automate
most of this!
In comes [Django Rest Framework](http://www.django-rest-framework.org/): a library for building web
services using Django.
Most services will be build using this framework.

The most important parts of those docs are:

- [serializers](http://www.django-rest-framework.org/api-guide/serializers/): they are in charge
  of parsing and generating json to/from model instances
- [viewsets](http://www.django-rest-framework.org/api-guide/viewsets/): these are collections of
  services that share some model
- [routers](http://www.django-rest-framework.org/api-guide/routers/): these are the things that
  help you wire the viewsets methods into the django router in a consistent (restful) way.
