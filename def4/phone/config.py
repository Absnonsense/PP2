from configparser import ConfigParser
import os
def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    file_path = os.path.join(os.path.dirname(__file__), filename)
    with open(file_path, encoding='windows-1251') as f:
        parser.read_file(f)
    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception(f'Section {section} not found in {filename}')
    return config