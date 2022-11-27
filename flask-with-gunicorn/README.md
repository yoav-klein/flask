# Flask with GUnicorn
---

Here we will see how to run a Flask application and serve it using GUnicorn.

GUnicorn is a WSGI-compatible HTTP server, which interacts with WSGI-compatible 
web frameworks, such as Flask, Django, etc.

Reminder: A WSGI server needs the web application (web framework) to define a standard
callable object (function, class, etc.), such as:
```
def application(environ: dict, start_response: Callable) -> List:
   ... 
   resp_headers = { ... }
   start_response("200 OK", resp_headers)
   ...
   data = ...
   return data
```

The web server imports this object, and calls it for each request it gets.

So in our example, when we define:
```
app = Flask(__name__)
```

The `app` object is a callable. So now we need to tell GUnicorn from where to import this object.

This is done by passing the GUnicorn executable the path to this object:

```
$ gunicorn --bind=0.0.0.0 wsgi:app
```

NOTE: The `wsgi` module is redundant, we don't really need it. We could just:
```
$ gunicorn --bind=0.0.0.0 my_web_app:app
```


