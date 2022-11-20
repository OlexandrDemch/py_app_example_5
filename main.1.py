try:
    print(((2745 / 60)*100) % 100)
    user_seconds = int(input('input seconds->'))
    all_seconds_per_day = 24 * 3600
    if all_seconds_per_day < user_seconds:
        raise Exception('All seconds per day is less then user seconds!')
    diff_seconds = all_seconds_per_day - user_seconds
    print('#>----------<Menu>---------<#')
    print('|  h - Seconds in hour      |')
    print('|  m - Seconds in minutes   |')
    print('|  s - Seconds              |')
    print('#>-------------------------<#')
    action = input('action->')
    if action == 'h':
        print(f'Hours to midnight = {int(diff_seconds/3600)}h')
    elif action == 'm':
        print(f'Minutes to midnight = {int(diff_seconds/60)}m')
    elif action == 's':
        print(f'Seconds to midnight = {int(diff_seconds/3600)} s')
    else:
        h = int(diff_seconds/3600)
        m = int((diff_seconds / 3600)/60)
        s = int((diff_seconds % 3600)%60)
except ValueError as vl_ex:
    print(f'ValueError: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
