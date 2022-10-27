class Solution:
    def simplifyPath(self, path: str) -> str:
        path_lis = path.split("/")
        can_path = []
        
        # print(path_lis)
        for ele in path_lis:
            if ele == "" or ele == ".":
                continue
            elif ele == "..":
                if can_path:
                    can_path.pop()
            else:
                can_path.append(ele)
            
            # print(can_path)
            
        return "/"+"/".join(can_path)