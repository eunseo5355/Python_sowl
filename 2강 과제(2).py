"""
<문제>
2-1 공백2개를 1개로 바꾸고 :는 ,로 바꾼다. 단, 모든 함수는 1번만 사용가능
2-2 naMe를 소문자로 바꾸고 뒤에 있는 my를 My로 바꿔라.
2-3 주민번호를 뒷자리 1자리만 남기고 지워라.

a = 'My  naMe  is  Son  Chang  Ha:  my  pin  is  000125-3!!!!!!.'
출력 예: My name is Son Chang Ha, My pin is 000125-3.
"""

a = 'My  naMe  is  Son  Chang  Ha:  my  pin  is  000125-3!!!!!!.'
a = a.replace("  ", " ")
a = a.replace(":", ",")
a = a.replace("m", "M")
l = a.split(" ")
l[1] = l[1].lower()
l[9] = l[9].replace('!', '')
a = " ".join(l)
print(a)
