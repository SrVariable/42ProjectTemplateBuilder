import os
from datetime import datetime

def create_section(title, separator):
    padding = (80 - (2 * len(separator)) - 4)
    l_padding = int((padding - len(title)) / 2)
    r_padding = l_padding if len(title) % 2 == 0 else l_padding + 1

    section = f"{separator} @" + "-" * padding + f"@ {separator[::-1]}\n"
    section += f"{separator} |" + " " * l_padding + title + " " * r_padding + f"| {separator[::-1]}\n"
    section += f"{separator} @" + "-" * padding + f"@ {separator[::-1]}"

    return section

# Function to create respective directories
def create_dirs():
    if (not os.path.exists("include")):
        os.makedirs("include")
    if (not os.path.exists("src")):
        os.makedirs("src")
    if (not os.path.exists("utils")):
        os.makedirs("utils")

# Function to create the 42 header
def create_header(filename, username, email):
    max_length = 46

    if (len(filename) > max_length):
        new_length = max_length - 1 - len(filename)
        filename = filename[:new_length].ljust(new_length)

    author = "By: " + username + " <" + email + ">"
    if (len(author) > max_length):
        new_length = max_length - 1 - len(author)
        author = author[:new_length].ljust(new_length)

    creation_date = "Created: " + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " by " + username
    if (len(creation_date) > max_length):
        new_length = max_length - 1 - len(creation_date)
        creation_date = creation_date[:new_length].ljust(new_length)

    update_date = "Updated: " + datetime.now().strftime("%Y/%m/%d %H:%M:%S") + " by " + username
    if (len(update_date) > max_length):
        new_length = max_length - 1 - len(update_date)
        update_date = update_date[:new_length].ljust(new_length)

    # First line
    header = "/* " + "*" * 74 + " */\n"

    # Empty line
    header += "/* " + " " * 74 + " */\n"

    # Middle
    header += "/*" + " " * 57 + ":::      ::::::::  */\n"
    padding = max_length + 6 - len(filename)
    header += "/*   " + filename + " " * padding + ":+:     :+:     :+:  */\n"
    header += "/*" + " " * 53 + "+:+ +:+         +:+    */\n"
    padding = max_length + 2 - len(author)
    header += "/*   " + author + " " * padding + "+#+  +:+       +#+       */\n"
    header += "/*" + " " * 49 + "+#" * 5 + "+   +#+          */\n"
    padding = max_length + 5 - len(creation_date)
    header += "/*   " + creation_date + " " * padding + "#+#    #+# Malaga     */\n"
    padding = max_length + 4 - len(update_date)
    header += "/*   " + update_date + " " * padding + "###   ########.com     */\n"

    # Empty line
    header += "/* " + " " * 74 + " */\n"

    # Last line
    header += "/* " + "*" * 74 + " */\n"

    return header

# Function that generates the main file
def c_main_template(header, name):
    file = open(os.path.join(f"src/{name}.c"), 'w')
    with open(os.path.join(f"src/{name}.c"), 'w') as file:
        file.write(
                f'''\
{header}
#include "{name}.h"

int\tmain(void)
{{
\tribanab();
\treturn (0);
}}
'''
        )

# Function that generates the header file
def c_header_template(header, name):
    separator = "/*"

    with open(os.path.join(f"include/{name}.h"), 'w') as file:
        file.write(
            f'''\
{header}
#ifndef {name.upper()}_H
# define {name.upper()}_H

{create_section("Define Section", f"{separator}")}

{create_section("Include Section", f"{separator}")}

# include <stdio.h>

{create_section("Typedef Section", f"{separator}")}

{create_section("Enum Section", f"{separator}")}

{create_section("Struct Section", f"{separator}")}

{create_section("Function Section", f"{separator}")}

void\tribanab(void);

#endif
'''
        )

# Function that generates the utils file
def c_utils_template(header, name):
    with open(os.path.join("utils/utils.c"), 'w') as file:
        file.write(
            f'''\
{header}
#include "{name}.h"

void\tribanab(void)
{{
\tprintf("Hello World, I am ribana-b from 42 Malaga c:\\n");
\treturn ;
}}
'''
        )

