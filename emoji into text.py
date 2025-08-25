import demoji

import demoji

import demoji

text = "I love 🍕, enjoy 🎶, and travel ✈️ with friends 😂."

# 1. Find all emojis with their descriptions (dict)
print("findall:", demoji.findall(text))

# 2. Find all emojis with their descriptions (list)
print("findall_list:", demoji.findall_list(text))

# 3. Replace emojis with blank (remove them)
print("replace:", demoji.replace(text, ""))

# 4. Replace emojis with their description text
print("replace_with_desc:", demoji.replace_with_desc(text))



