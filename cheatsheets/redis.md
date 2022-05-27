# redis cheats


## Move results of a scan to another db

Move all keys that match a specific pattern to database 1

```
redis-cli --scan --pattern '<pattern>' | xargs -I % redis-cli move % 1 > /dev/null
```

## Delete results of a scan

```
redis-cli --scan --pattern 'something' | xargs redis-cli del
```

## Show object idletime

```
OBJECT IDLETIME <key>
```

