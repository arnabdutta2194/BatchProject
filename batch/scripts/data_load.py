import csv
from os import name
from unesco.models import Region,Iso,State,Category,Site

def run():
    fhand = open('unesco/whc-sites-2018-clean.csv')
    reader = csv.reader(fhand)
    next(reader)

    Region.objects.all().delete()
    Iso.objects.all().delete()
    State.objects.all().delete()
    Category.objects.all().delete()
    Site.objects.all().delete()

    for row in reader:
        print(row)

        r,created = Region.objects.get_or_create(name=row[9])
        i,created = Iso.objects.get_or_create(name=row[10],region=r)
        s,created = State.objects.get_or_create(name=row[8])
        c,created = Category.objects.get_or_create(name=row[7])
        
        try:
            yr=int(row[3])
        except:
            yr=None

        try:
            long=float(row[4])
        except:
            long=None

        try:
            lat=float(row[5])
        except:
            lat=None

        if row[6]=="":
            ar=None
        else:
            ar = float(row[6])

        try:
            desc=row[1]
        except:
            desc=None

        try:
            just=row[2]
        except:
            just=None

        
        st,created = Site.objects.get_or_create(
            name = str(row[0]), description = desc, justification = just,
            year = yr, longitude = long, latitude = lat,
            area = ar, category = c, state = s, iso = i
        )