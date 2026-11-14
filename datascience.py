from collections import Counter
data = {7,3,4,1,2,6}
count = Counter(data)
max_count = max(count.values())
modes  = [k for k,v in count.items()if v == max_count]
if len(modes) == len(data):
    mode = None
else:
    modes = modes
print("Mode:",modes)
