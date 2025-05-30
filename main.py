import os
import re
import sys
from datetime import datetime

PROGRAM_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))

class Env:
    def __init__(self):
        self.config = {
                'USERNAME': '',
                'EMAIL': '',
                'TAG': '',
                }
        self.is_loaded = False

    def load(self):
        env_path = PROGRAM_PATH + '/.env'
        if not os.path.exists(env_path):
            return False

        with open(env_path, 'r') as f:
            for line in f:
                config = line.split('=')
                key, value = config[0].strip(), config[1].strip()
                self.config[key] = value

        self.is_loaded = True
        return True


def create_project_structure(project_name):
    paths = [ "include", "src", "utils" ]
    for path in paths:
        if (not os.path.exists(f"{project_name}/{path}")):
            os.makedirs(f"{project_name}/{path}")


def create_section(title, separator):
    title += ' Section'
    padding = (80 - (2 * len(separator)) - 4)
    l_padding = int((padding - len(title)) / 2)
    r_padding = l_padding if len(title) % 2 == 0 else l_padding + 1

    section = f"{separator} @" + "-" * padding + f"@ {separator[::-1]}\n"
    section += f"{separator} |" + " " * l_padding + title + " " * r_padding + f"| {separator[::-1]}\n"
    section += f"{separator} @" + "-" * padding + f"@ {separator[::-1]}"

    return section


# Function to create custom 42 header
def create_header(filename, username, email, tag):
    fields = email.split('.')
    if len(fields) < 3:
        raise Exception("Not a valid 42 email")

    if tag == '':
        tag = fields[1][2:11] if fields[1][:2] == '42' else fields[1][:9]
        tag = tag.capitalize()
    else:
        tag = tag[:9]

    tld = '.'.join(fields[2:])[:6]
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
    header += f"/*   {filename}" + " " * padding + ":+:     :+:     :+:  */\n"
    header += "/*" + " " * 53 + "+:+ +:+         +:+    */\n"
    padding = max_length + 2 - len(author)
    header += f"/*   {author}" + " " * padding + "+#+  +:+       +#+       */\n"
    header += "/*" + " " * 49 + "+#" * 5 + "+   +#+          */\n"
    padding = max_length + 5 - len(creation_date)
    padding2 = 11 - len(tag)
    header += f"/*   {creation_date}" + " " * padding + f"#+#    #+# {tag}" + " " * padding2 + "*/\n"
    padding = max_length + 4 - len(update_date)
    padding2 = 8 - len(tld)
    header += "/*   " + update_date + " " * padding + f"###   ########.{tld}" + " " * padding2 + "*/\n"

    # Empty line
    header += "/* " + " " * 74 + " */\n"

    # Last line
    header += "/* " + "*" * 74 + " */"

    return header


# Get template from `templates` directory
def get_template(template_name):
    section_pattern = re.compile('`create_section .+`')
    header_pattern = re.compile('`create_header .+`')

    template_path = f"{PROGRAM_PATH}/templates/{template_name}"
    template = ''

    with open(template_path) as f:
        template = [line for line in f]

    return template


def format_template(template, comment_type, project_name, config):
    section_pattern = re.compile('`create_section .+`')
    header_pattern = re.compile('`create_header .+`')
    project_name_pattern = '`project_name`'

    username = config["USERNAME"]
    email = config["EMAIL"]
    tag = config["TAG"]

    formatted_template = ''
    for line in template:
        # TODO: Figure out a better way to replace project_name to allow
        # any case style
        if project_name_pattern in line:
            line = line.replace(project_name_pattern, project_name)
        elif project_name_pattern.upper() in line:
            line = line.replace(project_name_pattern.upper(), project_name.upper())

        if section_pattern.match(line):
            title = line.strip()[16:-1].capitalize()
            line = create_section(title, comment_type) + '\n'
        elif header_pattern.match(line):
            filename = line.strip()[15:-1]
            line = create_header(filename, username, email, tag) + '\n'

        formatted_template += line

    return formatted_template


def generate_include(filename, project_name, config):
    template = get_template('header_template.h')
    template = format_template(template, "/*", project_name, config)
    with open(os.path.join(f"{project_name}/include/{filename}"), 'w') as f:
        f.write(template)


def generate_src(filename, project_name, config):
    template = get_template('main_template.c')
    template = format_template(template, "/*", project_name, config)
    with open(os.path.join(f"{project_name}/src/{filename}"), 'w') as f:
        f.write(template)


def generate_utils(filename, project_name, config):
    template = get_template('utils_template.c')
    template = format_template(template, "/*", project_name, config)
    with open(os.path.join(f"{project_name}/utils/{filename}"), 'w') as f:
        f.write(template)


def generate_makefile(project_name, config):
    template = get_template('Makefile')
    template = format_template(template, "#", project_name, config)
    with open(os.path.join(f"{project_name}/Makefile"), 'w') as f:
        f.write(template)

# Main function
if (__name__ == "__main__"):
    project_name = input('Project Name: ')
    if project_name == '':
        raise Exception("Project name can't be empty")

    env = Env()
    env.load()

    username = env.config["USERNAME"] if env.is_loaded else input('Login: ')
    if username == '':
        raise Exception("Username can't be empty")

    email = env.config["EMAIL"] if env.is_loaded else input('Email: ')
    if email == '':
        raise Exception("Email can't be empty")

    tag = env.config["TAG"] if env.is_loaded else input('Tag: ')

    project_name = project_name.replace(" ", "")
    create_project_structure(project_name)

    generate_include(f'{project_name}.h', project_name, env.config)
    generate_src('main.c', project_name, env.config)
    generate_utils('utils.c', project_name, env.config)
    generate_makefile(project_name, env.config)
