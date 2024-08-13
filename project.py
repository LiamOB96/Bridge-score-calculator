def main():
    # Get all details of the result
    contract = input("Contract: ")
    vulnerability = input("Vulnerability (V or NV): ")
    tricks_made = int(input("Tricks made: "))
    # Validate inputs and unpack results
    level, suit, doubled, redoubled = validate_contract(contract)
    vulnerability = validate_vulnerability(vulnerability)
    tricks_made = validate_tricks_made(tricks_made)

    # Calculate the score based on validated inputs
    score = calculate_score(level, suit, doubled, redoubled, vulnerability, tricks_made)

    print(f"Score: {score}")


def validate_contract(contract):
    valid_suits = ["C", "D", "H", "S", "NT"]
    valid_levels = ["1", "2", "3", "4", "5", "6", "7"]


    if contract.endswith("XX"):
        redoubled = True
        doubled = False
        level = contract[0]
        suit = contract[1:-2]

    elif contract.endswith("X"):
        redoubled = False
        doubled = True
        level = contract[0]
        suit = contract[1:-1]

    else:
        redoubled = False
        doubled = False
        level = contract[0]
        suit = contract[1:]

    if level not in valid_levels:
        raise ValueError("Invalid contract level")
    if suit not in valid_suits:
        raise ValueError("Invalid suit")

    return level, suit, doubled, redoubled

def validate_vulnerability(vulnerability):
    valid_vulnerabilities = ["V", "NV"]

    if vulnerability not in valid_vulnerabilities:
        raise ValueError("Invalid vulnerability")

    return vulnerability

def validate_tricks_made(tricks_made):
    if tricks_made < 0 or tricks_made > 13:
        raise ValueError("Invalid number of tricks")

    return tricks_made


def calculate_score(level, suit, doubled, redoubled, vulnerability, tricks_made):

    original_level = int(level)
    level = int(level)
    tricks_made = int(tricks_made)
    tricks_required = level + 6

    #Determine score per trick
    if suit in ["C", "D"]:  # Minor suits
        points_per_trick = 20
        score = points_per_trick*level
    elif suit in ["H", "S"]:  # Major suits
        points_per_trick = 30
        score = points_per_trick*level
    else:  # No Trump (NT)
        trick_one = 40
        level -= 1
        points_per_trick = 30  # First trick in NT
        score = trick_one + points_per_trick*level

    #Adjust for double or redouble
    if doubled:
        score *= 2
        insult_bonus = 50
    elif redoubled:
        score *= 4
        insult_bonus = 100
    else:
        insult_bonus = 0

    #if contract is made
    if tricks_made >= tricks_required:
    #Overtricks
        if tricks_made > tricks_required:
            overtricks = tricks_made - tricks_required
            if doubled:
                if vulnerability == "V":
                    score += overtricks * 200
                else:
                    score += overtricks * 100
            elif redoubled:
                if vulnerability == "V":
                    score += overtricks * 400
                else:
                    score += overtricks* 200
            else:
                score += overtricks * points_per_trick

        # Check for game bonus
        if (suit in ["H", "S"] and original_level >= 4) or \
           (suit in ["C", "D"] and original_level >= 5) or \
           (suit == "NT" and original_level >= 3):
            game_bonus = 500 if vulnerability == "V" else 300
            score += game_bonus

        else:
            # Part-score bonus
            part_score_bonus = 50
            score += part_score_bonus

        score += insult_bonus

        # Check for slam bonuses
        if original_level == 6:
            slam_bonus = 750 if vulnerability == "V" else 500
            score += slam_bonus
        elif original_level == 7:
            grand_slam_bonus = 1500 if vulnerability == "V" else 1000
            score += grand_slam_bonus

    #Undertricks
    elif tricks_made < tricks_required:
        undertricks = tricks_required - tricks_made
        if doubled:
            if vulnerability == "V":
                score = -(200 + 300 * (undertricks - 1))
            else:
                score = -(100 + 200 * (undertricks - 1))
        elif redoubled:
            if vulnerability == "V":
                score = -(400 + 600 * (undertricks - 1))
            else:
                score = -(200 + 400 * (undertricks - 1))
        else:
            if vulnerability == "V":
                score = -(100 * undertricks)
            else:
                score = -(50 * undertricks)

    return score



if __name__ == "__main__":
    main()
