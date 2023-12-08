class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        duplicates = {}
        for path in range(len(paths)):
            folder, *files = paths[path].split()
            for fileName in files:
                content = fileName.split(".")[-1][2:-1]
                fileName = fileName.split(".")[0] + ".txt"
                if content not in duplicates:
                    duplicates[content] = []
                duplicates[content].append(folder + "/" + fileName) 
        res = []
        for k,v in duplicates.items():
            if len(v) > 1:
                res.append(v)
        return res