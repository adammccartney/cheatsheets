# Setup

# permissions
After install, make sure mongodb user has ownership of the socket

```
chown -R mongodb:mongodb /var/lib/mongodb
chown mongodb:mongodb /tmp/mongodb-27017.sock
```
## storage locations

## data

`/var/lib/mongodb`

## logs
`/var/log/mongodb`


# Crash course

+ document is effectively equal to a row in a relational db
+ a collection is a table with a dynamic schema
+ a single instance of mongodb can host multiple independant databases
+ every document has a special key `_id` that is unique within a collection
+ mongosh is a fully functional javascript interpreter


## Authoriuzation & Authentication

### user admin


#### read
Read data on all nonsystem collections and on the following system collections:
system.indexes, system.js, and system.namespaces.
#### readWrite
Provides same privileges as read , plus the ability to modify data on all nonsystem
collections and the system.js collection.
#### dbAdmin
Perform administrative tasks such as schema-related tasks, indexing, and gather‐
ing statistics (does not grant privileges for user and role management).
#### userAdmin
Create and modify roles and users on the current database.
#### dbOwner
Combines the privileges granted by the readWrite, dbAdmin, and userAdmin
roles.
#### clusterManager
Perform management and monitoring actions on the cluster.
#### clusterMonitor
Provides read-only access to monitoring tools such as the MongoDB Cloud Man‐
ager and Ops Manager monitoring agent.
#### hostManager
Monitor and manage servers.
#### clusterAdmin
Combines the privileges granted by the clusterManager, clusterMonitor, and host‐
Manager roles, plus the dropDatabase action.
#### backup
Provides sufficient privileges to use the MongoDB Cloud Manager backup agent
or the Ops Manager backup agent, or to use mongodump to back up an entire
mongod instance.
#### restore
Provides privileges needed to restore data from backups that do not include sys‐
tem.profile collection data.
#### readAnyDatabase
Provides same privileges as read on all databases except local and config, plus the
listDatabases action on the cluster as a whole.
#### readWriteAnyDatabase
Provides same privileges as readWrite on all databases except local and config,
plus the listDatabases action on the cluster as a whole.
#### userAdminAnyDatabase
Provides same privileges as userAdmin on all databases except local and config
(effectively a superuser role).
#### dbAdminAnyDatabase
Provides same privileges as dbAdmin on all databases except local and config, plus
the listDatabases action on the cluster as a whole.
#### root
Provides access to the operations and all the resources of the readWriteAnyData‐
base, dbAdminAnyDatabase, userAdminAnyDatabase, clusterAdmin, restore, and
backup roles combined.



## Commands 

### create db

`use <dbname>`

You need to add at least one document for the database to show up in `show
databases`

`>db.notes.insertOne({"name":"notes"})`

### create user

```
db.createUser({user: "tester", pwd: "secret", roles: [{role: "dbOwner", db: "notes"}]})
```

### add extra roles to user



