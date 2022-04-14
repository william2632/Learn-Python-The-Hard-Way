# 423 · Valid Parentheses      423. 有效的括号序列
# https://www.lintcode.com/problem/423/
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

class Solution:
    """
    @param s: A string
    @return: whether the string is a valid parentheses
    """
    def is_valid_parentheses(self, s: str) -> bool:
        # write your code here
        Outp=True
        iSum=0
        ParentVal={
            '(':1,
            ')':-1,
            '[':1,
            ']':-1,
            '{':1,
            '}':-1,
        }
        #for i in range(len(s)):
        for ch in s:
            #print(i,s[i],ParentVal.get(s[i]))
            #iSum += ParentVal.get(s[i])
            iSum += ParentVal.get(ch)
            if ( iSum != 0 and iSum != 1):
                Outp=False
                break
        if(iSum!=0):Outp=False
        return Outp

    def is_valid_parentheses2(self, s: str) -> bool:
        # write your code here
        stack=[]
        for ch in s:
            print(ch,stack)
            if ch=='{' or ch=='[' or ch=='(':
                stack.append(ch)
            else:
                if not stack:
                    return False
                if ch==']' and stack[-1]!='[' or ch==')' and stack[-1]!='(' or ch=='}' and stack[-1]!='{':
                    return False
                #print('stack[-1]:',stack[-1])
                stack.pop()
        return not stack

def main():
    S=Solution()
    #s='(){}[]{}}'; print(s,S.is_valid_parentheses(s))
    #s='(){}[]{}'; print(s,S.is_valid_parentheses(s))
    #s='(())'; print(s,S.is_valid_parentheses(s))
    #s='('; print(s,S.is_valid_parentheses(s))
    #s=')'; print(s,S.is_valid_parentheses(s))

    #s='(){}[]{}}'; print(s,S.is_valid_parentheses2(s))
    s='(()'; print(s,S.is_valid_parentheses2(s))

if __name__ == "__main__":
    main()

