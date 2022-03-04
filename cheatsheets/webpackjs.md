Working with webpack
===============================================================================

This document contains personal notes taken while reading through the excellent
[webpack online docs][]

Generally, I've been trying to use the vue cli to get up and running with vue
projects. For a beginner, this tool seems way too heavyweight. Also some of the
more experienced devs at work are using webpack to structure their projects. 

Webpack seems to enable a little more light weight package management, enabling
developers to organize their projects in a more modular way. The typical
workflow goes a bit like this:

+ create project directory and install webpack
```
mkdir myproject
cd myproject
npm install webpack webpack-cli --save-dev
```


Set up basic directory structure 
```
mkdir dist/ src/
touch dist/index.html src/index.js 
```

From this point, the project can be built using the `npx webpack` command. 
Generally though, we follow the steps of setting up a webpack.config.json

[webpack online docs](https://webpack.js.org/guides)

## Webpack config js 

This is actually quite a useful little tool in terms of building. At the very
least, it provides devs with a place to specify the resources needed to build
the project. In some cases the resources will be in the style of build
patterns: source-target paris for transpiling the main javascript application.
Also any modules that will be packaged are specified in the config. 


## Output management 

A very useful plugin for handling the actual compile targets of the javascript
code that you are writing is 'HtmlWebpackPlugin'


## Development

One thing that is immediately noticeable about javascript development is that
the practice of debugging does not seem to be emphasized nearly as much as with
other languages (like c or python). There seems slightly more emphasis on the
higher level details than the details of how the code is being run. This seems
to contrast a bit with lower level languages, where it's pretty much standard
fare to know about how the code that you right is being translated into
something that the machine can read. Anyone who has spent anything more than
the briefest length of time hacking around in c will quickly discover that they
are going nowhere fast without intimate knowledge of the tools required for the
debugging process.
Of course it's the year 2021 and JavaScript is so widely used that it would
probably be insane to claim that the there is any one community that emphasizes
certain aspects of the language over others. That said, I've found myself in
situations recently when trying to get a handle of some of the tooling around
frameworks where I felt that there was basically no emphasis being put on how
to get rolling with the practical tools needed to work with the particular
framework. Specifically I was running into issues around working with the vue
cli and getting projects up and running and building properly. Okay, okay...the
vue docs do specifically point out that the vue cli is not intended to be used
by beginners and it assumes a fairly detailed working knowledge of JavaScript.
I've built some fairly substantial projects in python, java, c and c++ but
admittedly nothing really that great in javascript yet. I've probably been
underestimating it as a language slightly. Because of the fact it is so
ubiquitous, there are definitely many niches to get stuck into. Particularly
when it comes to the hyper quick changing world of frontend frameworks.
Nevertheless, there are a lot of really great and clear explanations and
excursions into the world of the bytecode interpreter in which javascript is
run [to be found][]
While your caching up on gutsy details of the lanugage, there are also a bunch
of super useful development tools available in webpack. 

[to be found](https://mathiasbynens.be/notes/shapes-ics)

## Source maps

Okay, so for debugging it's probably enough to get rolling with the
'inline-source-map' option provided by webpack.

It might be useful to investigate webpack-watch also, this may provide 
GNU-make like functionality i.e. compiles only what has changed on build. 


## Code Splitting

Much like header inclusion in c, we're going to want to avoid duplication of
code. Webpack offers a way to avoid code duplication. It's acutally quite a
clever model whereby you declare the dependency graph explicitly in the `entry`
property of the config. There is a plugin called 'SplitChunksPlugin' that
allows us to extract common dependencies into an existing entry chunk or an
entirely new chunk.

### Dynamic Imports

The use of async functions is common in modern webpack usage.

An [anylyzer tool][] is very useful for seeing just how modules have been
organized.

[analyzer tool](https://github.com/webpack-contrib/webpack-bundle-analyzer)

### Lazy Loading 

The practice of loading modules i.e. chunks as they are required is a very
common pattern when working with frameworks. There are a number of good
articles around [lazy loading with vue][]


[lazy loading with vue](https://vuedose.tips/dynamic-imports-in-vue-js-for-better-performance) 


## Caching

This seems to be particulary useful when loading modules whose content will not
change very regularly (like frameworks). These workflows in and around loading
code chunks in the browser are very reminiscent of the types of procedures that
get implemented when designing a virtual machine. 

