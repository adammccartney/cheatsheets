# designing simple sites with nextjs

to fire up a site:

`npx create-next-app@latest`

## Typically design pattern

1. create component
2. Load component into layout

# Styling

## Using bootstrap

There is a specific way to load bootstrap, typically we want to install it
using node and then load it in the app component using the `useEffect` Function

```
import 'bootstrap/dist/css/bootstrap.css'
import '../styles/globals.css'
import { useEffect } from "react";

function MyApp({ Component, pageProps }) {
  useEffect(() => {
    import("bootstrap/dist/js/bootstrap");
  }, []);

  return <Component {...pageProps} />;
}

export default MyApp
```
