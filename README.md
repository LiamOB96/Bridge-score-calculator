    # Bridge Score Calculator
    #### Video Demo:  https://www.youtube.com/watch?v=OVGVKFEdunE
    #### Description:

    ## Introduction
    The scoring system in bridge is complicated. It is one of the reasons the game has a high barrier for entry.
    Even experienced players can struggle to remember scores for rare contracts.
    This project aimed to make the scoring of bridge quick, easy and accurate.

    ## Main code
    The code starts by taking in the result from the player. This input is then validated using three functions:
    - **validate_contract(contract)**: There are 5 contract denominations in bridge (the 4 suits and NoTrump), and contacts go from level 1 (7 tricks) to level 7 (13 tricks). This function checks the contract has a valid denomination and level. It then returns the suit, level and whether the contract is doubled or redoubled.
    - **validate_vulnerability(vulnerability)**: This ensures that the vulnerability input is either "V" (vulnerable) or "NV" (not vulnerable). It raises an error if the input is invalid.
    - **validate_tricks_made(tricks_made)**: Confirms that the number of tricks made is between 0 and 13. If the input is outside this range, an error is raised.

    Now the the score has to be calculated. This was done using one function:
    -**calculate_score**: This took into account a number of factors which is why this is complicated for a human:
    The denomination since suits and NT score differently.
    Whether the contract was doubled or redoubled.
    The bonus scores - part score, game, slam, or grand slam.

    The final score is then printed for the user to see.

    ## Test code
    This tests a range of possible outcomes, such as contracts making, going down, getting doubled/redoubled. It also checks some possible invalid inputs to see the correct error message appears.

    ## Design Choices
    The basic outline of the code was simple. The logic with all of the conditional statements in calculate_score needed many tries and tests to ensure it worked. Perhaps calculate_score could have been separated into more functions to simplify it and make it more readable.

    ## Challenges
    NT is two characters whereas all the other suits are one character. This meant extracting the suits had to be done over a range of index values. These also depended on whether there was a X or XX.
    Validating the contract input was more difficult than anticipated because of X and XX changing the length of inputs. For example, "3NT", "4H", "4HX" and "4HXX" all had to be split correctly to extract the level, suit, and whether it was doubled or redoubled. This was solved using if statements and indexing backwards to get the suit.
    NT scores 40 for first trick then 30 for subsequent tricks. This was solved by giving a separate value for trick one and then reducing the level by 1 to get the correct number of 30s for subsequent tricks.
    In bridge doubling doesn't just double the score. There is also an added bonus if make the contract or additional penalties if you go down. To solve this I had to first determine if the contract was made and then apply the correct logic.
    Game bonus is awarded for bidding at the 3 level in NT, 4 level in majors and 5 level in minors. This required a large if statement with or's to correctly award game bonuses or not.





