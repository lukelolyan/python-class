frequency = float(input("Enter the frequency of the radiation (Hz): "))

if frequency < 3e9:
    print("Radio waves")
elif 3e9 <= frequency < 3e12:
    print("Microwaves")
elif 3e12 <= frequency < 4.3e14:
    print("Infrared light")
elif 4.3e14 <= frequency < 7.5e14:
    print("Visible light")
elif 7.5e14 <= frequency < 3e17:
    print("Ultraviolet light")
elif 3e17 <= frequency < 3e19:
    print("X-rays")
else:
    print("Gamma rays")
