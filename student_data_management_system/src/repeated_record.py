import json

def isrepeated(id):
    """checks whether input is already in
    db or not

    Args:
        id (int): roll of student or id of teacher

    Returns:
        bool: True id or roll is repeated
    """

    is_repeated = False
    all_records = []
    try:
        with open("data/teacher.json", "r") as file:
            all_records = json.load(file)
    except:
        if __name__ =="__main__":
            print("File is empty!") 

    for each_record in all_records:

        if each_record["Id"] == id :
            is_repeated = True
            break

    return is_repeated

if __name__ == "__main__":
    print(isrepeated(12))

        