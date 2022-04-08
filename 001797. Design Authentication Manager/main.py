from typing import List


class AuthenticationManager:
    def __init__(self, timeToLive: int):
        self.timeToLive = timeToLive
        self.tokens = {}

    def generate(self, tokenId: str, currentTime: int) -> None:
        self.tokens[tokenId] = currentTime + self.timeToLive        

    def renew(self, tokenId: str, currentTime: int) -> None:
        expiration = self.tokens.get(tokenId)
        if expiration:
            if expiration > currentTime:
                self.tokens[tokenId] = currentTime + self.timeToLive

    def countUnexpiredTokens(self, currentTime: int) -> int:
        return len([_ for _, expiration in self.tokens.items() if currentTime < expiration])


def tdd(func_list, args_list):
    obj = AuthenticationManager(*args_list[0])
    ans = [None]
    for f, args in zip(func_list[1:], args_list[1:]):
        f_ = getattr(obj, f)
        ans.append(f_(*args))
    return ans


if __name__ == "__main__":
    print(tdd(
        ["AuthenticationManager", "renew", "generate", "countUnexpiredTokens", "generate", "renew", "renew", "countUnexpiredTokens"],
        [[5], ["aaa", 1], ["aaa", 2], [6], ["bbb", 7], ["aaa", 8], ["bbb", 10], [15]]
    ))
    print(tdd(
["AuthenticationManager","generate","countUnexpiredTokens","countUnexpiredTokens","renew","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","generate","countUnexpiredTokens","countUnexpiredTokens","renew","countUnexpiredTokens","countUnexpiredTokens","renew","renew","countUnexpiredTokens","generate","countUnexpiredTokens","generate","renew","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","renew","renew","renew","generate","countUnexpiredTokens","renew","renew","generate","countUnexpiredTokens","generate","countUnexpiredTokens","countUnexpiredTokens","generate","generate","renew","countUnexpiredTokens","generate","renew","renew","renew","generate","generate","countUnexpiredTokens","countUnexpiredTokens","generate","renew","renew","generate","countUnexpiredTokens","countUnexpiredTokens","renew","countUnexpiredTokens","countUnexpiredTokens","countUnexpiredTokens","generate"],
[[444],["jvkl",16],[41],[53],["qvgq",88],[101],[119],[126],[137],["nesq",150],[161],[167],["ix",179],[181],[185],["kh",195],["rk",196],[197],["rrbox",207],[218],["wpqr",240],["prj",274],[296],[298],[320],[336],["d",339],["z",343],["ri",354],["fkpk",404],[429],["ix",434],["ytqq",506],["fqlu",519],[562],["wxmcw",578],[594],[619],["iz",623],["zaqb",629],["ugxe",640],[664],["smeb",665],["z",673],["rihj",674],["qikse",717],["rnizc",735],["ugxe",791],[803],[815],["jnofa",851],["ryp",857],["jvkl",862],["l",863],[871],[873],["ugxe",875],[902],[913],[979],["dqad",984]]  
    ))

# [null,null,1,1,null,1,1,1,1,null,2,2,null,2,2,null,null,2,null,3,null,null,4,4,4,4,null,null,null,null,5,null,null,null,5,null,5,5,null,null,null,6,null,null,null,null,null,null,8,8,null,null,null,null,10,10,null,10,10,9,null]
# [null,null,1,1,null,1,1,1,1,null,2,2,null,2,2,null,null,2,null,3,null,null,4,4,4,4,null,null,null,null,5,null,null,null,5,null,5,5,null,null,null,6,null,null,null,null,null,null,8,8,null,null,null,null,9,9,null,9,9,8,null]

