# Advent of Code 2019

My take on [adventofcode.com/2019](https//adventofcode.com/2019).

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

### Activate the environment

To activate the environment for this project, execute

```sh
$ pipenv shell
```

Check if a _Python_ version >= 3.7 is being returned:

```sh
$ python --version
Python 3.7.5
```

### Run challenges

To run a specific challenge, execute it like this:

```sh
$ python challenges/day_01/challenge_01.py
```

It will return the result to be submitted to [adventofcode.com](https://adventofcode.com).

## Run tests

Tests can be run from the project root as well as from any specific sub-folder.

To run the tests in the directory tree of the current directory, execute

```sh
$ pytest
```


