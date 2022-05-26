import textract
import os
import argparse

def convert_source_to_txt(path, output_directory=None):
    text = textract.process(path)
    text = text.decode("utf-8")
    full_path = path.split("/")
    name_file = full_path[-1]
    name_without_format = name_file.split(".")
    final_name = name_without_format[0]
    final_name_with_text = f'{final_name}.txt'
    if output_directory is not None:
        final_path = f'{output_directory}/{final_name_with_text}'
        with open(final_path, 'w') as f:
            f.write(text)
    else:
        with open(final_name_with_text, 'w') as f:
            f.write(text)
    

def sources_to_txt(path, output_directory=None):
    if os.path.isdir(path):
        list_of_files = os.listdir(path)
        for file in list_of_files:
            name_of_file = (f'{path}/{file}')
            if output_directory is not None:
                convert_source_to_txt(name_of_file, output_directory)
            else:
                convert_source_to_txt(name_of_file)
    if os.path.isfile(path):
        if output_directory is not None:
            convert_source_to_txt(path, output_directory)
        else:
            convert_source_to_txt(path)

def parse_opt():
    parser = argparse.ArgumentParser()
    parser.add_argument('--path', type=str, help='path of file, can be a directory')
    parser.add_argument('--output-directory', type=str, help='optional path output directory')
    opt = parser.parse_args()
    return opt

def main(opt):
    sources_to_txt(**vars(opt))


    
if __name__ == "__main__":
    opt = parse_opt()
    main(opt)

