import re

s = "My name is Victor"
print(re.search(r"V....r$", s))

pattern = re.compile(r"^M.*Vi")
print(pattern.search(s))

# Full match
pattern = re.compile(r"^My.*\.$")
print(pattern.match("My name is V."))

pattern = re.compile(r"V....r")
print(pattern.findall("My name is Victor. Victor is Vipper"))


def check_email(email: str):
    email_pattern = re.compile(r"^[a-zA-Z0-9_.]+@[a-zA-Z0-9.]+\.[a-zA-Z0-9-.]+$")
    res = email_pattern.fullmatch(email)
    return email, "valid email" if res else "invalid email"


# print(check_email("victor.novik@mail.ru"))
# print(check_email("victor_novik@mail.com.ru"))
# print(check_email("victor_novik.mail.com.ru"))


def check_password(pwd: str):
    pwd_pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[_-]).{8,}$")
    res = pwd_pattern.fullmatch(pwd)
    return pwd, "valid password" if res else "invalid password"


print(check_password("ASw_1er$"))

pwd_pattern = re.compile(r"^[a-zA-Z0-9]{8}$")
print(pwd_pattern.fullmatch("ASD1234Q"))

