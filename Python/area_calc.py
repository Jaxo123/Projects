from math import *
from time import *

def trapezoid(base1, base2, height):
    area_trap = 0
    if base1 < 0 or base2 < 0:
        print "One or both base lengths are invalid."
        return
    elif height < 0:
        print "Height is invalid"
        return
    else:
        area_trap += ((base1 + base2)/2)*height
        return area_trap

def rectangle(length, width):
    area_rect = 0
    if length < 0:
        print "Length is invalid"
        return
    elif width < 0:
        print "Width is invalid"
    else:
        area_rect += length * width
        return area_rect

def circle(radius):
    area_circ = 0
    if radius < 0:
        print "Radius is invalid."
        return
    else:
      area_circ += pi *  (radius ** 2)
      return area_circ

def triangle(base, height):
    area_tri = 0
    if height < 0:
        print "Height is invalid."
    elif base < 0:
        print "Base is invalid."
    else:
      area_tri += (base * height) / 2
      return area_tri

def n_gon(side, apothem, n_sides):
    area_gon = 0
    perim_gon = 0
    if side < 0:
        print "Side length is invalid"
        return
    elif apothem < 0:
        print "Apothem length is invalid."
        return
    elif n_sides < 3:
        print "Number of sides is invalid."
        return
    else:
        perim_gon += side * n_sides
        area_gon += (perim_gon * apothem) / 2
        return area_gon

def main_func():
    run = True
    while run is True:
        print "Select an option..."
        sleep(1)
        user_input = raw_input("1: regular polygon, 2: triangle, 3: parallelogram, 4: circle, 5: trapezoid, X: quit... ")
        if user_input == "3":
            length = int(raw_input("What is the rectangle's length? "))
            width = int(raw_input("What is the rectangle's width? "))
            print rectangle(length, width)
        elif user_input == "4":
            radius = int(raw_input("What is the circle's radius? "))
            print circle(radius)
        elif user_input == "2":
            base = int(raw_input("What is the trianle's base? "))
            height = int(raw_input("What is the triangle's height? "))
            print triangle(base, height)
        elif user_input == "1":
            side = int(raw_input("What is the polygon's side length? "))
            apothem = int(raw_input("What is the polygon's apothem? "))
            n_sides = int(raw_input("How many sides does the polygon have? "))
            print n_gon(side, apothem, n_sides)
        elif user_input == "5":
            base1 = int(raw_input("What is the length of one of the bases? "))
            base2 = int(raw_input("what is the length of the other base? "))
            height = int(raw_input("What is the trapazoid's height? "))
            print trapezoid(base1, base2, height)
        elif user_input.upper() == "X":
            run = False

main_func()
