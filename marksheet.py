grace_count=0
sup_count=0
absent=0


maths=int(input('Enter the number for maths: '))
sst=int(input('Enter the number for sst: '))
science=int(input('Enter the number for science: '))
hindi=int(input('Enter the number for hindi: '))
english=int(input('Enter the number for english: '))

lowest=20

if(21<=maths<=30):
    sup_count+=1
if(21<=sst<=30):
    sup_count+=1
if(21<=science<=30):
    sup_count+=1
if(21<=hindi<=30):
    sup_count+=1
if(21<=english<=30):
    sup_count+=1

if(31<=maths<=33 ):
    grace_count+=1
if(31<=science<=33):
    grace_count+=1
if(31<=hindi<=33):
    grace_count+=1
if(31<=sst<=33):
    grace_count+=1
if(31<=english<=33):
    grace_count+=1
if grace_count<2:
    sup_count+=1

if(maths<20):
    absent+=1
if(science<20):
    absent+=1
if(hindi<20):
    absent+=1
if(english<20):
    absent+=1
if(sst<20):
    absent+=1
    

total=maths+sst+science+hindi+english
average=int((total/500)*100)

print('Total= ',total)
print('Average= ',average)

if (maths<=20 or sst<=20 or science<=20 or hindi<=20 or english<=20 and absent>1):
    print("FAILED IN")
    if (maths<=20):
        print('maths')
    if (science<=20):
        print('science')
    if (sst<=20):
        print('sst')
    if (hindi<=20):
        print('hindi')
    if (english<=20):
        print('english')


if (21<=maths<=30 or 21<=sst<=30 or 21<=science<=30 or 21<=hindi<=30 or 21<=english<=30 or grace_count>2 or absent<2):
    if (sup_count<2 ):
        print('SUPPLIMENTRY IN:')
        
        if (21<=maths<=30 or maths<lowest):
            print('maths')
            sup_count+=1
        if (21<=science<=30 or science<lowest):
            print('science')
            sup_count+=1
        if (21<=sst<=30 or sst<lowest):
            print('sst')
            sup_count+=1
        if (21<=hindi<=30 or hindi<lowest):
            print('hindi')
            sup_count+=1
        if (21<=english<=30 or english<lowest):
            print('english')
            sup_count+=1
    else:
        print("FAILED")


if (31<=maths<=33 or 31<=sst<=33 or 31<=science<=33 or 31<=hindi<=33 or 31<=english<=33):
    if(grace_count<2 and sup_count<2):
        print("GRACE applied in following subjects: ")
        if(31<=maths<=33):
            print('maths')
            
        if(31<=sst<=33):
            print('sst')
            
        if(31<=science<=33):
            print('science')
            
        if(31<=hindi<=33):
            print('hindi')
            
        if(31<=english<=33):
            print('english')
        
    

if (maths>20 and sst>20 and hindi>20 and english>20 and science>20 and sup_count<2):
    if (average>=90):
        print("GRADE= A+")
    elif(average>=80):
        print("GRADE= A")
    elif(average>=75):
        print("GRADE= B")
    elif(average>=70):
        print("GRADE= C")
    elif(average>=60):
        print("GRADE= D")
    else:
        print("GRADE=POOR")

