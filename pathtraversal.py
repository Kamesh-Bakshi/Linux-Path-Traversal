class Directory(object):
    def __init__(self, name,parent):
        self.name = name
        self.children = list()
        self.parent = parent 


class PathTraversal(object):
    
    def __init__(self):

        self.root = Directory('/',None)
        self.current_directory = self.root
        self.location = list()
        
    def execute(self, user_input: str):
        
        user_input = user_input.strip().split() # 1212001
        
        if user_input[0] == 'pwd':
            return self.Get_Path()
        if user_input[0] == 'ls':
            return self.List_Directory()
        
        length = len(user_input)
        
        if length == 1:
            return "invalid input"
        
        if user_input[0] == 'cd':
            
            return self.Change_Directory(user_input[1])
        
        elif user_input[0] == 'mkdir':
            return self.Make_Directory(user_input[1])
        
        elif user_input[0] == 'rm':
            return self.Remove_Directory(user_input[1])
        
        else:
            return "    ERR: CANNOT RECOGNIZE INPUT." 

    
    def Get_Path(self):
        
        return "    PATH: /" + "/".join(self.location)


    
    def List_Directory(self):

        childs = list()
        for child in self.current_directory.children:
            childs.append(child.name)

        return "    DIRS: " + "  ".join(childs)

    """ There are 3 Cases common for cd , mkdir and rm commands.
    1. Change/Add/Remove in same directory.
    2. Change/Add/Remove in grand child of dirrectory.
    3. If path is given is from root directory. """
    
    def Change_Directory(self, path_list):

        initial_path = list(self.location)
        
        if path_list == "..":

            if self.current_directory.name == '/':
                return "SUCCESS"
            
            current_node = self.current_directory
            self.current_directory = current_node.parent
            self.location.pop()
            return "SUCCESS"
        
         
        if len(path_list) == 1:
            if path_list[0] == '/':
                self.current_directory = self.root
                self.location = list()
                return "    SUCC: REACHED"
            
        if path_list[0] == '/':
            count = path_list[1]
            Flag1 = True
            
            
            for child in self.current_directory.children:
                if child.name == count:
                    Flag1 = False
                    break
                
       
            if Flag1:
                self.current_directory = self.root
                self.location = list()
            path_list = path_list[1:]

      
        path_list = path_list.strip().split('/')
        
    
        if len(path_list) == 1:

            for child in self.current_directory.children:

                if child.name == path_list[0]:
                    self.current_directory = child
                    self.location.append(child.name)
                    return "    SUCC: REACHED"
            self.location = initial_path
            return "    ERR: INVALID PATH"

      
        pointer = self.location
        node = self.current_directory
        
        for name in path_list:

          
            node_flag = False

            for child in node.children:

                if child.name == name:
                    node_flag = True
                    pointer.append(child.name)
                    node = child
                    break

            if node_flag == False:
                self.location = initial_path
                return "    ERR: INVALID PATH"
            
        self.location = pointer
        self.current_directory = node
        return "    SUCC: REACHED"

   
    def Make_Directory(self, path_list):

        
        original_path = self.location
        original_node = self.current_directory

     
        Flag = False
        if path_list[0] == '/':
            
            
            Flag1 = True
            count = path_list[1]
            for child in self.current_directory.children:
                
                if child.name == count:
                    Flag1 = False
                    break
                
           
            if Flag1:
                Flag = True 
                self.current_directory = self.root
                self.location = list()
            path_list = path_list[1:]
        
        path_list = path_list.strip().split('/')


        if Flag == False and len(path_list) == 1:

            for child in self.current_directory.children:
                
           
                if child.name == path_list[0]:
                    return "    ERR: DIRECTORY ALREADY EXISTS"

            new_node = Directory(path_list[0],self.current_directory)
            self.current_directory.children.append(new_node)
            
            return "    SUCC: CREATED"

        
        node = self.current_directory
        count = 0
        for name in path_list:
            
       
            node_flag = False

            for child in node.children:

                if child.name == name:
                    
                    count += 1
                    node = child
                    node_flag = True
                    break
                
            if not node_flag and count == len(path_list) - 1:
                
                new_node = Directory(name,node)
                node.children.append(new_node)
                count += 1
                break
            
            
            if node_flag == True and count == len(path_list):
                
                return "    ERR: DIRECTORY ALREADY EXISTS"
                
           
            if node_flag == False and count < len(path_list) - 1:
                
                self.location = original_path
                self.current_directory = original_node
                return "    ERR: INVALID PATH"

        if count == len(path_list):
            
            if Flag:
                self.location = original_path
                self.current_directory = original_node
            return "    SUCC: CREATED"
        
        return "    ERR: DIRECTORY ALREADY EXISTS"


    def Remove_Directory(self, path_list):

        original_path = self.location
        original_node = self.current_directory

       
        Flag = False
        if path_list[0] == '/':
            
            
            to_check = path_list.strip().split('/')
            if original_node.name == to_check[-1]:
                count = original_path.pop()
            
    
            Flag1 = True
            count = path_list[1]
            for child in self.current_directory.children:
                if child.name == count:
                    Flag1 = False
                    break
                
           
            if Flag1:
                Flag = True 
                self.current_directory = self.root
                self.location = list()
            path_list = path_list[1:]

        path_list = path_list.strip().split('/')
        
      
        if Flag == False and len(path_list) == 1:
            for child in self.current_directory.children:
                
                if child.name == path_list[0]:
                    child_list = child.children
                    if len(child_list) > 0:
                        return " CANNOT BE DELETED"
                    
                    temp = self.current_directory.children.pop(self.current_directory.children.index(child))
                    return "    SUCC: DELETED"
            return "    ERR: INVALID PATH"

        
        pointer = self.location
        node = self.current_directory
        count = 0

        for name in path_list:
            
            node_flag = False

            for child in node.children:
                if child.name == name:
                    node_flag = True
                    count += 1
                    pointer = node
                    node = child

                
                if node_flag and count == len(path_list):
                    if Flag:
                        self.location = original_path
                        self.current_directory = original_node
                    child_list = child.children
                    if len(child_list) > 0:
                        return " CANNOT BE DELETED"
                    pointer.children.remove(child)
                    return "    SUCC: DELETED"

        return "    ERR: INVALID PATH"
