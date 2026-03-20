def restore_health(current_health, potion):
    max_health = 100
    if current_health + potion > max_health:
        current_health = 100
    else:
        current_health += potion
    return current_health


print(restore_health( 90, 20))