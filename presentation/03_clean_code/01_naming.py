# === Variable names ===

t = 10

t = 10  # time

time = 10

elapsed_time = 10

elapsed_time_in_days = 10


# funcition naming
def allowed(a, status):
    if a >= 18 and not status:
        return True
    else:
        return False


def is_allowed_into_pub(age_years: int, is_drunk: bool) -> bool:
    legal_age = 18
    if age_years >= legal_age and not is_drunk:
        return True
    else:
        return False
