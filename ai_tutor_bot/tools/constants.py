PHYSICS_CONSTANTS = {
    "speed of light": "3.0 x 10^8 m/s",
    "gravitational constant": "6.674 x 10^-11 N·m²/kg²",
}

def lookup_constant(term: str) -> str:
    return PHYSICS_CONSTANTS.get(term.lower(), "Constant not found")