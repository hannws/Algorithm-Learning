x, y, w, h = map(int, input().split())
dis_x = abs(x-w)
dis_y = abs(y - h)
small_x = dis_x if dis_x < x else x
small_y = dis_y if dis_y < y else y
print(small_x if small_x < small_y else small_y)