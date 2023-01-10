validator_message = ""


def validate_signup(data):
    global validator_message

    if not "first_name" in data or data["first_name"] == "":
        validator_message = "First name is required"
        return False

    if not "last_name" in data or data["last_name"] == "":
        validator_message = "Last name is required"
        return False

    if not "email" in data or data["email"] == "":
        validator_message = "Email is required"
        return False

    if not "phone" in data or data["phone"] == "":
        validator_message = "Email is required"
        return False

    if not "country" in data or data["country"] == "":
        validator_message = "Email is required"
        return False

    if not "password" in data or data["password"] == "":
        validator_message = "Password is required"
        return False

    return True


def validate_activate_account(data):
    global validator_message

    if not "token" in data or data["token"] == "":
        validator_message = "OTP token is required"
        return False

    return True


def validate_signin(data):
    global validator_message

    if not "email" in data or data["email"] == "":
        validator_message = "Email is required"
        return False

    if not "password" in data or data["password"] == "":
        validator_message = "Password is required"
        return False

    return True
