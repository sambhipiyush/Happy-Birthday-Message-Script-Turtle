#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun  6 16:11:50 2020

@author: Piyush Sambhi
 (                          (                              
 )\ )                   )   )\ )                 )    )    
(()/((  (      (     ( /(  (()/(    )    )    ( /( ( /((   
 /(_))\ )\ )  ))\ (  )\())  /(_))( /(   (     )\()))\())\  
(_))((_|()/( /((_))\((_)\  (_))  )(_))  )\  '((_)\((_)((_) 
| _ \(_))(_)|_))(((_) |(_) / __|((_)_ _((_)) | |(_) |(_|_) 
|  _/| | || | || (_-< ' \  \__ \/ _` | '  \()| '_ \ ' \| | 
|_|  |_|\_, |\_,_/__/_||_| |___/\__,_|_|_|_| |_.__/_||_|_| 
        |__/                                               

@Contact-Details:
    Email: piyush.sambhi07@icloud.com
"""
import turtle

bgcolor = 'black'
btm_lines_color='white'
cake_color = 'white'
candel_colors = ["red", "blue", "yellow", "green", "purple"]
main_text_color = "orange"
main_text = "Happy Birthday !!"
final_pen_color = bgcolor

font_type = "Comic Sans MS"
font_size = 30

# sets background
bg = turtle.Screen()
bg.bgcolor(bgcolor)

# Bottom Line 1
turtle.penup()
turtle.goto(-170,-180)
turtle.color(btm_lines_color)
turtle.pendown()
turtle.forward(350)

# Mid Line 2
turtle.penup()
turtle.goto(-160,-150)
turtle.color(btm_lines_color)
turtle.pendown()
turtle.forward(300)

# First Line 3
turtle.penup()
turtle.goto(-150,-120)
turtle.color(btm_lines_color)
turtle.pendown()
turtle.forward(250)

# Cake
turtle.penup()
turtle.goto(-100,-100)
turtle.color(cake_color)
turtle.begin_fill()
turtle.pendown()
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.left(90)
turtle.forward(140)
turtle.left(90)
turtle.forward(95)
turtle.end_fill()

# Candles
turtle.penup()
turtle.goto(-90,0)
turtle.color(candel_colors[0])
turtle.left(180)
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-60,0)
turtle.color(candel_colors[1])
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(-30,0)
turtle.color(candel_colors[2])
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(0,0)
turtle.color(candel_colors[3])
turtle.pendown()
turtle.forward(20)

turtle.penup()
turtle.goto(30,0)
turtle.color(candel_colors[4])
turtle.pendown()
turtle.forward(20)

# Decoration
colors = ["red", "orange", "yellow", "green", "blue", "purple", "black"]
turtle.penup()
turtle.goto(-40,-50)
turtle.pendown()

for each_color in colors:
    angle = 360 / len(colors)
    turtle.color(each_color)
    turtle.circle(10)
    turtle.right(angle)
    turtle.forward(10)

# Happy Birthday message
turtle.penup()
turtle.goto(-150, 50)
turtle.color(main_text_color)
turtle.pendown()
turtle.write(main_text, move=False, align="left", font=(font_type, font_size, "normal"))
turtle.color(final_pen_color)

