from config import * 
from colorPair_number_mapping import * 

def color_pair_to_string(major_color, minor_color):
  return f'{major_color} {minor_color}'

def print_reference_manual():
    print("\nReference Manual for telecommunications Cable Color Coding")
    print("===========================================")
    print("{:<6} | {:<6} | {:<6} | {:<16}".format("Pair #", "Major", "Minor", "Color Combination"))
    print("===========================================")
    
    # Generate and print each row
    total_pairs = len(MAJOR_COLORS) * len(MINOR_COLORS)
    for pair_number in range(1, total_pairs + 1):
        major, minor = get_color_from_pair_number(pair_number)
        color_combo = color_pair_to_string(major, minor)
        print("{:<6} | {:<6} | {:<6} | {:<16}".format(
            pair_number, major, minor, color_combo))
    
    print("===========================================")
    print(f"Total pairs: {total_pairs}")
    return total_pairs 