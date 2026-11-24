import os

def createDir(dirName):
    os.makedirs(dirName, exist_ok=True)

def createFile(dirName, fileName):
    try:
        with open(os.path.join(dirName, fileName), "x"):
            pass
    except FileExistsError:
        print(fileName + " already exists")


if __name__ == "__main__":
    try:
        # currentDir = os.path.dirname(os.path.realpath(__file__))
        currentDir = input("Give your path: ")
        createDir(currentDir)
        createFile(currentDir, "index.html")

        assets = os.path.join(currentDir,"assets")
        createDir(assets)

        lib = os.path.join(currentDir,"lib")
        createDir(lib)
        createFile(lib, "script.js")

        src = os.path.join(currentDir,"src")
        createDir(src)
        
        scss = os.path.join(src,"scss")
        createDir(scss)
        createFile(scss, "main.scss")

        css = os.path.join(src,"css")
        createDir(css)
        createFile(css, "main.css")

    except Exception as e:
        print("An Error Occurred:")
        print(e)

