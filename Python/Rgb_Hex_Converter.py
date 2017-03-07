#Converts RGB values to there hexadecimal equivilent#

def rgb_hex():
  invalid_msg = "Value entered is invalid: "
  red = int(raw_input("Enter value for RED: "))
  if 0 > red or red > 255:
    print invalid_msg
    return
  green = int(raw_input("Enter value for GREEN: "))
  if 0 > green or green > 255:
    print invalid_msg
    return
  blue = int(raw_input("Enter value for BLUE: "))
  if 0 > blue or blue > 255:
    print invalid_msg
    return
  val = (red << 16) + (green << 8) + (blue)
  print "%s" % (hex(val)[2:]).upper()

def hex_rgb():
  invalid_msg = "Value entered is invalid: "
  hex_val = raw_input("Enter a hexadecimal value: ")
  if len(hex_val) != 6:
    print invalid_msg
    return
  else:
   hex_val = int(hex_val, 16)
  two_hex_digits = 2**8
  blue = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  green = hex_val % two_hex_digits
  hex_val = hex_val >> 8
  red = hex_val % two_hex_digits
  print "Red: %s Green: %s Blue %s" % (red, green, blue)

def convert():
  while True:
    option = raw_input("Enter 1 to convert RGB to HEX. Enter 2 to convert HEX to RGB. Enter X to Exit: ")
    if option == "1":
      print "RGB to HEX..."
      rgb_hex()
    elif option == "2":
      print "HEX to RGB..."
      hex_rgb()
    elif option == "X" or option == "x":
      print "Goodbye."
      break
    else:
      print "Error."
convert()
