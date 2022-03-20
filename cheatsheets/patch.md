## Creating a patch file

```
diff -u file1 file2 > patchfile.patch
```

## Applying a patch file

```
patch file1 patchfile.patch
```

## Reverse a patch

```
patch -p0 -R -i patchfile.patch
```

## patch Directories

```
diff -ruN folder1/ folder2/ > patchfile.patch

patch -s -p0 < patchfile.patch
```
