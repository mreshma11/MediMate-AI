import random



def simulate_bp():

    """Simulate blood pressure readings between 110–180"""

    return random.randint(110, 180)



def simulate_movement():

    """Randomly return 'moving' or 'no_movement'"""

    return random.choice(['moving', 'no_movement'])
