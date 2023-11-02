'''
A transport company charges the fare according to following table:
Distance Charges
1-50 8 Rs./Km
51-100 10 Rs./Km
> 100 12 Rs/Km
'''

distance = int(input("Enter the distance km : "))
if distance > 0 and distance <= 50:
    dis_caculate = distance * 8
    print("Transport changers is /-", dis_caculate)
elif distance > 50 and distance <= 100:
    dis_caculate = distance * 10
    print("Transport changers is /-", dis_caculate)
else:
    dis_caculate = distance * 12
    print("Transport changers is /-", dis_caculate)

'''
OUTPUT -
Enter the distance km : 60
Transport changers is /- 600
'''