# Working with webpack

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

## Webpack config js 

This is actually quite a useful little tool in terms of building. At the very
least, it provides devs with a place to specify the resources needed to build
the project. In some cases the resources will be in the style of build
patterns: source-target paris for transpiling the main javascript application.
Also any modules that will be packaged are specified in the config. 
