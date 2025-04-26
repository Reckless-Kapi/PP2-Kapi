from configparser import ConfigParser

def load_config(filename='database.ini', section='postgresql'):
    parser = ConfigParser()
    parser.read('lab 11/phonebook/database.ini')

    config = {}
    if parser.has_section(section):
        for param in parser.items(section):
            config[param[0]] = param[1]
    else:
        raise Exception(f"Section {section} not found in {filename}")
    return config


if __name__ == "__main__":
    config = load_config()
    print(config)

