encoded = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
k='m'
o='q'
e='g'
# +2
encoded = encoded.lower()
str1 = 'abcdefghijklmnopqrstuvwxyz'
str2 = str1[2:] + 'ab'
table = ''.maketrans(str1,str2)
decoded = encoded.translate(table)

sol = "map".translate(table)
print(decoded)
print(sol)