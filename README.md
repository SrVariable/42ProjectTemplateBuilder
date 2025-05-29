# 42 Project Template Builder

## Table of Contents

1. [Description](#description)
2. [Requirements](#requirements)
3. [Usage](#usage)

## Description

This is a Python script that builds a 42 Project Template for your C Projects.

## Requirements

- Git
- Python3

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

It will ask you the project name, your login, your email and a tag,
which will be displayed alongside 42 logo.

```Shell
Project Name: hello_world
Login: ribana-b
Email: ribana-b@student.42malaga.com
Tag: Málaga
```

> [!NOTE]
>
> Tag field is optional. By default is set to your campus, extracted
> from email.

It will create the following directory tree in the current directory:

```text
| - hello_world
|   | - include
|   |   | - hello_world.h
|   | - src
|   |   | - hello_world.c
|   | - utils
|   |   | - utils.c
|   | - Makefile
```
