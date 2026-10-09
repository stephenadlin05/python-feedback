feedback = [5,4,3,5,2,4,5,1]
def avg_rating(feedback):
    return sum(feedback)/len(feedback)
print("Average Rating:", avg_rating(feedback))

def five_star_ratings(feedback):
    count = 0
    for rating in feedback:
     if rating >=5: 
      count +=1
    return count
print("5_star_ratings:", five_star_ratings(feedback))

def count_below_three(feedback):
    count = 0
    for rating in feedback:
     if rating <=3: 
      count +=1
    return count
print("Ratings_below_three:", count_below_three(feedback))

#Cricket scores
runs = [45,67,12,89,105,54]
def highest_score(runs):
    return max(runs)
print("Highest_score:",highest_score(runs))

def count_half_centuries(runs):
    count = 0
    for score in runs:
     if score >=50 and score <=99:  
      count +=1
    return count
print("Half_centuries:", count_half_centuries(runs))

def count_centuries(runs):
    count = 0
    for score in runs:
     if score >=100:  
      count +=1
    return count
print("Centuries:", count_centuries(runs))

#HospitalPatientRecord
patients = [{"Name":"A","Age":45},
            {"Name":"B","Age":62},
            {"Name":"C","Age":28},
            {"Name":"D","Age":70}]

def count_senior_citizen(patients):
    count = 0
    for patient in patients:
        if patient["Age"] >= 60:
            count += 1
    return count
print("senior_citizen:", count_senior_citizen(patients))

def oldest_patient(patients):
    oldest = patients[0]
    for patient in patients:
        if patient["Age"] > oldest["Age"]:
         oldest = patient
    return oldest
print("Oldest_patient:", oldest_patient(patients))

def avg_Age(patients):
    total = 0
    count = 0
    for patient in patients:
        total += patient["Age"]
        count += 1
    return total / count
print("Average Age:", avg_Age(patients))

#studentDatabase
students =[{"Name":"Amit","Marks":80},
           {"Name":"Neha","Marks":92},
           {"Name":"Ravi","Marks":75},
           {"Name":"Priya","Marks":88}]

def student_data(students):
    names = []
    highest_marks = 0
    topper = ""
    totalMarks = 0
    stu_above80= []
    for stu in students:
        names.append(stu["Name"])
        if stu["Marks"] > highest_marks:
            highest_marks = stu["Marks"]
            topper = stu["Name"]
        if stu["Marks"] > 80:
            stu_above80.append(stu["Name"])
        
        totalMarks += stu["Marks"]
        avg = totalMarks/len(students)

                
    print("all students: ", names)
    print("topper: ", topper)
    print("average marks: ",avg)
    print("scorring above 80 :",stu_above80 )
    

student_data(students)

#onlineshoppingdata
orders = [{"Products":"Laptop","Price":50000},
          {"Products":"Mouse","Price":500},
          {"Products":"Keyboard","Price":1500},
          {"Products":"Monitor","Price":1200}]

def orders_data(orders):
    Products = []
    
    for order in orders:
        Products.append(order["Products"])
    
    return Products

print("All Products:", orders_data(orders))

def orders_data(orders):
    products = []

    for order in orders:
        if order["Price"] > 1000:
            products.append(order["Products"])

    return products

print("Products_above_1000:",orders_data(orders))

def orders_data(orders):
    highest_price = 0
    expensive_product = None

    for order in orders:
        if order["Price"] > highest_price:
            highest_price = order["Price"]
            expensive_product = order

    return expensive_product

print("Expensive_product:", orders_data(orders))

def orders_data(orders):
    discounted_orders = []

    for order in orders:
        discounted_price = order["Price"] * 0.95
        discounted_orders.append((order["Products"], discounted_price))
    return discounted_orders
print("After 5% discount:", orders_data(orders))


#CompanyPerformanceDashboard
company=[{"Department":"Sales","Revenue":12000},
         {"Department":"HR","Revenue":30000},
         {"Department":"IT","Revenue":80000},
         {"Department":"Marketing","Revenue":60000}]

def company_data(company):
    total_rev = 0
    highest_rev = company[0]["Revenue"]
    above_50000 = []

    for data in company:
        total_rev += data["Revenue"]

        if data["Revenue"] > highest_rev:
            highest_rev = data["Revenue"]

        cont_rev = (data["Revenue"] / total_rev) * 100
        print(f'{data["Department"]} = {cont_rev:.2f}')

    avg_rev = total_rev / len(company)

    if data["Revenue"] > 50000:
            above_50000.append(data["Department"])

    print("Total Revenue:", total_rev)
    print("Highest Revenue:", highest_rev)
    print("Average Revenue:", avg_rev)
    print("Departments above 50000:", above_50000)
    sort_comp =  sorted(company, key=lambda x: x["Revenue"], reverse = True)
    print(sort_comp)
    
         
company_data(company)

    
    


        





































 

