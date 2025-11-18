# -----------------------------
# 2. BACKEND SIMULATION: LOGIN SYSTEM
# -----------------------------

# Fake user database
users = {
    "john": "1234",
    "alice": "5678",
    "admin": "admin123"
}

print("=== Login System ===")
username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful! Welcome,", username)
else:
    print("Login failed. Invalid username or password.")
