def kmp_search(text, pattern):
    n, m = len(text), len(pattern)
    lps = [0] * m
    j = 0
    i = 1
    while i < m:
        if pattern[i] == pattern[j]:
            j += 1; lps[i] = j; i += 1
        elif j:
            j = lps[j - 1]
        else:
            lps[i] = 0; i += 1
    i = j = 0
    matches = []
    while i < n:
        if text[i] == pattern[j]:
            i += 1; j += 1
        if j == m:
            matches.append(i - j); j = lps[j - 1]
        elif i < n and text[i] != pattern[j]:
            if j: j = lps[j - 1]
            else: i += 1
    return matches

def rabin_karp(text, pattern, base=256, mod=101):
    n, m = len(text), len(pattern)
    h = pow(base, m - 1, mod)
    ph = th = 0
    matches = []
    for i in range(m):
        ph = (base * ph + ord(pattern[i])) % mod
        th = (base * th + ord(text[i])) % mod
    for i in range(n - m + 1):
        if ph == th and text[i:i+m] == pattern:
            matches.append(i)
        if i < n - m:
            th = (base * (th - ord(text[i]) * h) + ord(text[i + m])) % mod
    return matches

def suffix_array(s):
    return sorted(range(len(s)), key=lambda i: s[i:])

def demo():
    text = 'abcabcabcabc'
    pat = 'abcabc'
    print(f'KMP: {kmp_search(text, pat)}')
    print(f'Rabin-Karp: {rabin_karp(text, pat)}')
    sa = suffix_array('banana')
    print(f'SA of banana: {sa}')

if __name__ == '__main__':
    demo()
