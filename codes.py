def hour_24(time):
    h, m, p = list(map(str, time[:-2].split(":"))) + [time[-2:].lower()]
    if p == "pm":
        h = str(int(h) + 12)
    else:
        h = str(int(h) % 12).zfill(2)  # Handle midnight (12:00am)
    return f"{h}:{m}"

result = hour_24("8:30am")
print(result)

hour_24("12:00pm")
            
            

def exactly_two_positive(a, b, c):
    positive_count = 0

    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    return positive_count == 2



def max_consonant_value(s):
    consonants = 'bcdfghjklmnpqrstvwxyz'
    max_value = 0
    current_value = 0

    for char in s:
        if char in consonants:
            current_value += ord(char) - ord('a') + 1
        else:
            current_value = 0

        max_value = max(max_value, current_value)

    return max_value
            
