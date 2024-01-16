#!/usr/bin/python3
i = 97
for i in range(97, 123):
    if chr(i) == 'e' or chr(i) == 'q':
        continue
    else:
        print(f"{chr(i)}", end="")
