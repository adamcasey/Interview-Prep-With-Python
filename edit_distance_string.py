# def say_hello():
#     print('Hello, World')

# for i in range(5):
#     say_hello()

def case_insensitive_compare(s1, s2):
    if len(s1) != len(s2):
        return False
    s1_iter = iter(s1)
    s2_iter = iter(s2)
    # '_' means it's a variable meant to be discarded
    for _ in range(len(s1)):
        # grab the char on each string
        s1_c = next(s1_iter)
        #print(f's1_c: {s1_c}')
        s2_c = next(s2_iter)
        #print(f's1_c: {s2_c}')

        if not s1_c.upper() == s2_c.upper():
            return False
        
    return True

print(case_insensitive_compare("adam", "ADAM"))
print(case_insensitive_compare("adam", "Casey"))
print(case_insensitive_compare("adam", ""))
print(case_insensitive_compare("", ""))
#print(case_insensitive_compare("", 0))