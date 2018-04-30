
# Example Django Project

## Project Description

A very basic Django project, to show how the general framework functions.

Note that the base project url will give a 404, and then list all possible valid urls, which are as follows:
* /admin/ - These are the "admin" views that Django automatically generates. Apps 3 and 4 have customized these
views as well.
* /ex1/ - Standard urls for Example App 1.
* /ex2/ - Standard urls for Example App 2.
* /ex3/ - Standard urls for Example App 3.
* /ex4/ - Standard urls for Example App 4.


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
