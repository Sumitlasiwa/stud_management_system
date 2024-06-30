import json

def pass_fail_determination(name, roll):
    """This function checks pass or fail status of student

    Args:
        name (str): name of student
        roll (int): roll no of student

    Returns:
        str : pass or fail
    """
    all_records = []
    try:
        with open("data/student.json", "r") as file:
            all_records = json.load(file)
    except:
        pass
    
    result = "pass"
    for each_record in all_records:
        if each_record["Name"] == name and each_record["roll"] == roll:
            mark_list_of_each = each_record["Marks"]
            for mark in mark_list_of_each:
                if mark<32:
                    result = "fail"
                    break
                else:
                    pass
            break

    return result

# if __name__=="__main__":
#     print(pass_fail_determination("Sumit", 41))

def highest_and_lowest_scores(name, roll):
    """gives the highest and lowest marks of a student

    Args:
        name (str): name of student
        roll (int): roll no of student
    """
    all_records = []
    try:
        with open("data/student.json", "r") as file:
            all_records = json.load(file)
    except:
        pass
    
    highest = 0
    lowest = 0
    for each_record in all_records:
        if each_record["Name"] == name and each_record["roll"] == roll:
            mark_list_of_each = each_record["Marks"]
            highest = max(mark_list_of_each)
            lowest = min(mark_list_of_each)
            break
    print(f"highest score: {highest}")
    print(f"lowest score: {lowest}")

# if __name__=="__main__":
#     highest_and_lowest_scores("Sumit",41)

def percentage(name, roll):
    """gives the percentage of student

    Args:
        name (str): name of student
        roll (int): roll no of student

    Returns:
        float: percentage of student
    """
    all_records = []
    try:
        with open("data/student.json", "r") as file:
            all_records = json.load(file)
    except:
        pass
    
    sum = 0
    percent = 0
    for each_record in all_records:
        if each_record["Name"] == name and each_record["roll"] == roll:
            mark_list_of_each = each_record["Marks"]
            for mark in mark_list_of_each:
                sum+=mark
            percent = round(sum/len(mark_list_of_each), 2)
            break
    return percent

# if __name__=="__main__":
#     print(percentage("Sumit",41))

def rank_calculation(name, roll):
    """calculates rank of a student

    Args:
        name (str): name of student
        roll (int): roll no of student
        
    """
    specific_stud_percent = percentage(name, roll)
    percentage_of_all = []
    all_records = []
    try:
        with open("data/student.json", "r") as file:
            all_records = json.load(file)
    except:
        pass

    for i in all_records:
        percent = percentage(i["Name"], i["roll"])
        percentage_of_all.append(percent)

    percentage_of_all.sort(key = None, reverse = True) #sorts in decending

    rank = 0
    for i in percentage_of_all:
        rank += 1 
        if i == specific_stud_percent:
            break

    print(f"Rank: {rank}")

# if __name__=="__main__":
#     rank_calculation("Sumit", 41)

    

    
                
    