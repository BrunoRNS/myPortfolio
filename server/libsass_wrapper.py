from settings import BASE_DIR
import sass
import sys

def compile_scss(input_file_loc: str, output_file_loc: str) -> str:
    file: str
    
    input_file_loc = BASE_DIR / input_file_loc
    output_file_loc = BASE_DIR / output_file_loc


    with open(input_file_loc, 'r') as input_scss:
       file = input_scss.read()

    with open(output_file_loc, 'w') as output_css:
       output_css.write(sass.compile(string=file, output_style='compressed'))

if __name__ == '__main__':
    compile_scss(sys.argv[1], sys.argv[2])