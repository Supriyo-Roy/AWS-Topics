import random
from faker import Faker
import time
fake = Faker()
l1=[22,33,44,55,66,77,66,55,21212,21212,121]
for i in range(5):
    print(random.randint(1,100),end=" ")
    # print(random.randrange(1,10,2))
    # print(random.choice(l1))
    # print(random.sample(l1,3))

