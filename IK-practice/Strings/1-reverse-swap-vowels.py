def reverse_vow(s):
    s_arr = list(s)
    vowels = ['a', 'e', 'i', 'o', 'u']
    l, r = 0, len(s_arr) - 1
    done = False

    while not done:
        if l <= r and s_arr[l] not in vowels:
            l += 1
            continue
        if l <= r and s_arr[r] not in vowels:
            r -= 1
            continue
        if l > r:
            done = True
        else:
            s_arr[l], s_arr[r] = s_arr[r], s_arr[l]
            l += 1
            r -= 1
    return ''.join(s_arr)




if __name__ == '__main__':
    assert reverse_vow("hello world") == "hollo werld"