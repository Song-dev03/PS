n, k = map(int, input().split())

belt_dura = list(map(int, input().split()))
robot_position = list()

cnt = 1
tmp = 1
while True:
    # step1
    belt_dura = [belt_dura[-1]] + belt_dura[:-1]
    robot_position = [x+1 for x in robot_position]
    if n-1 in robot_position:
        robot_position.remove(n-1)
    # print(belt_dura, robot_position)

    # step 2
    new_robot_position = []
    for x in list(robot_position):
        xx = x+1
        if belt_dura[xx] > 0 and xx not in robot_position:
            belt_dura[xx] -= 1
            new_robot_position.append(xx)
            robot_position.remove(x)
        else:
            new_robot_position.append(x)
    
    robot_position = new_robot_position

    if n-1 in robot_position:
        robot_position.remove(n-1)

    # print(belt_dura, robot_position)

    # step 3
    if belt_dura[0] > 0:
        belt_dura[0] -= 1
        robot_position.append(0)

    # print(belt_dura, robot_position)
    
    # step4
    if belt_dura.count(0) >= k:
        print(cnt)
        break

    cnt += 1