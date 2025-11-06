
from __future__ import annotations
from collections import deque, defaultdict
from typing import List, Tuple


def max_in_list(nums: List[int]) -> int:
    
    m = nums[0]
    for x in nums[1:]:
        if x > m:
            m = x
    return m

# 2. String'i Ters Çevirme

def reverse_string(s: str) -> str:
    return s[::-1]

# 3. Faktöriyel Hesaplamaa

def factorial(n: int) -> int:
    if n < 0:
        raise ValueError("Negatif sayının faktöriyeli tanımsız.")
    result = 1
    for k in range(2, n + 1):
        result *= k
    return result

# 4. Listedeki Çift Sayıları Filtreleme

def filter_evens(nums: List[int]) -> List[int]:
    return [x for x in nums if x % 2 == 0]

# 5. İki Listenin Birleşimi ve Tekilleştirilmesi

def union_unique(a: List[int], b: List[int]) -> List[int]:
    
    return sorted(set(a) | set(b))

# 6. Palindrom Kontrolü (boşluk ve büyük/küçük harf göz ardı)

def is_palindrome(s: str) -> bool:
    filtered = [ch.lower() for ch in s if ch.isalnum()]
    i, j = 0, len(filtered) - 1
    while i < j:
        if filtered[i] != filtered[j]:
            return False
        i += 1
        j -= 1
    return True

# 7. EBOB (GCD) - Öklid Algoritması

def gcd(a: int, b: int) -> int:
    while b:
        a, b = b, a % b
    return abs(a)

# 8. Anagram Kontrolü (boşluk ve büyük/küçük harf göz ardı)

def are_anagrams(s: str, t: str) -> bool:
    def norm(x: str) -> str:
        return ''.join(sorted(ch.lower() for ch in x if ch.isalnum()))
    return norm(s) == norm(t)

# 9. Listedeki Eksik Sayıyı Bulma (1..N veya 0..N varyantını da destekleyelim)

def missing_number(nums: List[int]) -> int:
    
    if not nums:
        raise ValueError("Liste boş olmamalı")
    n = len(nums)
    
    min_v, max_v = min(nums), max(nums)
    if min_v == 0 and max_v == n:
       
        expected = n * (n + 1) // 2
        return expected - sum(nums)
    else:
        
        N = max_v
        expected = N * (N + 1) // 2
        return expected - sum(nums)

# 10. Listeyi k adımı kadar sağa döndürme

def rotate_right(arr: List[int], k: int) -> List[int]:
    if not arr:
        return []
    k %= len(arr)
    if k == 0:
        return arr[:]
    return arr[-k:] + arr[:-k]

# 11. İki Sıralı Listenin Medyanı (O(log(m+n)))

def median_two_sorted_arrays(a: List[int], b: List[int]) -> float:
    
    if len(a) > len(b):
        a, b = b, a
    m, n = len(a), len(b)
    if m == 0 and n == 0:
        raise ValueError("İki liste aynı anda boş olamaz")
    imin, imax = 0, m
    half = (m + n + 1) // 2
    import math
    while imin <= imax:
        i = (imin + imax) // 2
        j = half - i
        a_left = a[i - 1] if i > 0 else -math.inf
        a_right = a[i] if i < m else math.inf
        b_left = b[j - 1] if j > 0 else -math.inf
        b_right = b[j] if j < n else math.inf
        if a_left <= b_right and b_left <= a_right:
            if (m + n) % 2 == 1:
                return float(max(a_left, b_left))
            return (max(a_left, b_left) + min(a_right, b_right)) / 2.0
        elif a_left > b_right:
            imax = i - 1
        else:
            imin = i + 1
    raise RuntimeError("Medyan bulunamadı (beklenmeyen durum)")

# 12. En Uzun Palindromik Alt String (O(n^2), merkez genişletme)

def longest_palindrome(s: str) -> str:
    if not s:
        return ""
    start, end = 0, 0
    def expand(l: int, r: int) -> Tuple[int, int]:
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return l + 1, r - 1
    for i in range(len(s)):
        l1, r1 = expand(i, i)
        l2, r2 = expand(i, i + 1)
        if r1 - l1 > end - start:
            start, end = l1, r1
        if r2 - l2 > end - start:
            start, end = l2, r2
    return s[start:end + 1]

# 13. Kelime Merdiveni (Word Ladder) - BFS

def word_ladder_length(begin: str, end: str, word_list: List[str]) -> int:
    word_set = set(word_list)
    if end not in word_set:
        return 0
    # Pattern -> kelimeler (hız için ön-işleme)
    patterns = defaultdict(list)
    L = len(begin)
    for w in word_set:
        for i in range(L):
            patterns[w[:i] + '*' + w[i+1:]].append(w)
    q = deque([(begin, 1)])
    visited = {begin}
    while q:
        word, dist = q.popleft()
        if word == end:
            return dist
        for i in range(L):
            pat = word[:i] + '*' + word[i+1:]
            for nei in patterns.get(pat, []):
                if nei not in visited:
                    visited.add(nei)
                    q.append((nei, dist + 1))
           
    return 0

# 14. Maksimum Alt Dizi Toplamı (Kadane)

def max_subarray_sum(nums: List[int]) -> int:
    best = cur = nums[0]
    for x in nums[1:]:
        cur = max(x, cur + x)
        best = max(best, cur)
    return best

# 15. Birleştirme Aralıkları (Merge Intervals)

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0][:]]
    for s, e in intervals[1:]:
        last = merged[-1]
        if s <= last[1]:
            last[1] = max(last[1], e)
        else:
            merged.append([s, e])
    return merged


# --- Hızlı Örnek Çalıştırmalar ---
if __name__ == "__main__":
    print("1.", max_in_list([1,2,3,4,5]))                 
    print("2.", reverse_string("Python"))                 
    print("3.", factorial(5))                             
    print("4.", filter_evens([1,2,3,4,5,6]))             
    print("5.", union_unique([1,2,3], [3,4,5]))          
    print("6.", is_palindrome("A man a plan a canal Panama")) 
    print("7.", gcd(54, 24))                              
    print("8.", are_anagrams("listen", "silent"))        
    print("9.", missing_number([1,2,4,5]))                
    print("10.", rotate_right([1,2,3,4,5], 2))            
    print("11.", median_two_sorted_arrays([1,3], [2]))   
    print("12.", longest_palindrome("babad"))            
    print("13.", word_ladder_length("hit", "cog", ["hot","dot","dog","lot","log","cog"])) 
    print("14.", max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4])) 
    print("15.", merge_intervals([[1,3],[2,6],[8,10],[15,18]])) 