#Simple Web Application That Shows AWS Instances

###Depedencies
* Inenv installation setup [here](http://github.com/pnegahdar/inenv)
* All other dependencies will be installed once python wrapper is initialized

```shell
    $ pip install inenv
```

### Run python server

```shell
    $ cd ask-flask
    $ inenv init ask-flask
    $ inenv ask-flask
    $ python app.py
```

### Run Frontend Server
```npm
    $ cd fe/
    $ npm install
    $ gulp develop
```

####Notes:
* Visit http://127.0.0.1:3000
* Configurable Flask Settings are in config.py
* You need aws access_key and secret_key to login and view instances.




