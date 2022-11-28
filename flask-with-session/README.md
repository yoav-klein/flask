# Using session
---

What we want to do here is, we want the user to log in, and then to be redirected 
to the `/user` endpoint, (not to the `/<usr>` where `<usr>` is the name submitted by the user), 
and be displayed with the user name.

Since the session iformation is being stored on the server, it must be encrypted. This is done
by specifying a key `app.secret` - this value can be anything.

The `session` object is basically just a dictionary that stores information throughout the
session of the user with the website. 
 
