
def palindrome(s):

    print("회문 체크용 문자열 : " + s)
    
    qu = []
    st = []
    
    for x in s:
        if x.isalpha():
            qu.append(x.lower())
            st.append(x.lower())
    
    while qu:
        if qu.pop(0) != st.pop():
            print(s + " : 회문아님!!")
            print("=" * 30)
            return False
    print(s + " : 회문임!!")
    print("=" * 30)
    return True


s = "madam, I'm Adam"
palindrome(s)

s = "eye"
palindrome(s)

s = "race car"
palindrome(s)

s = "my name is Hong"
palindrome(s)
