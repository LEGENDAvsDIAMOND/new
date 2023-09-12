from championship import Championship
# from grand_prix import GrandPrix

a = Championship()

ali = a.creat_driver("Ali")
vali = a.creat_driver("Vali")
sali = a.creat_driver("Sali")

f1 = a.difine_grand_prix("f1-1")
f2 = a.difine_grand_prix("f2-2")

settime_1 = a.set_time(f1, ali, 5, 20, 30, 200)
settime_2 = a.set_time(f1, vali, 5, 10, 23, 123)
setting_3 = a.set_time(f2, ali, 5, 3, 37, 888)
# settime_3 = a.set_time(f2, sali, 5, 9, 58, 1234)

# b = a.get_grand_prix("f1-1").get_GP_rankin()
#
#  c = a.get_grand_prix("f2-2").get_GP_rankin()
# b = a.get_grand_prix("f1-1").get_position(ali)
# b1 = a.get_grand_prix("f1-1").get_position(vali)
# b = ali.get_points()
b = a.get_championship_ranking()
print(b)



# print(a.get_drivers())
# print(a.get_driver("Ibrohimjon"))
# print(a.get_driver("Ali"))
# a.difine_grand_prix("FirstGrand")
# print(a.get_grand_prix("jkhvenflhv"))
# print(a.get_grand_prix("FirstGrand"))