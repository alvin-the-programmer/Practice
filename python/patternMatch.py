# pattern match, wildcards: '.' = 1 char, '?' = 1 or 0 chars

def patternMatch(p, s):
    j = 0
    for i in range(0, len(p)):
        if p[i] == '?':
            if patternMatch(p[i+1:], s[j:]):
                return True
        if j == len(s):
            return False
        if p[i] == '?' or p[i] == '.' or p[i] == s[j]:
            j += 1
        else:
            return False
    if len(p) == len(s):
        return True
    else:
        return False

print patternMatch('?????al?????in??', 'alvin')
print patternMatch('alvin?zablan', 'alvin zablan')
print patternMatch('alvin?zablan', 'alvinzablan')
print patternMatch('al?in', 'alvin')
print patternMatch('al.in', 'alvin')
print patternMatch('al.in.', 'alvin')
print patternMatch('al', 'alvin')
print patternMatch('alvin?', 'al')