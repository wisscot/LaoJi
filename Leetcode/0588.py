# 588. Design In-Memory File System
'''
Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.
'''

Basic idea: file system is a tree
Define Node as below to represent both file and folder


class NodeType:
    folder = "folder"
    file = "file"

class Node:
    def __init__(self, nodeType: str):
        self.type = nodeType
        self.children = {}
        self.content = ""
        

class FileSystem:
    # key operatios: 
    #     list, create dir(recursively), create file
    # data structure:
    #     tree with hashmap
    # time complex
    
    def __init__(self):
        self.root = Node(NodeType.folder)

    def ls(self, path: str) -> List[str]:
        current_node = self.getNodeFromPath(path)
        if current_node.type == NodeType.folder:
            return sorted(current_node.children.keys())
        return [path.split("/")[-1]]
        

    def mkdir(self, path: str) -> None:
        # sanity check
        self.createNodeFromPathRecursively(path)        

    def addContentToFile(self, filePath: str, content: str) -> None:
        folderNode = self.getNodeFromPath(filePath[:filePath.rindex("/")])
        fileName = filePath[filePath.rindex("/")+1:]
        fileNode = folderNode.children.setdefault(fileName, Node(NodeType.file))
        fileNode.content += content
        
    def readContentFromFile(self, filePath: str) -> str:
        # assume last node in the path is file node
        fileNode = self.getNodeFromPath(filePath)
        return fileNode.content

    def getNodeFromPath(self, path: str) -> Node:
        #assume path is valid, otherwise needs sanity check
        if path == "/":
            return self.root
        
        path_nodes = path.split("/")[1:]
        current_node = self.root        
        for path_node in path_nodes:
            current_node = current_node.children[path_node]
        return current_node

    def createNodeFromPathRecursively(self, path: str) -> None:
        path_nodes = path.split("/")[1:]
        current_node = self.root
        for path_node in path_nodes:
            current_node = current_node.children.setdefault(path_node, Node(NodeType.folder))
        

# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.ls(path)
# obj.mkdir(path)
# obj.addContentToFile(filePath,content)
# param_4 = obj.readContentFromFile(filePath)