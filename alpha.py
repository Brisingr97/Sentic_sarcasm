import pickle,re

pickle_in = open("sentic.pickle","rb")
sentic = pickle.load(pickle_in)

user_input = input("Enter your input: ")
delimiters =  "but", ".", "however"
pattern = "|".join(map(re.escape, delimiters))
parsed_user_input = re.split(pattern,user_input)
#print(parsed_user_input);
data = []

for string in parsed_user_input:
    s = string.strip()
    if(len(s)==0):
    	continue;
    try:
        sent = sentic[s]
        data.append([sent[6],sent[7],s])
    except KeyError as k:
        print('NOT FOUND -',s)
print("");
for i in range(len(data)-3):
    if(data[i][0] is data[i+1][0] and data[i][0] is data[i+3][0] and data[i][0] is not data[i+2][0] and float(data[i+1][1])*float(data[i+2][1]) <= 0): 
    	# here less than zero defines the threshold which we will identify with the help of the survey.
        print('Sarcasm found at -',data[i+1][2],'and',data[i+2][2])
