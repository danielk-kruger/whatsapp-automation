from parser import Parser


def main():
    p = Parser()

    print(p.file_paths)
    p.get_contactlist()



if __name__ == '__main__':
    main()
