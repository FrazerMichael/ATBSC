import pyperclip, re

phoneNumbers = []
emailAddresses = []

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?            # area code
    (\s|-|\.)?                    # separator
    (\d{3})                       # first 3 digits
    (\s|-|\.)                     # separator
    (\d{4})                       # last 4 digits
    (\s*(ext|x|ext.)\s*\d{2,5})?  # extension
    )''', re.VERBOSE)

emailRegex = re.compile(r'''(
    ([a-zA-Z0-9!#$%&'*+-\/=?^_`{|]+)    # Recipent name
    (@)                                 # @
    ([a-zA-Z0-9-]+.[a-zA-Z0-9-]+)       # domain space
    (.[a-zA-Z0-9-]+)?                   # top level domain
)''', re.VERBOSE)


phoneTuple = phoneRegex.findall(pyperclip.paste())
emailTuple = emailRegex.findall(pyperclip.paste())

for each in phoneTuple:
    phoneNumbers.append(each[0])

for each in emailTuple:
    emailAddresses.append(each[0])

print(phoneNumbers)
print(emailAddresses)
