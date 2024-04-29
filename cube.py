import math
import os
import time

width, height = 160, 44
z_buffer = [0.0] * (width * height)
buffer = [' '] * (width * height)
background_ascii_code = '.'
distance_from_cam = 100
horizontal_offset = 0
k1 = 40
increment_speed = 0.6

def calculate_x(i, j, k):
    return j * math.sin(A) * math.sin(B) * math.cos(C) - k * math.cos(A) * math.sin(B) * math.cos(C) + j * math.cos(A) * math.sin(C) + k * math.sin(A) * math.sin(C) + i * math.cos(B) * math.cos(C)

def calculate_y(i, j, k):
    return j * math.cos(A) * math.cos(C) + k * math.sin(A) * math.cos(C) - j * math.sin(A) * math.sin(B) * math.sin(C) + k * math.cos(A) * math.sin(B) * math.sin(C) - i * math.cos(B) * math.sin(C)

def calculate_z(i, j, k):
    return k * math.cos(A) * math.cos(B) - j * math.sin(A) * math.cos(B) + i * math.sin(B)

def calculate_for_surface(cube_x, cube_y, cube_z, ch):
    global x, y, z, ooz, xp, yp, idx
    x = calculate_x(cube_x, cube_y, cube_z)
    y = calculate_y(cube_x, cube_y, cube_z)
    z = calculate_z(cube_x, cube_y, cube_z) + distance_from_cam
    ooz = 1 / z
    xp = int(width / 2 + horizontal_offset + k1 * ooz * x * 2)
    yp = int(height / 2 + k1 * ooz * y)
    idx = xp + yp * width
    if 0 <= idx < width * height and ooz > z_buffer[idx]:
        z_buffer[idx] = ooz
        buffer[idx] = ch

A, B, C = 0, 0, 0

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    buffer = [' '] * (width * height)
    z_buffer = [0.0] * (width * height)
    cube_width = 20
    horizontal_offset = -2 * cube_width
    for cube_x in range(-cube_width, cube_width):
        for cube_y in range(-cube_width, cube_width):
            calculate_for_surface(cube_x, cube_y, -cube_width, '@')
            calculate_for_surface(cube_width, cube_y, cube_x, '$')
            calculate_for_surface(-cube_width, cube_y, -cube_x, '~')
            calculate_for_surface(-cube_x, cube_y, cube_width, '#')
            calculate_for_surface(cube_x, -cube_width, -cube_y, ';')
            calculate_for_surface(cube_x, cube_width, cube_y, '+')

    cube_width = 10
    horizontal_offset = 1 * cube_width
    for cube_x in range(-cube_width, cube_width):
        for cube_y in range(-cube_width, cube_width):
            calculate_for_surface(cube_x, cube_y, -cube_width, '@')
            calculate_for_surface(cube_width, cube_y, cube_x, '$')
            calculate_for_surface(-cube_width, cube_y, -cube_x, '~')
            calculate_for_surface(-cube_x, cube_y, cube_width, '#')
            calculate_for_surface(cube_x, -cube_width, -cube_y, ';')
            calculate_for_surface(cube_x, cube_width, cube_y, '+')

    cube_width = 5
    horizontal_offset = 8 * cube_width
    for cube_x in range(-cube_width, cube_width):
        for cube_y in range(-cube_width, cube_width):
            calculate_for_surface(cube_x, cube_y, -cube_width, '@')
            calculate_for_surface(cube_width, cube_y, cube_x, '$')
            calculate_for_surface(-cube_width, cube_y, -cube_x, '~')
            calculate_for_surface(-cube_x, cube_y, cube_width, '#')
            calculate_for_surface(cube_x, -cube_width, -cube_y, ';')
            calculate_for_surface(cube_x, cube_width, cube_y, '+')

    for k in range(width * height):
        print(buffer[k], end='\n' if k % width == width - 1 else '')

    A += 0.05
    B += 0.05
    C += 0.01
    time.sleep(0.016)
