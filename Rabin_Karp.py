size=256
random_prime=15487469
def Rabin_Karp(text,pattern):
    pattern_length=len(pattern)
    pattern_hash=hash(pattern,pattern_length)
    text_length=len(text)
    start_points=[]
    if(text_length<pattern_length):
        start_points.append(text_length)
    text_hash=hash(text,pattern_length)
    if(pattern_hash==text_hash):
        start_points.append(0)
    for i in range(1,text_length-pattern_length+1):
        text_hash=hash_for_substr_with_next_symbol(pattern_length,text_hash,text[i+pattern_length-1],text[i-1])
        offset=i
        if pattern_hash==text_hash:
            if check_match(text,pattern,i):
                start_points.append(offset)
    return start_points


def hash(pattern,pattern_lenth):
    hash=0
    for j in range(pattern_lenth):
        hash=(size*hash+ord(pattern[j]))%random_prime
    return hash

def hash_for_substr_with_next_symbol(pattern_length,prev_hash,new_symbol,old_symbol):
    h=size**(pattern_length-1)%random_prime
    return ((prev_hash-ord(old_symbol)*h)*size+ord(new_symbol))%random_prime

def check_match(text, pattern, start_index):
    for i in range(len(pattern)):
        if pattern[i] != text[start_index + i]:
            return False
    return True

if __name__ == "__main__":
    text = input("Please write your text:") or "My cute hamsters want to eat 24/7"
    pattern=input("Please write a pattern to find in your text:") or "hamster"
    new_random_prime = input("Please input random prime number(2^n-1 the easiest way) if necessary:")
    if new_random_prime:
        random_prime=new_random_prime
    start_points=Rabin_Karp(text,pattern)
    end_points=[start_points[i]+len(pattern) for i in range(len(start_points))]
    for i in range(len(start_points)):
        result = ""
        print("Start position of found pattern in text is:"+ str(start_points[i])+" || End position of found pattern in text is:" + str(end_points[i]))
        for j in range(start_points[i], end_points[i]):
            result += text[j]
        print(result)
