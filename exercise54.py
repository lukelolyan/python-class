wavelength = float(input("Enter the wavelength (nm): "))

if 380 <= wavelength < 450:
    print("Color: Violet")
elif 450 <= wavelength < 495:
    print("Color: Blue")
elif 495 <= wavelength < 570:
    print("Color: Green")
elif 570 <= wavelength < 590:
    print("Color: Yellow")
elif 590 <= wavelength < 620:
    print("Color: Orange")
elif 620 <= wavelength <= 750:
    print("Color: Red")
else:
    print("Error: Wavelength is outside the visible spectrum.")
