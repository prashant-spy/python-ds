def longest_unique_substring(string):
    n = len(string)
    maxlen = 0
    visited = [False] * 256
    l = 0
    r = 0
    while r < n:
        if visited[ord(string[r])]:
            while visited[ord(string[r])]:
                visited[ord(string[l])] = False
                l += 1
        visited[ord(string[r])] = True
        maxlen = max(maxlen,r-l+1)
        r += 1
    return maxlen


if __name__ == '__main__':
    string = "geeksforgeek"
    print(longest_unique_substring(string))
