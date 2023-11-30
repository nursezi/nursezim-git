def find_boxes():
    total_weight = 713
    #there are 3 boxes, each of them have own weight, and when we sum them, we should total weight
    boxes_weights = [0, 0, 0]
    kilometer_marks = [0, 0, 0]

    while True:
        print("\nEnter the kilometer mark for each box:")

        for i in range(3):
            kilometer_marks[i] = int(input(f"Box {i + 1}: "))

        for i in range(3):
            if boxes_weights[i] == 0 or kilometer_marks[i] == 0:
                boxes_weights[i] = int(input(f"Enter the weight for Box {i + 1}: "))

        if sum(boxes_weights) == total_weight:
            print("\nCongratulations! You found all the boxes.")
            break
        else:
            print("\nOops! The total weight is not 713. Try again.")

if __name__ == "__main__":
    print("Welcome to the Martian Cargo Finder!")
    print("You need to enter kilometer marks and weights for each box.")

    find_cargo()

    print("\nThank you for helping the Martians!")
    print("They are impressed with your skills and may contact you for an intergalactic project.")
