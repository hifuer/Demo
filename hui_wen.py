def hui_wen(s):
    '''
    检查s是不是回文
    思路:
    检查abcdefgfedcba 是不是回文
    检查bcdefgfedcb 是不是回文
    检查cdefgfedc 是不是回文
    检查defgfed 是不是回文
    检查efgfe 是不是回文
    检查fgf是不是回文
    检查g是不是回文

    '''
    if len(s)<2:
        #s长度小2位时，s是回文
        return True
    elif s[0] != s[-1]:
        #第一个和最后一个不相等 
        return False
    return hui_wen(s[1:-1])#递归去s[0],s[-1]   return hui_wen(s[1,-1])  切片用：我用了，号
    # return s[0] == s[-1] and hui_wen(s[1:-1])   #elif 省略模式

print(hui_wen('hello'))
print(hui_wen('abcdefgfedcba'))
