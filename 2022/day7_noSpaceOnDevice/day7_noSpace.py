class SubDirectory:

    def __init__(self, name, size = 0):
        self.name = name
        self.size = size

class ParentDirectory:
    subDirs = []
    
    def __init__(self, name, size = 0):
        self.name = name
        self.size = size

    def addSubDir(self, subDir):
        self.subDirs.append(SubDirectory(subDir))


with open('day7_input.txt') as commandLine:
    TOTAL_UNDER_100000 = 0
    HOME_DIRS = []
    CURRRENT_DIRECTORY = None
    HOME_DIRECTORY = None
    for line in commandLine:
        line_strip = line.strip('\n')
        line_list = line_strip.split()

        #
        # Find the directories in the Home directory
        #
        if CURRRENT_DIRECTORY == '/' and '$' not in line_list:
            if 'dir' in line:
                HOME_DIRS.append(ParentDirectory(line_list[1]))
            else:
                ParentDirectory(CURRRENT_DIRECTORY).size = line_list[0]

        #
        # Look for changing of directories and store any unseen
        #   directory and subdirectory in lists as objects
        #
        if 'cd' in line_list:
            CURRRENT_DIRECTORY = line_list[2]
            # print("Your current directory:", CURRRENT_DIRECTORY)

            for direct in HOME_DIRS:
                if CURRRENT_DIRECTORY == direct.name:
                    HOME_DIRECTORY = CURRRENT_DIRECTORY
                    print("Home Directory Switched:", HOME_DIRECTORY)
                    # print("(IN HOME DIRS IF) Current Directory:", CURRRENT_DIRECTORY)
            # if CURRRENT_DIRECTORY != '..' and CURRRENT_DIRECTORY is not None and HOME_DIRECTORY is not None:
            #     if CURRRENT_DIRECTORY not in ParentDirectory(HOME_DIRECTORY).subDirs:
            #         ParentDirectory(HOME_DIRECTORY).addSubDir(CURRRENT_DIRECTORY)
            #         print("Subdirectory made:", SubDirectory(CURRRENT_DIRECTORY).name)
            #         # print('(IN SUB DIRS IF) Current Sub Directories:', HOME_DIRS[HOME_DIRECTORY].subDirs)

        #
        # Look for changing of directories and store any unseen
        #   directory and subdirectory in lists as objects
        #
        elif 'ls' in line_list:
            pass
        
        #
        # Look for directory in list command and add subdirectories
        #
        elif 'dir' in line_list:
            if CURRRENT_DIRECTORY != '..' and CURRRENT_DIRECTORY is not None and HOME_DIRECTORY is not None:
                for d in HOME_DIRS:
                    if CURRRENT_DIRECTORY != d.name and CURRRENT_DIRECTORY not in ParentDirectory(HOME_DIRECTORY).subDirs:
                        ParentDirectory(HOME_DIRECTORY).addSubDir(line_list[1])
                        print(line)
                        print("Subdirectory made:", SubDirectory(line_list[1]).name)
                        # print('(IN SUB DIRS IF) Current Sub Directories:', HOME_DIRS[HOME_DIRECTORY].subDirs)

        #
        # Assume line is file sizes and add to directory size
        #
        else:
            pass
                
        
            # while line[0] != '$':
            #     size, file = line.split()
            #     if int(size) <= 100000:
            #         total += int(size)
    for dir in HOME_DIRS:
        print(dir.name, dir.size)
    print('Total storage used:', TOTAL_UNDER_100000)