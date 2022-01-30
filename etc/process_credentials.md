process credentials
===================

## real User ID and real Group ID

At login, the shell pulls these values from the /etc/passwd file according to
whoever happens to be logging in.

## effective User ID and effective group ID

On most unix systems, these values determine the permissions granted to the
process that is currently running as it tries to perform specific operations.
Unlike real ID, the effective ID's privileges can be escalated and processes
can be enabled to run various tasks, say for example with effective ID of 0 or
root.

## Set-User-ID or Set-Group-ID

This will allow the program to *gain* privileges that it normally wouldn't
have. These privileges are gained when the process running the program is
started and the processes UID and GID are inherited. (These don't have any
effect on Linux ... as we've discovered recently!)

## Saved Set-User-ID and Saved Set-Group-ID

If the previous flags have been set, then the IDs of the parent process who
started the program running are 1). used to elevate the program's effective ID
and 2). copied. 


## File-System User ID and File-System Group ID

Specific to linux, enabled only after calling two routines `setfsuid()
setfsgid()`


# Interface available for elevating privileges

|   Interface         |  unprivileged proc       | privileged proc  | portability         |
|---------------------|--------------------------|------------------|------------------   |
|  `setuid(u)`        | Change effective ID      | Change real,     | Specified SUSv3     |
|  `setgid(g)`        | to the same val as       | effective, and   | BSD derivatives     |
|                     | current run proc         | saved set IDs to | have different      |
|                     |                          | any (single) val | semantics           |
|---------------------|--------------------------|------------------|------------------   |
| `seteuid(e)`        | Change effective ID      | Change effective | Specified SUSv3     |
| `setegid(e)`        | to the same val as       | ID to any value  |                     |
|                     | current real or          |                  |                     |
|                     | saved set IDs            |                  |                     |
|---------------------|--------------------------|------------------|------------------   |
| `setreuid(r, e)`    | (Independently)          | (Independently)  | Specified SUSv3,    | 
| `setregid(r, e)`    | change realID to same    | change real and  | but operation       |
|                     | val as current real      | effective IDs to | varies across       |
|                     | or effective ID and      | any value.       | implementations     |
|                     | effective ID to same     |                  |                     |
|                     | val as current real,     |                  |                     |
|                     | effective or saved       |                  |                     |
|                     | set ID                   |                  |                     |
|---------------------|--------------------------|------------------|------------------   |
| `setresuid(r,e,s)`  | (Independently)          | (Independently)  | Not in SUSv3 and    |
| `setresgid(r,e,s)`  | change real, efffective, | change real,     | present on few      |
|                     | and saved set IDs to same| effective, and   | other UNIX          |
|                     | value as current real,   | saved set IDs to | implementations     |
|                     | effective, or saved set  | any values       |                     |
|                     | ID                       |                  |                     |
|---------------------|--------------------------|------------------|------------------   |
| `setfsuid(u)`       | Change file-system ID to | Change file-     | Linux-specific      |
| `setfsgid(g)`       | same value as curent real| system ID to any |                     |
|                     | effective, file system,  | value            |                     |
|                     | or saved set ID          |                  |                     |
|---------------------|--------------------------|------------------|------------------   |
| `setgroups(n, l)`   | Can't be called from     | Set supplmentary | Not in SUSv3, but   |
|                     | an unprivileged proc     | group IDs to any | available on all    |
|                     |                          | values           | UNIX implmentations |
