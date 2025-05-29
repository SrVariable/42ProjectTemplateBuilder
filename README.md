# 42 Project Template Builder

## Table of Contents

1. [Description](#description)
2. [Requirements](#requirements)
3. [Usage](#usage)
4. [Alias](#alias)

## Description

This is a Python script that builds a 42 Project Template for your C Projects.

## Requirements

- Git
- Python 3

## Usage

Clone the repository:
```Shell
git clone https://github.com/SrVariable/42ProjectTemplateBuilder
```

Go inside the folder:
```Shell
cd 42ProjectTemplateBuilder
```

Run the file:
```Shell
python3 main.py
```

It will ask you the project name, your login and your email

```Shell
Introduce the name of the project: hello_world
Introduce your login: ribana-b
Introduce your email: ribana-b@student.42malaga.com
```

It will create the following directory tree in the current directory:

```text
| - include
|   | - hello_world.h
| - src
|   | - hello_world.c
| - utils
|   | - utils.c
| - Makefile
```

> [!TIP]
> If you don't want to type this every time you can modify the inputs for strings
> with your login and email in the file main.py
> Check [personal](https://github.com/SrVariable/42ProjectTemplateBuilder/blob/personal/main.py) to see an example.

## Alias

Since it creates the template in the current directory, you can create an alias to run
the program, so you will be able to execute it anywhere.

```Shell
alias build="python3 ~/(path_of_repository)/42ProjectTemplateBuilder/main.py" >> ~/.${SHELL##/bin/}rc
```
