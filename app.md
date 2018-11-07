# Application archictecture
## November 7th, 2018

### 1. What are the key features of the application? Are these clearly separated into their own files, classes, and/or modules?
    So far, my app is composed of a ouple of key components
    * web app - my app.py file utilizes the flask framework to make our application accessible via the web
    * histogram - There are currently four different implementations of a histogram that is used for keeping track of the different *types* of words and their *tokens*
    * sampling - sample.py provides two sampling functions (one weighted, one purely random) to sample words out of our histograms
Right now, these three components are broken down into their own modules, however not their classes.

### 2. Are the names of files, modules, functions, and variables appropriate and accurate? Would a new programmer be able to understand the names without too much contextual knowledge?
    For the most part, yes. I believe that i've provided pretty intuitive naming for most items listed above. However, there is definitely work that can be done to make sure that a new programmer
    would be able to roll into my project without too much contextual knowledge.

### 3. What are the scopes of the and are they appropriate for their use case? If they are global variables, why are they needed?
    99% of my variables are defined within the scopes of the functions I've created. I have one global variable, `histogram`, in app.py because I only want to create the histogram once and didn't know how
    to do so with flask being mixed into the project.

### 4. Are the functions small and clearly specified, with as few side effects as possible?
    I'd say roughly 80% of my functions are small and try to complete only one task. As for side effects, i've tried to reduce most functions to having as little parameters and global
    variables as possible to reduce any potential side effects 

### 5. Are there functions that could be better organized in an Object-Orientated Programming style by defining them as methods of classes?\
    Definitely. For example, all histogram modules I have act as classes that encapsulate all the functions that would be needed to create a histogram class. 

### 6. Can files be used as both modules and scripts?
    Currently, some can while others can't. I've made tons of files that do have functionality alongside being a library of things other scripts would need but then have some that only
    implement the latter.
### 7. Do modules depend on eachother or can they all be used separately?
   90% of my current modules are independent of other modules. Both `app.py` and `sample.py` both rely on the histogram modules in order to function. 
