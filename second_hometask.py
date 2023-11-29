string_with_multiplication = "~."
print(string_with_multiplication * 40)

user_name = input("Please, enter your name >>").strip().title()

user_age = input("Please, enter your age >>")
user_age = int(user_age)

user_average_salary = input("Please, enter average salary >>")
user_average_salary = float(user_average_salary)

retirement_age = 65
age_before_retirement = retirement_age - user_age

all_money = age_before_retirement * 12 * user_average_salary

bank_rate = 37.3
amount_in_dollar = all_money / bank_rate

toyota_price = 31500
toyota_quantity = amount_in_dollar // toyota_price
toyota_quantity = int(toyota_quantity)

final_statement = (
    f"Я, {user_name}, зможу заробити "
    f"лише __{all_money}__ доларів, що вистачить "
    f" на __{toyota_quantity}__ тойот, мене це не влаштовує, "
    f"тому я буду змінювати своє життя і буду завзято "
    f"вивчати програмування!"
)

print(final_statement)
