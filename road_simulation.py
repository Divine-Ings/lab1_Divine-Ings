SEGMENT_M = 100
ZEBRA_WAIT = 15
ACCELERATION = 5
BRAKING = 20
START_NAME = "ALU Rwanda"
END_NAME = "Convention Center"

# Each item in the road list is ONE segment of road. On the screen each segment is 100 m long
road = [
    "60", "road", "road", "road", "zebra", "road", "road",
    "80", "road", "road", "road", "road", "road", "road",
    "bus", "road", "road", "bus", "road", "road","road",
    "60", "road", "road", "road", "road","80", "road", 
    "road","zebra", "road", "road","road", "road",
]



# TODO 1: Return True only if sign is text AND is "bus", "zebra",
# or a number from 20 to 100 written as text (e.g. "80"). Otherwise False.
def is_valid_sign(sign):
    # must be text first
    if type(sign) != str:
        return False

    if sign == "bus" or sign == "zebra":
        return True

    # check if it is a speed number written as text
    try:
        number = int(sign)
        if number >= 20 and number <= 100:
            return True
        else:
            return False
    except:
        return False


# TODO 2: Return "bus", "zebra", "speed" (a number) or "road" (anything else).
def get_sign_type(sign):
    if sign == "bus":
        return "bus"
    elif sign == "zebra":
        return "zebra"
    else:
        # try to see if it is a speed limit
        try:
            number = int(sign)
            if number >= 20 and number <= 100:
                return "speed"
            else:
                return "road"
        except:
            return "road"



# TODO 3: If the sign is a speed sign, return its number as an int. Else return current_limit.
def get_speed_limit(sign, current_limit):
    if get_sign_type(sign) == "speed":
        return int(sign)
    else:
        return current_limit


# TODO 4: Return 0 while stop_timer is above 0, otherwise return limit.
def get_target_speed(limit, stop_timer):
    if stop_timer > 0:
        return 0
    else:
        return limit


# TODO 5: Move speed ONE step towards target and return it.
# Below target: add ACCELERATION (never go above target).
# Above target: subtract BRAKING (never go below target).
def adjust_speed(speed, target):
    if speed < target:
        speed = speed + ACCELERATION
        # do not go past the target
        if speed > target:
            speed = target
    elif speed > target:
        speed = speed - BRAKING
        # do not go below the target
        if speed < target:
            speed = target
    return speed


# TODO 6: Use a loop. Return (speed_signs, zebras, buses).
def count_signs(road_list):
    speed_signs = 0
    zebras = 0
    buses = 0

    for sign in road_list:
        kind = get_sign_type(sign)
        if kind == "speed":
            speed_signs = speed_signs + 1
        elif kind == "zebra":
            zebras = zebras + 1
        elif kind == "bus":
            buses = buses + 1

    return (speed_signs, zebras, buses)



# TODO 7: Keep asking until the user types a whole number from low to high.
# Use try/except for text that is not a number. Return the number as an int.
def ask_for_number(question, low, high):
    while True:
        answer = input(question)
        try:
            number = int(answer)
            if number >= low and number <= high:
                return number
            else:
                print("  Please enter a whole number from", low, "to", high)
        except:
            print("  That is not a whole number. Try again.")


# TODO 8: Insert sign at position. Return False if position is not from 0 to len(road_list).
# Otherwise insert and return True.
def insert_sign(road_list, sign, position):
    if position < 0 or position > len(road_list):
        return False
    road_list.insert(position, sign)
    return True


# TODO 9: Replace the sign at index with a new sign. Return False if index is not
# from 0 to len(road_list) - 1. Otherwise replace it and return True.
def replace_sign(road_list, sign, index):
    if index < 0 or index > len(road_list) - 1:
        return False
    road_list[index] = sign
    return True


# TODO 10: Summarise the journey. Use a loop to count the signs we pass
# (every segment that is not "road"). Return four values:
# (signs_passed, length_m, START_NAME, END_NAME)
# length_m is the number of segments times SEGMENT_M.
def get_journey_summary(road_list):
    signs_passed = 0

    for sign in road_list:
        if sign != "road":
            signs_passed = signs_passed + 1

    length_m = len(road_list) * SEGMENT_M
    return (signs_passed, length_m, START_NAME, END_NAME)


if __name__ == "__main__":
    import sys
    import transit_program
    transit_program.run(sys.modules[__name__])
