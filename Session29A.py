import matplotlib.pyplot as plt

languages = ["Python", "Java", "C++", "Dart", "JavaScript"]
jobs = [70, 80, 88, 12, 90]

plt.pie(jobs, labels=languages)
plt.legend()
plt.show()

chinese = ["Noddels", "Burger", "Manchurian", "Chilly Potato"]
persons = [60, 10, 20, 10]
plt.pie(persons, labels=chinese)
plt.legend()
plt.show()

