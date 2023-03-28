
import pendulum as p
import datetime

# 1.feladat - Idő a világ körül
def time_zones_now():
    cities = ["Europe/Budapest",
              "Asia/Pyongyang",
              "America/Toronto",
              "Asia/Tokyo",
              "Pacific/Kiritimati"]
    times = []
    for city in cities:
        now = p.now(city)
        now = now.to_datetime_string()
        times.append(now)
    for i in range(len(cities)):
        print(f"{cities[i]} idő: {times[i]}")


# from my_package import my_package_base as mp
import my_package.my_package_base as mp
# a kettő ugyanazt tudja

# 6.feladat: A csomagunk használata
def using_my_package():
    num_1 = 33
    num_2 = 24
    print(mp.my_sum(num_1, num_2))
    print(mp.my_avg(num_1, num_2))
    print(mp.my_pow(num_1, num_2))
    print(mp.my_prime_finder(100))


def time_handling():
    today = datetime.date.today()
    yesterday = today - datetime.timedelta(days=1)
    tomorrow = today + datetime.timedelta(days=1)
    next_week = today + datetime.timedelta(weeks=1)
    print("Tegnap: ", yesterday)
    print("Ma: ", today)
    print("Holnap: ", tomorrow)
    print("Jövő hét: ", next_week)

time_handling()