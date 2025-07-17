""" 
Project: server - My Portfolio
Author: Bruno Rian Nunes de Souza
License: GNU General Public License v3.0

This program is free software: you can redistribute it and/or modify it
under the terms of the GNU General Public License, version 3, as published
by the Free Software Foundation.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.
If not, see <http://www.gnu.org/licenses/>.
"""

from pathlib import Path
import re


def get_path_to_index() -> Path:
    """
    Return the path to index.html in the templates directory.

    This method returns an absolute path to the index.html file
    in the templates directory. The path is obtained by getting
    the path to the current file and going two directories up to
    get the project root directory, then going down to the templates
    directory and finally to the index.html file.

    Returns:
        Path: The absolute path to the index.html file in the
        templates directory.
    """
    
    return Path(__file__).parent.parent / "templates" / "index.html"


def read_content() -> str:
    """
    Read the content of the index.html file in the templates directory.

    This method opens the index.html file in the templates directory,
    reads its content and returns it as a string. The content is read
    in UTF-8 encoding.

    Returns:
        str: The content of the index.html file in the templates directory.
    """
    
    with open(get_path_to_index(), 'r', encoding='utf-8') as file:
        content = file.read()
        
    return content

def replace_content(content: str) -> str:
    """
    Replace static file paths in the given HTML content with Django static template tags.

    This function searches for occurrences of file paths in the content that start with '/static/' 
    and replaces them with Django's {% static %} template tag format. It also specifically replaces 
    the '/favicon.png' path with its corresponding {% static %} tag.

    Args:
        content (str): The HTML content in which static file paths need to be replaced.

    Returns:
        str: The content with static file paths replaced by Django static template tags.
    """

    
    content = re.sub(r'/static/(.+?)"', r"{% static '\1' %}\"", content)
    content = content.replace('/favicon.png', '{% static \'favicon.png\' %}')
    
    return content

def write_content() -> None:
    """
    Write the content of the index.html file with static file paths replaced by Django static template tags.

    This method reads the content of the index.html file, replaces the static file paths with Django's
    {% static %} template tags and writes the modified content back into the file.
    """
    
    with open(get_path_to_index(), 'w', encoding='utf-8') as file:
        
        file.write(replace_content(read_content()))

def main():
    """
    Main entry point for the script.

    This function calls the write_content method which reads the content of the index.html file, 
    replaces the static file paths with Django's {% static %} template tags and writes the modified 
    content back into the file.
    """
    
    write_content()
    
if __name__ == "__main__":
    """
    Only used this service one time, it changes the content of index.html to use Django static template tags
    """
    main()
