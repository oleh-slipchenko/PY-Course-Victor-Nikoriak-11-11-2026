# AI log: none

# об’єднайте їх за допомогою конкатенації, додавши між ними пробіл. Присвойте результат змінній `full_name` і виведіть привітання: Hi, {first_name} {last_name}!
first_name="Oleh"
last_name="Slipchenko"
full_name = " ".join([first_name, last_name])
print(f"Hi, {full_name}!")