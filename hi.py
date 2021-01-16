def con(s):
    h = {}
    x = []
    c = 0
    d = 0
    z = 0
    for i in s:
        if i not in h:
            h[i] = 1
        else:
            h[i] = h[i] + 1
    for i in range(len(s)):
    	d = 0
        c = s[i]
        h[s[i]] = False
        if h[s[i]] == False:
            continue
        else:
            for j in range(i+1,len(s)):
                if c + j in h:
                    if h[c+j] == 1:
                        h[c+j] = False
                    else:
                        h[c+j] -= 1
                        if h[c+j+1] == 1 and d+1 >= 3:
                            break
                    d += 1
                    
                else:
                    break
        if d >= 3:
        	z += 1
    if z >= 1:
    	return True

print(con([1,2,3,4,5]))