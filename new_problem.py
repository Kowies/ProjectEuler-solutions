import os

def main():
    number_of_problem = input('Which Problem are you going to do? (e.g "013") ')

    path = "./Problem " + number_of_problem

    try:  
        os.mkdir(path)
    except OSError:  
        print ('Creation of the directory "%s" failed' % path)
    else:  
        print ('Successfully created the directory "%s"' % path)

        path_of_file = path + "/script.py"
        with open(path_of_file,"w+") as f:
            pass


if __name__ == "__main__":
    main()