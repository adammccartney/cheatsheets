# Postgres cheat sheet

## Source compiled on Debian/Ubuntu

The hand-compiled versions on on debian will try to set the Unix socket as
`/var/run/postgresql`, this conflicts with the settings created by the
hand-compiled version and will emit the error:

```
psql: error: could not connect to server: No such file or directory
        Is the server running locally and accepting
                connections on Unix domain socket "/tmp/.s.PGSQL.5432"?

```

The workaround for this is to

```
psql -h /var/run/postgresql
```

## Importing a db from backup

- Create db locally

```
createdb newdb
```

### Database roles

The db that is being imported will likely have a specific role associated with
it. This role needs creation. Any of the following commands are helpful in this
respect.

```
psql> CREATE ROLE name;
```

```
psql> DROP ROLE name;
```

Wrappers to use these commands from system shell:

```
createuser name
dropuser name
```

Check if it worked:

```
psql> SELECT rolname FROM pg_roles;
```

Check if the permissions are the same as they were with dumped db

```
psql> SELECT * FROM pg_roles;
```

Add a password:

psql>

### Restore Backup

```
pg_restore -x --no-privileges --if-exists -1 -c -U postgres -d scheitportal /home/adam/scheit_backup_4-10-21
```

##

SELECT \* from django_migrations;

## Alter Role permissions

```
CREATE ROLE user_name PASSWORD 'pass' NOSUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;

ALTER USER tester CREATEDB CREATEROLE LOGIN;

ALTER DATABASE test_db OWNER TO tester

DELETE FROM django_migrations WHERE id = 28
```

SELECT pg_catalog.setval('mdwuser_customuser_id_seq', 3, false);

## Run psql on another port

```
sudo su - postgres -c "psql --port=5435"
```

or as postgres
```
postgres ~>psql --port=5435 
```


## Nuxeo specific selects

```
SELECT * FROM hierarchy WHERE primarytype = 'Audio';
```

