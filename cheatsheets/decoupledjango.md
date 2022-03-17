# Some notes on improving django practices 


## environment files are useful ... 

Typically I will have an .env file in the project root that I use for
development, `source .env` will set the following variables
```
DJANGO_SETTINGS_MODULE=decoupled_dj.settings.development
```

## uvicorn

`uvicorn project.asgi:application`

## asyncio

python interpreter is single threaded, so in order to avoid tying up the event
loop when a call does not return within a reasonable amount of time, the
asyncio library was introduced in python 3.5.

