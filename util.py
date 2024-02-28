# Method intakes a string formatted 'HH:MM:SS' and outputs total minutes
def to_minutes(hhmmss) -> int:
    hours, minutes, seconds = hhmmss.split(":")
    total_minutes = (int(hours) * 60) + int(minutes) + (int(seconds) / 60)
    return total_minutes
