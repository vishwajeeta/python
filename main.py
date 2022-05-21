import mysql.connector
vishwa = mysql.connector.connect(
  host="localhost",
  user="root",
  password="golu",
  database="sample"
)
print(" welcome to sql \n choose from the given options:")
print("1.show\n2.update\n3.remove\n4.details \n5.select row\n exit or 0")
while True:

  aj=vishwa.cursor()
  name=input("Enter:")
  if name=='1':
      aj.execute("select*from python;")
  else:
      if 'exit' in name:
        print('thanks see you later.....')
        break
      else:
         if '0' in name:
           print('thanks see you later.....')
           break
         else:
             if name=='help':
                 print("1.show\n2.update\n3.remove\n4.details \n5.select row\n exit or 0")
             else:
                 if name=='4':
                     aj.execute("desc python;")
                 else:
                     if name=='5':
                         print("select the name to show")
                         a="select*from python where name='"
                         b=input("Enter the name:")
                         c="';"
                         d=a+b+c
                         aj.execute(d)

                     else:
                         print("               invalid command..")






  for i in aj:
   print(i)
