#call by value

string = "jayvin gohel"
def test(string):

        string = "jayvin gohel"
        print("inside function:",string)

        
#  drives code
test(string)
print("outside function:",string)
