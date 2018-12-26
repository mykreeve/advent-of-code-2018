
value = 0
appeared = []
previous = 0

while True:
  temp = value | 65536
  value = 10283511

  while True:
    value = (((value + (temp & 255)) & 16777215) * 65899) & 16777215

    if 256 > temp:
      if value not in appeared:
        appeared.append(value)
        previous = value
        break
      else:
        print("Answer to part two: " + str(previous))
        exit()
    else:
      temp = int(temp / 256)