# Advent of Code 2019

My take on http:s//adventofcode.com/2019.

I'm going to do it in _Python_ to revive my rusty _Python_ skills. I'm not sure if I'll make it through the whole calendar due to time constraints but I'll try my very best. Let's see how far I will get...

## Install

This project uses _pipenv_ for package management. Make sure that it is installed [according to the following tutorial](https://realpython.com/pipenv-guide/).

To install this project, run

```sh
$ pipenv install --ignore-pipfile
```

from this directory.

If you want to run tests and other development tools, install the project by running

```sh
$ pipenv install --dev --ignore-pipfile
```

## Run

### Activate environment

To activate the environment for this project, execute

```sh
$ pipenv shell
```

### Run challenges

Challenges are run from within ```challenges``` folder.

```sh
$ cd challenges
```

To run a specific challenge, execute

```sh
$ python day01
```

## Run tests

Tests can be run from the project root as well as from any specific sub-folder.

To run the tests in the directory tree of the current directory, execute

```sh
$ pytest
```


