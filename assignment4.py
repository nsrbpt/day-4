activityscores = [23,4,56,89,67]

rollnumber = input("Enter your Register Number: ")
D = int(rollnumber[-1])

low_risk = []
medium_risk = []
high_risk = []
critical_risk = []

valid = 0
ignored = 0
remove = 0

for score in activityscores:

    if score < 0:
        ignored = ignored + 1

    else:
        valid = valid + 1

        if score <= 30:
            low_risk = low_risk + [score]

        elif score <= 60:
            medium_risk = medium_risk + [score]

        elif score <= 100:
            high_risk = high_risk + [score]

        else:
            critical_risk = critical_risk + [score]

print("Before Filtering\n")
print("Low Risk:", low_risk)
print("Medium Risk:", medium_risk)
print("High Risk:", high_risk)
print("Critical Risk:", critical_risk)

if D % 2 == 0:
    remove = len(low_risk)
    low_risk = []
    print("\n if D is even → Low Risk will removed")

else:
    remove = len(critical_risk)
    critical_risk = []
    print("\nD is ODD → Critical Risk removed")

print("\nAfter Personalized Filtering")
print("Low Risk:", low_risk)
print("medium risk:", medium_risk)
print("high Risk:", high_risk)
print("Critical Risk:", critical_risk)

print("\nTotal Valid Entries:", valid)
print("ignored Entries:", ignored)
print("removed Due to Personalization:", remove)
