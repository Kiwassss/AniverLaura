import os
import qrcode

# Base URL for generating QR codes
base_url = "https://kiwassss.github.io/AniverLaura"

# List of guests
guests = [
    "Ana", "Bruno", "Camila", "Daniel", "Eduardo", "Fernanda", "Gabriel", "Helena", "Igor", "Juliana",
    "Karina", "Lucas", "Mariana", "Natan", "Olivia", "Paulo", "Quesia", "Rafael", "Sabrina", "Tiago",
    "Ursula", "Vanessa", "Wagner", "Xuxa", "Yasmin", "Zeca", "Alice", "Bernardo", "Clara", "Diego",
    "Elisa", "Felipe", "Giovana", "Hugo", "Isabela", "Joao", "Kelly", "Leonardo", "Mirela", "Nicolas",
    "Otavio", "Priscila", "Rodrigo", "Samara", "Tadeu", "Ulisses", "Vitoria", "William", "YasminS",
    "Zuleica", "Arthur", "Bianca", "Caio", "Duda", "Enzo", "Flavia", "Gustavo", "Heloisa", "Ingrid", "Jorge"
]

# Directory to save QR code images
output_dir = "qrcodes"
os.makedirs(output_dir, exist_ok=True)

for guest in guests:
    # Create URL with guest name
    guest_url = f"{base_url}/{guest.replace(' ', '%20')}"
    # Generate QR code
    qr = qrcode.make(guest_url)
    # Save QR code image
    filename = f"{guest.replace(' ', '_')}.png"
    filepath = os.path.join(output_dir, filename)
    qr.save(filepath)
    print(f"QR code generated for {guest}: {filepath}")