# Function that generates the Makefile template
def c_makefile_template(name):
    separator = "#"
    with open(os.path.join("Makefile"), 'w') as file:
        file.write(
            f'''\
{create_section("Macro Section", f"{separator}")}

NAME := {name}

INCLUDE_DIR := include/
SRC_DIR := src/
UTILS_DIR := utils/
OBJ_DIR := obj/

INCLUDE_FILES := {name}.h
SRC_FILES := {name}.c
UTILS_FILES := utils.c

INCLUDE = $(addprefix $(INCLUDE_DIR), $(INCLUDE_FILES))
SRC = $(addprefix $(SRC_DIR), $(SRC_FILES))
UTILS = $(addprefix $(UTILS_DIR), $(UTILS_FILES))

VPATH = $(SRC_DIR)\\
        $(UTILS_DIR)\\

OBJ = $(patsubst $(SRC_DIR)%.c, $(OBJ_DIR)%.o, $(SRC))\\
 \t\t$(patsubst $(UTILS_DIR)%.c, $(OBJ_DIR)%.o, $(UTILS))\\

CC = clang
CFLAGS := -Wall -Wextra -Werror -MMD -MP
CPPFLAGS := -I $(INCLUDE_DIR)
LDFLAGS := 
LDLIBS := 

RM := rm -rf

{create_section("Target Section", f"{separator}")}

all: $(NAME)

clean:
\t@$(RM) $(OBJ_DIR)
\t$(CLEAN_MSG)

fclean: clean
\t@$(RM) $(NAME)
\t$(FCLEAN_MSG)

re:
\t@$(MAKE) -s fclean
\t@$(MAKE) -s all

.PHONY: all clean fclean re

$(NAME): $(OBJ)
\t$(OBJ_MSG)
\t@$(CC) -o $(NAME) $(OBJ) $(LDFLAGS) $(LD_LIBS) # Use this if you want to create a program
\t@#ar rcs $(NAME) $(OBJ) # Use this if you want to create a library
\t$(OUTPUT_MSG)

$(OBJ_DIR):
\t@mkdir -p $(OBJ_DIR)

$(OBJ_DIR)%.o: %.c | $(OBJ_DIR)
\t$(COMPILE_MSG)
\t@$(CC) $(CFLAGS) $(CPPFLAGS) -c $< -o $@

-include $(OBJ:.o=.d)

{create_section("Colour Section", f"{separator}")}

T_BLACK := \\033[30m
T_RED := \\033[31m
T_GREEN := \\033[32m
T_YELLOW := \\033[33m
T_BLUE := \\033[34m
T_MAGENTA := \\033[35m
T_CYAN := \\033[36m
T_WHITE := \\033[37m

BOLD := \\033[1m
ITALIC := \\033[2m
UNDERLINE := \\033[3m
STRIKETHROUGH := \\033[4m

CLEAR_LINE := \\033[1F\\r\\033[2K

RESET := \\033[0m

{create_section("Message Section", f"{separator}")}

COMPILE_MSG = @echo -e "🌊 🦔 $(T_BLUE)$(BOLD)Compiling $(T_WHITE)$<...$(RESET)"
OBJ_MSG = @echo -e "✅ 🦔 $(T_MAGENTA)$(BOLD)$(NAME) $(T_YELLOW)Objects $(RESET)$(T_GREEN)created successfully!$(RESET)"
OUTPUT_MSG = @echo -e "✅ 🦔 $(T_MAGENTA)$(BOLD)$(NAME) $(RESET)$(T_GREEN)created successfully!$(RESET)"
CLEAN_MSG = @echo -e "🗑️  🦔 $(T_MAGENTA)$(BOLD)$(NAME) $(T_YELLOW)Objects $(RESET)$(T_RED)destroyed successfully!$(RESET)"
FCLEAN_MSG = @echo -e "🗑️  🦔 $(T_MAGENTA)$(BOLD)$(NAME) $(RESET)$(T_RED)destroyed successfully!$(RESET)"
'''
        )

# Main function
def main():
    project_name = input('Introduce the name of the project: ')
    username = input('Introduce your login: ')
    email = input('Introduce your email: ')
    create_dirs()
    project_name = project_name.replace(" ", "")
    c_main_template(create_header(f"{project_name}.c", username, email), project_name)
    c_header_template(create_header(f"{project_name}.h", username, email), project_name)
    c_utils_template(create_header(f"{project_name}.c", username, email), project_name)
    c_makefile_template(project_name)

if (__name__ == "__main__"):
    main()
