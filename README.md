# 42 Project Template Builder

## Table of Contents

1. [Description](#description)
2. [Requirements](#requirements)
3. [Usage](#usage)
4. [Alias](#alias)
5. [Example](#example)

## Description

This is a Python script that builds a 42 Project Template for your C Projects.

## Requirements

- Git
- Python 2.7.16 or later versions

## Usage

Clone the repository:
```Shell
git clone https://github.com/SrRecursive/42ProjectTemplateBuilder
```

Go inside the folder:
```Shell
cd 42ProjectTemplateBuilder
```

Run the file:
```Shell
python main.py
```

It will ask you the project name:

```Shell
Introduce the name of the project: "hello_world"
```
**NOTE:** In Python 3.X you have to introduce the name of the project without double quotes.

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

## Alias

Since it creates the template in the current directory, you can create an alias to run the program, so you will be able to execute it anywhere.

To do that, open your .bashrc or .zshrc with your favorite text editor.
```Shell
vim ~/.zshrc
```

Add at the end of the file the following line:

```Shell
alias build ="python ~/(path_of_repository)/42ProjectTemplateBuilder/main.py"
```

## Example

```Shell
cd ~/Documents
mkdir pipex
cd pipex
build
```

It will generate this directory tree:
```text
pipex
| - include
|   | - pipex.h
| - src
|   | - pipex.c
| - utils
|   | - utils.c
| - Makefile
```

- **pipex.h**
```C
#ifndef PIPEX_H
# define PIPEX_H

/* <--Defines Section--> */

/* <--Libraries Section--> */
# include <stdio.h>

/* <--Structs Section--> */

/* <--Functions Section--> */
void	ribanab(void);

#endif
```

- **pipex.c**
```C
#include "../include/pipex.h"

int	main(int argc, char **argv)
{
	printf("Hello World\n");
	ribanab();
	return (0);
}
```

- **utils.c**
```C
#include "../include/pipex.h"

void	ribanab(void)
{
	printf("ribana-b is a 42 Student :O\n");
	return ;
}
```

- **Makefile**
```Makefile
# ========================================================================== #

# <-- Color Library --> #

# <-- Text Color --> #
T_BLACK = \033[30m
T_RED = \033[31m
T_GREEN = \033[32m
T_YELLOW = \033[33m
T_BLUE = \033[34m
T_MAGENTA = \033[35m
T_CYAN = \033[36m
T_WHITE = \033[37m

# <-- Text Style --> #
BOLD = \033[1m
ITALIC = \033[2m
UNDERLINE = \033[3m
STRIKETHROUGH = \033[4m

# <-- Background Color --> #
B_RED = \033[31m
B_BLACK = \033[30m
B_GREEN = \033[32m
B_YELLOW = \033[33m
B_BLUE = \033[34m
B_MAGENTA = \033[35m
B_CYAN = \033[36m
B_WHITE = \033[37m

# <-- Reset Everything --> #
RESET = \033[0m

# ========================================================================== #

# <-- Library's Name --> #
NAME = pipex

# <-- Compilation Command --> #
CC = gcc

# <-- Compilation Flags --> #
CFLAGS = -Wall -Wextra -Werror

# <-- Remove Command -->#
RM = rm -f

# <-- Directories --> #
SRC_DIR = src/
UTILS_DIR = utils/

# <-- Files --> #
SRC_FILES = pipex.c
UTILS_FILES = utils.c

# <-- Directories + Files --> #
SRC = $(addprefix $(SRC_DIR), $(SRC_FILES))
UTILS = $(addprefix $(UTILS_DIR), $(UTILS_FILES))

# <-- Objects --> #
OBJ_SRC = $(SRC:.c=.o)
OBJ_UTILS = $(UTILS:.c=.o)

# ========================================================================== #

# <-- Main Target --> #
all: $(NAME)

# <--Library Creation--> #
$(NAME): $(OBJ_SRC) $(OBJ_UTILS)
	@echo "$(T_YELLOW)$(BOLD)Objects created successfully$(RESET)"
	ar rcs $(NAME) $(OBJ_SRC) $(OBJ_UTILS)
	@echo "$(T_YELLOW)$(BOLD)$(NAME) created successfully$(RESET)"

# <-- Objects Creation --> #
%.o: %.c
	$(CC) $(FLAGS) -c $< -o $@

# <-- Objects Destruction --> #
clean:
	$(RM) $(OBJ_SRC) $(OBJ_UTILS)
	@echo "$(T_RED)$(BOLD)Objects destroyed successfully$(RESET)"

# <- Clean Execution + pipex Destruction -> #
fclean: clean
	$(RM) $(NAME)
	@echo "$(T_RED)$(BOLD)$(NAME) destroyed successfully$(RESET)"

# <- Fclean Execution + All Execution -> #
re: fclean all

# <- Targets Declaration -> #
.PHONY = all clean fclean re

# ========================================================================== #
```
