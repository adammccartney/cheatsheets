# Linux container secutiry

## Capabilities

There are 3 high level options for using capabilites:

1. run containers as root with a large set of capabilities and try to maintain
   the capabilities manually

2. Run containers as root with a much more limited set of capabilities and
   never change them within the container.

3. Run containers as an unpriviliged user without any capabilities

Option 2 is the most reaslistic.

## Example:

Docker omits the CAP\_ prefix when managing capabilities

```
docker run --rm -it --cap-drop ALL --cap-add CHOWN alpine chown nobody /
```
