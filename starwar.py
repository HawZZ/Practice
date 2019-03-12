#starwar.py


def b(hp):
    if hp%3 !=0:
        return 1
    else:
        return 0
'''judge if dmg over'''
enemy = [{'hp': 10, 'ap': 2},
         {'hp': 20, 'ap': 1},
         {'hp': 8, 'ap': 6},
         {'hp': 1, 'ap': 1}]
'''enter enemy status'''
for i in range(4):
    enemy[i].setdefault('ratio', enemy[i]['ap']/(int(enemy[i]['hp']/3)+b(enemy[i]['hp'])))
'''calculate ratio : ap/（hp//3+if hp%3 !=0 return 1）'''
print(enemy)
'''checkpoint'''
dmg = 0
ratio = 0
n=0
'''initialization'''
while not ratio < 0:
    ratio = -1
    for i in range(4):
        if ratio < enemy[i]['ratio']:
            ratio = enemy[i]['ratio']
            j=i
    '''find max ratio to aim a enemy'''
    while enemy[j]['hp']>0:
        enemy[j]['hp'] = enemy[j]['hp']-3
        for k in range(4):
            if k != j:
                enemy[k]['hp'] = enemy[k]['hp']-0.15
        for l in range(4):
            if enemy[l]['hp']>0:
                dmg = dmg + enemy[l]['ap']
    '''calculate hp changing and dmg summary'''
    for k in range(4):
        if enemy[k]['hp'] > 0:
            enemy[k]['ratio'] = enemy[k]['ap']/(int(enemy[k]['hp']/3)+b(enemy[k]['hp']))
        else:
            enemy[k]['ratio'] = -1
    '''renew the ratio'''
    n = n+1
    if n <= 4:
        print ('Enemy ',j+1,' will be killed at No. ', n)
print ('Luke takes minimum damage is ',dmg)
