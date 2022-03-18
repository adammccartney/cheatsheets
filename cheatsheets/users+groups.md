# users and groups

Each user as a unique login name and user identifier (UID). They can belong to
one of more groups. Each group also has a specific identifier (GID). These IDs
are used to determine ownership of resources and to control permissions granted
to processes accessing those resources.

# storage and retrieval of sensitive information

The thing to remember about all info relating to users and groups is that they
need to be stored on the system somewhere. Historically this had been
`/etc/passwd`. This method was insecure as many unprivileged system utils
required read access to information stored in the password file. This lead to
secrurity issues, as it was possible to compile dictionaries of common words or
names in order to try and crack encrypted password information. For this
reason, a linux system stores this sensitive information in a socalled shadow
password file. Open access information is still stored in the passwd file, but
encrypted passwords are stored in the shadow file, which only privileged
processes can access.

# processes that require validation

Typically, the `crypt()` interface is used for cases where we need to
authenticate a user password within the context of a process. The function
`getpass()` is used to gather a password from user input (while at the same
time masking any echo of the password to the shell). This is a pretty much
universally used inteface and is offered by such implementations as python's
getpass module.

Once a password has been collected via getpass, an authentication will
typically occur by comparing the hased password returned from the call to
`crypt()` with the user's input. Crypt gets run with the userinput (plaintext)
password as the first arg and the (encypted) password that was retrieved from
the shadow password file.
