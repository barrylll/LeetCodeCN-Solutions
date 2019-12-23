class Solution(object):
    def simplifyPath(self, path: str) -> str:
        path_list = []
        temp = ""
        flag = 0
        for i in range(len(path)):
            if path[i] == "/":
                flag ^= 1
                while i < len(path) - 1 and path[i + 1] == "/":
                    i += 1
                if temp:
                    path_list.append(temp)
                temp = ""
            else:
                temp += path[i]
        if temp:
            path_list.append(temp)

        ret_list = []
        for i in path_list:
            if i == ".":
                continue
            elif i == "..":
                if ret_list:
                    ret_list.pop(-1)
            else:
                ret_list.append(i)

        ret = ""
        for i in ret_list:
            ret = ret + "/" + i

        if ret:
            return ret
        else:
            return "/"


if __name__ == '__main__':
    print(
        Solution().simplifyPath("/../")
    )
