
# Before using session
---

In this example, we have a simple website with the `/login` endpoint,
When you browse to this endpoint, you can fill in your name,
and when hit `Submit` you'll be redirected to the `/<usr>` endpoint, where `<usr>`
is what you submitted. 
This page will then just print your name to the screen.

What if we want to access the user's name in another page in our site?
This is why we use `session` for.