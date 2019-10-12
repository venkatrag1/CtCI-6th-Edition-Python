

#def LCSubStr(X, Y, m, n):


def naive_search(pat, txt):
    match_ind = list()
    M = len(pat)
    N = len(txt)
    for i in range(N-M+1):
        if txt[i] == pat[0]:
            j, k = i+1, 1
            while j < N and k < M and txt[j] == pat[k]:
                j += 1
                k += 1
            if k == M:
                match_ind.append(i)
    return match_ind




# Driver Code
if __name__ == '__main__':
    txt = "AABAACAADAABAAABAA"
    pat = "AABA"
    search = naive_search
    print(search(pat, txt))
