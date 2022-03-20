# Some notes on headless browsing with puppeteer

# Set up for debug

```
  const browser = await puppeteer.launch({
      headless: false,     // run in a visible browser
      sloMo: 250;          // slow it down

  });
```
