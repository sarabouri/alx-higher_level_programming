#!/usr/bin/python3
i = 97
for i in range(97, 123):
    if chr(i) == 101 and chr(i) == 113:
        continue
    else:
        print(f"{chr(i)}", end="")
