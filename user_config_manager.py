def add_setting(settings, key_value_pair):

    key, value = key_value_pair
    key = str(key).lower()
    value = str(value).lower()

    existing_keys = {str(existing_key).lower() for existing_key in settings}
    if key in existing_keys:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value
    return f"Setting '{key}' added with value '{value}' successfully!"
    
def update_setting(settings, key_value_pair):
    
    key, value = key_value_pair
    key = str(key).lower()
    value = str(value).lower()

    existing_key_map = {str(existing_key).lower(): existing_key for existing_key in settings}
    if key in existing_key_map:
        original_key = existing_key_map[key]
        # Keep dictionary key identity stable while updating with normalized value.
        settings[original_key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."


def delete_setting(settings, key):
    key = str(key).lower()

    existing_key_map = {str(existing_key).lower(): existing_key for existing_key in settings}
    if key in existing_key_map:
        original_key = existing_key_map[key]
        settings.pop(original_key)
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"


def view_settings(settings):
    if not settings:
        return "No settings available."

    lines = ["Current User Settings:"]
    for key, value in settings.items():
        lines.append(f"{str(key).capitalize()}: {value}")
    return "\n".join(lines) + "\n"


test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high",
}

#print(add_setting({'theme': 'light'}, ('volume', 'high')))
print(view_settings(test_settings))