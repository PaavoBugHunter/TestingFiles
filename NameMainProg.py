import NameMainImport #Why does the entire NameMainImport module get executed right-away?

def firstprint():
    print("Module was ran.")

def secondprint():
    print("Second function in NameMainProg was run.")

if __name__ == "__main__":
    firstprint()
else:
    secondprint()