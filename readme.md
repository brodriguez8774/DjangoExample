
# Example Django Project

## Project Description

A very basic Django project, to show how the general framework functions.

Note that the base project url will give a 404, and then list all possible valid urls, which are as follows:
* /admin/ - These are the "admin" views that Django automatically generates. Apps 3, 4 and 5 have customized these
views as well. App 6 does not have models and thus has no associated admin views.
* /ex1/ - Standard urls for Example App 1.
* /ex2/ - Standard urls for Example App 2.
* /ex3/ - Standard urls for Example App 3.
* /ex4/ - Standard urls for Example App 4.
* /ex5/ - Standard urls for Example App 5.
* /ex6/ - Standard urls for Example App 6.
* /ex7/ - Standard urls for Example App 7.
* /ex8/ - Standard urls for Example App 8.


## App Descriptions:

* Example App 1:
    * A very basic app with essentially the bare minimum to have a functioning project.
    * Has a single, lone model. Note that model does not have any extended functionality defined.
        *  Ex: Look at how the admin view spells the model name.


* Example App 2:
    * A copy of App 1, except that it uses class-based views instead of method-based ones. Mostly to show that it's
    possible, as these tend to be less customizable and thus less functional than method-based ones.


* Example App 3:
    * A little bit more advanced app, showing how to create models that use a ForeignKey relation.
    * Also has customized admin views, as well as shows the basics of how to use more advanced templating.


* Example App 4:
    * Even more advanced, showing how to create models with a Many-to-Many relation.
    * Again, the admin views are customized and front end uses basic templating.


* Example App 5:
    * A variation on Example App 4. Uses a custom intermediary field for the Many-to-Many relation.
    * Otherwise identical to Example App 4.
    
    
* Example App 6:
    * An example of using an Ajax request. The Ajax itself generates and sends a random number.
    * On load, the page immediately sends a single Ajax request. The user can also click the button to send more.
    * Page updates dynamically (aka without reloading the entire page from scratch).


* Example App 7:
    * An example of adding React (a JavaScript extension) on top of Django templating. See below for more info on React.


* Example App 8:
    * A copy of App 7, except using Vue.js instead of React.js.
    * Created mostly for ease of mind to compare the two and be confident that we're choosing the correct one.

    
## React Notes

Unfortunately, React seems to prefer a syntax that browsers do not fully understand, out of the gate. To correct for
this, you will need to install "npm", and then use "browserify" to compile the code into a browser-friendly format.

(It's actually similar to how sass files compile into standard css. You write code that's easier to handle and far more
human-friendly. Then you use the console to run a compiler, changing the code into a format the browser understands.)

### Installing NPM

Npm is "the world's largest software registry" and what most front end libraries now seem to install through.

Npm now installs as part of NodeJS. The simplest way to install is to visit:
* https://nodejs.org/

### Installing Browserify for React

Browserify is a package which "transforms" files into browser-friendly formats.

Setting up Browserify for React is a two step process, and requires npm to be installed first.

* First, install Browserify globally via:
    * ```npm install browserify -g```
* Second, change to the project's root directory and install "other required npm packages":
    * ```npm install babel-cli babel-preset-env babel-preset-react babelify```

### Compiling React Files through Browserify

From the project's root directory, run:
* ```browserify -t [ babelify --presets [env react] ] <sourceFile> -o <destinationFile>```
    * Where \<sourceFile> is the original react file.
    * And \<destinationFile> is where the browser-friendly file is compiled to.


## Vue Notes

Vue is an alternative to react. As long as you keep Vue code within a single JavaScript file, then it doesn't need any
compiling, unlike react.

However, the downside is that portions of logic are intertwined within the template syntax. IE, it seems much harder to
understand the general logic at a glance because it's more spread out.
