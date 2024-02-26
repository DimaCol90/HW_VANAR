user = {
    'username': 'john',
    'online': True,
    'email': 'john@lucky.me',
    'rating': 1001,  

    'friends': [
        'marry',
        'candy',
        'peter'
    ]
}

add_friend = True

while add_friend:
    add_friend = input("Do you want to add more friends?(y/n) ") == 'y'
    if add_friend:
        new_friend = input("What is your new friend's name? ")
        user['friends'].append(new_friend)
    else:
        break

print(user['username'])
print(user['email'])

if user['rating'] == 0:
    print("No likes")
elif 1 <= user['rating'] <= 999:
    print(f"{user['rating']} likes")
elif 1000 <= user['rating'] <= 1000_000:
    print(f"{user['rating'] // 1000}k likes")
elif 1000_000 < user['rating'] <= 1000_000_000:
    print(f"{user['rating'] / 1000_000:.2f}M likes")
elif 1000_000_000 < user['rating'] <= 1000_000_000_000:
    print(f"{user['rating'] / 100_000_000_0:.2f}T likes")

print("FRIENDS LIST")
for friend in user['friends']:
    print(">>", friend)