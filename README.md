redir
=====

url redirection service

## server

```
$ python redir.py -b 127.0.0.1 -p 5000

 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
127.0.0.1 - - [12/Jun/2015 12:26:03] "GET /?url=https%3A%2F%2Fwww.google.com HTTP/1.1" 301 -
```

## client

```
$ curl -i -G http://localhost:5000/ --data-urlencode url=https://www.google.com

HTTP/1.0 301 MOVED PERMANENTLY
Content-Type: text/html; charset=utf-8
Content-Length: 251
Location: https://www.google.com
Server: Werkzeug/0.10.4 Python/2.7.10
Date: Fri, 12 Jun 2015 04:24:45 GMT

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
<title>Redirecting...</title>
<h1>Redirecting...</h1>
<p>You should be redirected automatically to target URL: <a href="https://www.google.com">https://www.google.com</a>.  If not click the link.
```
