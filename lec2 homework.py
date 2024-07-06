# Q1- 169. Majority Element
def majority_element(nums):
    reqnum = nums[0]
    count = 1

    for num in nums[1:]:
        if reqnum == num:
            count += 1
        else:
            if count == 0:
                reqnum = num
                count = 1
            else:
                count -= 1
    majority_count = 0
    for num in nums:
        if num == reqnum:
            majority_count += 1

    if majority_count > len(nums) // 2:
        return reqnum
    else:
        return -1


nums = [3, 2, 3]
majority = majority_element(nums)
print("Majority element:", majority)


# Q2- 383. Ransom Note

def can_construct(ransomNote, magazine):
    m_char_count = {}
    for char in magazine:
        m_char_count[char] = m_char_count.get(char, 0) + 1

    for char in ransomNote:
        if char not in m_char_count or m_char_count[char] == 0:
            return False
        m_char_count[char] -= 1

    return True


ransomNote = "aa"
magazine = "aab"
can_form = can_construct(ransomNote, magazine)
print("Can ransom note be formed:", can_form)


# Q3- 387. First Unique Character in a String

def firstUniqChar(s):
    char_counts = {}
    for i, char in enumerate(s):
        char_counts[char] = char_counts.get(char, 0) + 1
    for i, char in enumerate(s):
        if char_counts[char] == 1:
            return i
    return -1


s = "leetcode"
firstIndex = firstUniqChar(s)
print("Index of first non-repeating character:", firstIndex)