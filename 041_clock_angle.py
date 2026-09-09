h, m = map(int, input().split())
h_angle = (h % 12) * 30 + m * 0.5
m_angle = m * 6
diff = abs(h_angle - m_angle)
print(min(diff, 360 - diff))
