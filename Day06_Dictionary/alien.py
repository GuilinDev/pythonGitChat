# 6.1 6.2
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])
print("you just earned " + str(alien_0["points"]) + " points.")

alien_1 = {}
alien_0['x_position'] = 0
alien_0['y_position'] = 25
alien_1['x_position'] = 0
alien_1['y_position'] = 25
print(alien_0)
print(alien_1)
alien_0['color'] = 'yellow'
print(alien_0)

alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Origianl x-position: " + str(alien_2['speed']))

# 向右移动外星人
# 根据外星人的当前速度决定移动多远
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

# new position = old postion + increment
alien_2['x_position'] += x_increment
print("New x-position: " + str(alien_2['x_position']))

# re define
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = []
for alien_number in range(30):
    new_alien = {'color':'green', 'points': '5', 'speed': 'slow'}
    aliens.append(new_alien)
for alien in aliens[0:3]:
    print(alien)
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
print("The total number of aliens is: " + str(len(aliens)))
for alien in aliens[:5]:
    print(alien)