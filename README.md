GoDaddy DynDNS script
Don't use godaddy!
![godaddy ceo kills elephant](http://www.geek.com/wp-content/uploads/2011/03/bob-parsons-GoDaddy-elephant.jpg)

To configure the script for your domain to update the GoDaddy entry just fill it
in with your GoDaddy key and secret.

```json
{
    "key": "qH3Df29ysxdDaT8p7PWMRV8rVuU75EjHy",
    "secret": "A4pXPyNJs2v6SF2kjXoS",
    "domain": "main-domain.eu",
    "subdomain": "subdomain"
}
```

and save it as conf.json
Call the script regularly. It will try to avoid contacting external services as
much as possible.
