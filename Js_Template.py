import os

def createDir(dirName):
    if(os.path.exists(dirName)):
        print(dirName + " already exists")
    else:
        os.mkdir(dirName)

def createFile(dirName, fileName):
    if(os.path.exists(os.path.join(dirName,fileName))):
        print(fileName + " already exists")
    else:
        file = open(os.path.join(dirName,fileName), "w+")


if __name__ == "__main__":
    try:
        currentDir = os.path.dirname(os.path.realpath(__file__))
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

