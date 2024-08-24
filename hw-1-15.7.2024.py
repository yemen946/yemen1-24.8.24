
# קלוט 10 מספרים מהמשתמש בלולאה, ואז הדפס:
positive_num = 0
negative_num = 0
zero_num = 0
divisible_by_7_num  = 0
last_positive_num = None;
last_negative_num = None;

# קליטת 10 מספרים מהמשתמש
for i in range(1, 11):
    number = int(input("insert number: "));

# אם הוכנס המספר מינוס 9999 אז צא מהלולאה ואל תדפיס סטטיסטיקות בכלל
    if number == -9999:
        break;

# אם הוכנס מספר גדול מ- 1000 או קטן ממינוס 1000 התעלם מהמספר
    if number > 1000 or number < -1000:
        continue;

# בדיקה האם המספר חיובי, שלילי או אפס ועדכון המונים בהתאם
    if number > 0:
        positive_num += 1
        last_positive_number = number
    elif number < 0:
        negative_num += 1
        last_negative_num = number
    else:
        zero_num += 1

# בדיקה האם המספר מתחלק ב-7 ללא שארית
    if number % 7 == 0:
        divisible_by_7_num += 1
    else:
    # הדפסת הסטטיסטיקות לאחר סיום הלולאה
        print("Positive numbers received: ", positive_num);
        print("Negative numbers received: ", negative_num);
        print("The number 0 has been entered: ", zero_num);
        print("Numbers divisible by 7 without a remainder: ", divisible_by_7_num);
        print("Last positive number entered: ", last_positive_num if last_positive_num is not None else "None")
        print("Last negative number entered: ", last_negative_num if last_negative_num is not None else "None")




