import csscompressor

def _compress_css(css_file_loc:str, css_file_out_loc:str) -> None:
    css_file_content: str

    with open(css_file_loc, 'r') as css_file:
        css_file_content = css_file.read()
    
    with open(css_file_out_loc, 'w') as css_file_out:
        css_file_out.write(csscompressor.compress(css_file_content))
    

