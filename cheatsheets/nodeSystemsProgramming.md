# Heading towards an understanding of asynchronous routines

node has a lot of inbuilt functionality for managing standard unix style
systems programming tasks. In other words, the api for managing various tasks
like spawning child processes.

# Event emitters and err callback arguments

The big thing to remember with asynchronous programing in node is that
asynchronous functions are basically a way of instantiating future events. In
other words, by writing an async function, you are basically saying that this
resulting exeucutiong of the following procedure will happen at some time in
the future.

# It seems easy to forget to introduce elements of timing to programs

In other words, one issue that I seem to be running into is this idea of a
seemingly frozen process...

Consider the following code, it sets up a child process resonably successfully,
and it will watch the file whose name is passed in as an arg on the command
line. There is nothing inside the fs.open to detect the file being deleted.
That is, you can set this program running in the environment and then delete
the file that it is watching. The deletion has no noticeable effects on the
process, it just continues to watch the now non-existant file.

```
'use strict';

const fs = require('fs');

const filename = process.argv[2];

fs.open(filename, 'r', (err, fd) => {
    if (err) {
        if (err.code === 'ENOENT') {
            console.error('No file descriptor present');
            return;
        }
        throw err;
    }
    try {
        const spawn = require('child_process').spawn;
        fs.watch(filename, () => {
            const ls = spawn('ls', ['-l', 'h', filename]);
            ls.stdout.pipe(process.stdout);
        });
        console.log(`Now watching ${filename} for changes...`);
    } finally {
        fs.close(fd, (err) => {
            if (err) throw err;
        });
    }
});
```
