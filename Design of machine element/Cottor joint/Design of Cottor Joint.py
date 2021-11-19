print("Design of Cottor Joint")

#Load required to solve problem
P = float(input("Enter load in (N) : "))

# Display problem statement
print('''
Your Problem is as follows:

    It is required to design a cottor joint to two steel rods of equal diameter. 
    Each radius is subjected to an axial tensile force of''', P, '''kN design the joint 
    and specify it's main diamention.\n''')

# Solution
Material = ["Plain Carbon Steel", "plain carbon steel", "Plain Steel", "plain steel"]
# add more material in list
M = str(input("Enter Name of material : "))
if M in Material:
    Grade = ["30C8","30c8"]
    Grade1 = [] #add more lists after adding material
    G = str(input("Enter Grade : "))
    if G in Grade:
        S = 400
        if G in Grade:
            fs,fs1 = 6, 4 #create more control statements for FOS of different material
    if G in Grade1:
        S = None #Add more S after adding grade in list
        if G in Grade1:
            fs, fs1
    else:
        print("Entered grade is not available or enter valid grade for material")

    print('''Solution:
(I)  Selection of Material:

    On the basis of strength, the material of the two rods and cottor is selected 
    as''', M, "of grade", G, "(Syt =",S,"N/mm**2)\n")

    print('''(II) Selection of Factor of Safty:

    Selection of factor of safty for rod spigot end and socket end is assumed 
    as''', fs, "while cotter is taken as", fs1,". \n")

    print('''(III)Calculation of permissible stresses:

    The permissible stresses rods, spigot end and socket end as follows:\n''')
    T = S/fs
    print("     Sigma_t = {:0.2f}".format(T), "N/mm**s \n")
    C = float((2*S)/fs)
    print("     Sigma_c = {:0.2f}".format(C), "N/mm**2 \n")
    Tau = (0.5*S)/fs
    print("     Tau = {:0.2f}".format(Tau), "N/mm**2\n")
    print("    Permissible stresses for the cottor joint as follows:\n")
    T1 = S/fs1
    print("     Sigma_t1 = {:0.2f}".format(T1), "N/mm**2\n")
    Tau2 = (0.5*S)/fs1
    print("     Tau2 = {:0.2f}".format(Tau2), "N/mm**2\n")

    import math as m
    print('''(IV) Calculations:

1. Failure of rod in tension due to the tensile load P:\n''')
    D = m.sqrt((P/T)*(4/m.pi))
    
    if D % 2 != 0:
        d = int(D + 2)
    else:
        d = int(D + 3)
    print("     d = {:0.2f}".format(D), "mm =", d, "mm\n")

    print("2. Failure of spigot in tension across weak section (or slot):\n")
    D2 = m.sqrt(4*P/(T*(m.pi-1)))
    if D2 % 2 != 0:
        d2 = (D2+3)
    else:
        d2 = (D2+2)
    print("     d2 = {:0.2f}".format(D2), "mm =", int(d2), "mm\n")

    if D2 % 2 == 0:
        t = int((D2 / 4) + 2)
    else:
        t = int((D2 / 4) + 1)
    print("     t =", t, "mm\n")

    print("3. Failure of rod or cottor in crushing:\n")
    C1 = float(P/(int(d2)*t))
    if C1 <= C:
        print("     Sigma_c (induced) {:0.2f} < Sigma_c (permissible) {:0.2f}".format(C1,C), "mm\n")
        print("     Design is Safe.\n")
    
        print("4. Failure of socket in tension across the slot:\n")

    # create quadratic equation
        def quad_eq(a,b,c):
            x1 = (-b + m.sqrt(abs(4*a*c)))/(2*a)
            if x1 < 0:
                None
            else:
                return(x1)
            x2 = -(b + m.sqrt(abs(4*a*c)))/(2*a)
            if x2 < 0:
                None
            else:
                return(x2)

        d1 = quad_eq(m.pi/4, -t, (-((m.pi/4)*(d2**2)) + (d2*t)) - (P/T))
        print("     d1 = {:0.2f}".format(d1), "mm", "=", int(d1 + 4), "mm\n")

        print("5. Failure of cotter in shear:\n")
        b = int((P/(t*Tau2))/2)
        print("     b =", b, "mm\n")

        print("6. Failure of socket cotter in crushing:\n")
        d41 = ((P/(t*C))+d2)
        if d41 % 2 != 0:
            d4 = d41+3
        else:
            d4 = d41+2
        print("     d4 = {:0.2f}".format(d41), "mm =", int(d4), "mm\n")

        print("7. Failure of socket end in shearing:\n")
        c1 = ((P/Tau)/(2*(int(d4+3)-d2)))
        if c1 % 2 != 0:
            c = c1+2
        else:
            c = c1+3
        print("     c = {:0.2f}".format(c1), "mm =", int(c), "mm\n")

        print("8. Failure of rod end in shear:\n")
        a1 = (P/(2*int(d2)*Tau))
        if a1 % 2 != 0:
            a = a1+2
        else:
            a = a1+3
        print("     a = {:0.2f}".format(a1), "mm =", int(a), "mm\n")

        print("9. Failure of spigot collor in crushing:\n")
        d31 = m.sqrt((P/C)*(4/m.pi)+(d2**2))
        if d31 % 2 != 0:
            d3 = d31+3
        else:
            d3 = d31+2
        print("     d3 = {:0.2f} mm".format(d31), "=", int(d3), "mm\n")

        print("10. Failure of the spigot collor in shearing:\n")
        t11 = P/(m.pi*d2*Tau)
        if t11 % 2 != 0:
            t1 = t11+1
        else:
            t1 = t11+2
        print("     t1 = {:0.2f} mm".format(t11), "=", int(t1), "mm\n")

        print("11. Failure of cotter in bending:\n")
        B = (P*(int(d4)+(0.5*int(d2))))/((2*t)*(b**2))
        print("     Sigma_b =", B, "N/mm**2\n")

        print("12. The length (l) of cotter is taken as 4d:\n")
        l = 4*d
        print("     l =", l, "mm\n")

        print("13. Tapper in cotter:\n")
        Tap = m.degrees(m.atan(1/24))
        print("     Theta = {:0.2f} degree\n".format(Tap))
    
        print('''14. The draw of cotter is gradually taken as: 2 mm to 3 mm''')

    else:
        print("     Design is unsafe.\n")
else:
    print('''Choosen grade isn't available or you might had entered wrong grade.
    Or
    Please enter proper material or selected material isn't avilable.\n''')
    
