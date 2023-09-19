def common_prefix(strings):
    if not strings:
        return ""
    strings.sort()
    first_str = strings[0]
    last_str = strings[-1]
    
    common = []
    for i in range(len(first_str)):
        if i < len(last_str) and first_str[i] == last_str[i]:
            common.append(first_str[i])
        else:
            break
    
    return ''.join(common)


strings = ["flower", "flour", "flourish"]
result = common_prefix(strings)
print(result) 
