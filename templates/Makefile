`create_section macro`

NAME := `project_name`

INCLUDE_DIR := include/
SRC_DIR     := src/
UTILS_DIR   := utils/
OBJ_DIR     := obj/

INCLUDE_FILES := `project_name`.h
SRC_FILES     := main.c
UTILS_FILES   := utils.c

INCLUDE := $(addprefix $(INCLUDE_DIR), $(INCLUDE_FILES))
SRC     := $(addprefix $(SRC_DIR), $(SRC_FILES))
UTILS   := $(addprefix $(UTILS_DIR), $(UTILS_FILES))

VPATH := $(SRC_DIR)\
			$(UTILS_DIR)\

OBJ := $(patsubst $(SRC_DIR)%.c, $(OBJ_DIR)%.o, $(SRC))\
		$(patsubst $(UTILS_DIR)%.c, $(OBJ_DIR)%.o, $(UTILS))\

CC       := clang
CFLAGS   := -Wall -Wextra -Werror -MMD -MP
CPPFLAGS := -I $(INCLUDE_DIR)
LDFLAGS  := 
LDLIBS   := 

RM := rm -rf

`create_section target`

all: $(NAME)

clean:
	@$(RM) $(OBJ_DIR)
	$(CLEAN_MSG)

fclean: clean
	@$(RM) $(NAME)
	$(FCLEAN_MSG)

re:
	@make -s fclean
	@make -s all

.PHONY: all clean fclean re

$(NAME): $(LIBBFL) $(LIBMLX42) $(OBJ_DIR) $(OBJ)
	$(OBJ_MSG)
	@$(CC) -o $@ $(OBJ) $(CPPFLAGS) $(LDFLAGS) $(LDLIBS)
	$(OUTPUT_MSG)

$(OBJ_DIR):
	@mkdir -p $(OBJ_DIR)

$(OBJ_DIR)%.o: %.c | $(OBJ_DIR)
	@$(COMPILE_MSG)
	@$(CC) -o $@ $(CFLAGS) $(CPPFLAGS) -c $<

-include $(OBJ:.o=.d)

`create_section colour`

T_BLACK   := \033[30m
T_RED     := \033[31m
T_GREEN   := \033[32m
T_YELLOW  := \033[33m
T_BLUE    := \033[34m
T_MAGENTA := \033[35m
T_CYAN    := \033[36m
T_WHITE   := \033[37m

BOLD          := \033[1m
ITALIC        := \033[2m
UNDERLINE     := \033[3m
STRIKETHROUGH := \033[4m

CLEAR_LINE := \033[1F\r\033[2K

RESET := \033[0m

`create_section message`

COMPILE_MSG = @echo -e "🌊 🦔 $(T_BLUE)$(BOLD)Compiling $(T_WHITE)$<...$(RESET)"
OBJ_MSG     = @echo -e "✅ 🦔 $(T_MAGENTA)$(BOLD)$(NAME) $(T_YELLOW)Objects $(RESET)$(T_GREEN)created successfully!$(RESET)"
OUTPUT_MSG  = @echo -e "✅ 🦔 $(T_MAGENTA)$(BOLD)$(NAME) $(RESET)$(T_GREEN)created successfully!$(RESET)"
CLEAN_MSG   = @echo -e "🗑️  🦔 $(T_MAGENTA)$(BOLD)$(NAME) $(T_YELLOW)Objects $(RESET)$(T_RED)destroyed successfully!$(RESET)"
FCLEAN_MSG  = @echo -e "🗑️  🦔 $(T_MAGENTA)$(BOLD)$(NAME) $(RESET)$(T_RED)destroyed successfully!$(RESET)"
