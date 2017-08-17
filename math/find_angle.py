import math

if __name__ == "__main__":
    a = int(raw_input())
    b = int(raw_input())
    theta = math.degrees(math.atan2(a, b))
    print '{:.0f}°'.format(theta)
