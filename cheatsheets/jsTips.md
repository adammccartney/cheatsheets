# JavaScript tips and tricks

# asynchronous JS

## Promises

New style of async code that gets used in modern Web APIs. e.g.: `fetch()`
Modern, more efficient version of `XMLHttpRequest`

# Call stacks and hoisting

Be aware of the execution order that JavaScript implements by default.
It's non-sequential.

# Functional style

Consider:

```
const max = function(...values) {
    console.log (values instanceof Array);

    let large = values[0];

    for (let i = 0; i < values.length; i++) {
        if (values[i] > large) {
            large = values[i];
        }
    }

    return large;
};


```

vs.

```
const mmax = function(...values) {
    return values.reduce((large, e) => large > e ? large : e, values[0]);
};
```
