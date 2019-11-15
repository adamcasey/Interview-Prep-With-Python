# Reverse a string
class ReverseString:
    def __init__(self):
        self.string_to_reverse = ""
        #print(f"This is a test: {self.string_to_reverse}")
        print("This is a test: {}".format(self.string_to_reverse))

    def reverse_string(self, string_param):
        string_list = [None] * (len(string_param))
        for index, char in enumerate(string_param):
            self.string_to_reverse = char + self.string_to_reverse
            #print("index: {}".format(index))
            #print("char: {}".format(char))
            #print("len(string_param) - index: {}".format(len(string_param) - index))
            string_list[index] = string_param[len(string_param) - index - 1]
            #print(index)
        return (self.string_to_reverse, string_list)

if __name__ == '__main__':
    reverse_me = ReverseString()
    temp = reverse_me.reverse_string('Bacon')
    #print(reverse_me.reverse_string("Adam Casey"))
    print("temp[1]: {}".format("".join(temp[1])))
