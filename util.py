# Method intakes a string formatted 'HH:MM:SS' and outputs total seconds
def to_seconds(hhmmss) -> int :
    hours, minutes, seconds = hhmmss.split(":")
    total_seconds = (int(hours) * 60 * 60) + (int(minutes) * 60) + int(seconds)
    return total_seconds