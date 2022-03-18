# guile 3.0.7 installation guide

lifted verbatim from: https://www.linuxfromscratch.org/blfs/view/svn/general/guile.html

First, fix a build failure with glibc-2.34 installed:

```
sed -e 's/#ifndef __attribute_maybe_unused__//' \
    -e '174d'                                   \
    -i lib/libc-config.h
```

Install Guile by running the following commands:

```
./configure --prefix=/usr    \
            --disable-static \
            --docdir=/usr/share/doc/guile-3.0.7 &&
make      &&
make html &&

makeinfo --plaintext -o doc/r5rs/r5rs.txt doc/r5rs/r5rs.texi &&
makeinfo --plaintext -o doc/ref/guile.txt doc/ref/guile.texi
```

To test the results, issue: ./check-guile.

Now, as the root user:

```
make install      &&
make install-html &&

mkdir -p                       /usr/share/gdb/auto-load/usr/lib &&
mv /usr/lib/libguile-*-gdb.scm /usr/share/gdb/auto-load/usr/lib &&
mv /usr/share/doc/guile-3.0.7/{guile.html,ref} &&
mv /usr/share/doc/guile-3.0.7/r5rs{.html,}     &&

find examples -name "Makefile*" -delete         &&
cp -vR examples   /usr/share/doc/guile-3.0.7   &&

for DIRNAME in r5rs ref; do
  install -v -m644  doc/${DIRNAME}/*.txt \
                    /usr/share/doc/guile-3.0.7/${DIRNAME}
done &&
unset DIRNAME
```
