# Tutorial for React

## Python virtual machine
  - Make sure that you have python3 installed
  - cd into $PROJECT_DIR
  - Run the following code
  ```shell
  $ python3 -m venv env
  $ source env/bin/activate
  $ pip install --upgrade pip
  $ pip install -r requirements.txt
  ```
  - Just remember to run `$ source env/bin/activate` before every development session

## React toolchain setup
  - Run the following code to setup Nodeenv virtual machine
  ```shell
  $ nodeenv --python-virtualenv
  $ deactivate
  $ source env/bin/activate # activate again since we added another environment
  ```
  - Test if the nodeenv is setup correctly
  ```shell
  $ echo $VIRTUAL_ENV
  # PROJECT_DIR/env
  $ echo $NODE_VIRTUAL_ENV
  # PROJECT_DIR/env
  ```
  - Install the packages
  - Pull from master branch to get #PROJECT_DIR/package.json file
  - Run the following code in #PROJECT_DIR
  ```shell
  $ npm install .
  ```
  - You should see #PROJECT_DIR/node_modules folder appear, which contains all the JavaScript modules that we need for the front end

## Setup the file tree
  ```shell
  $ mkdir PROJECT_DIR/js
  $ touch PROJECT_DIR/js/main.jsx
  ```

## Compile jsx to js
  - Since we are using ES6 standard of JavaScript, we have to convert it into the browser standard ES5 JavaScript using webpack. 
  ```shell
  # This will compile all your jsx code into one bundle.js(the only script need to be included in the HTML template)
  $ ./node_modules/.bin/webpack
  ```
