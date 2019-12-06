> from brandi.models import Cloth, Closet, Temp, Month, Category
> from django.utils import timezone
> cate = Category(cate_id="1", cate_name="Top")
> cate.save()
> Category.objects.all()
cate = Category(cate_id="1", cate_name="Top")
cate.save()
cate = Category(cate_id="2", cate_name="Outer")
cate.save()
cate = Category(cate_id="3", cate_name="Skirt")
cate.save()
cate = Category(cate_id="4", cate_name="Pants")
cate.save()
cate = Category(cate_id="5", cate_name="One-piece")
cate.save()

m1 = Month(month="1")
m1.save()
m2 = Month(month="2")
m2.save()
m3 = Month(month="3")
m3.save()
m4 = Month(month="4")
m4.save()
m5 = Month(month="5")
m5.save()
m6 = Month(month="6")
m6.save()
m7 = Month(month="7")
m7.save()
m8 = Month(month="8")
m8.save()
m9 = Month(month="9")
m9.save()
m10 = Month(month="10")
m10.save()
m11 = Month(month="11")
m11.save()
m12 = Month(month="12")
m12.save()

t1 = Temp(temp="0")
t1.save()
t1 = Temp(temp="1")
t2 = Temp(temp="2")
t3 = Temp(temp="3")
t4 = Temp(temp="4")
t5 = Temp(temp="5")
t6 = Temp(temp="6")
t7 = Temp(temp="7")
t8 = Temp(temp="8")

t1.save()
t2.save()
t3.save()
t4.save()
t5.save()
t6.save()
t7.save()
t8.save()


# make cloth
c = Cloth()

c = Cloth(product_id="1234", category=1, cloth_type="Knit", color="Black", pattern="none", month="1", temp="1", label="img.jpg")


# make closet
c = Closet(user_id="1", create_at=timezone.now, updated_at=timezone.now)

closet.clothes.add(~~)
cloth.closets

# delete cloth
Cloth.objects.filter(product_id=8503628).delete()

# update cloth
# 한개만 수정
c = Cloth.objects.get(id=..)
c.label = ...
c.save()
# 여러개 동시에 수정
c = Cloth.objects.filter(label="1C2CFF6").update(category_id=1)
c = Cloth.objects.filter(label="1T00FF5", product_id=12331893).update(color="화이트")


# read cloth
Cloth.objects.filter(cloth_type="후드/맨투맨")

# update temp
t = Temp.objects.filter(temp=0).update(temp=9)

git rm -rf --cached *.pyc
