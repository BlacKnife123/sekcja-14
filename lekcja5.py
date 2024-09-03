import requests
import json


"""
{
1:11
2:6
3:15
}
"""

def count_task_frequency(tasks):
    completedTasksFrequencyByUser = dict()
    for entry in tasks:
        if(entry["completed"] == True):
            try:
                completedTasksFrequencyByUser[entry["userId"]] += 1
            except KeyError:
                completedTasksFrequencyByUser[entry["userId"]] = 1

    return completedTasksFrequencyByUser

def get_keys_with_top_values(my_dict):
    return [
    key
    for (key,value) in my_dict.items()
    if value == max(my_dict.values())
    ]

def get_users_with_top_completed_tasks(completedTasksFrequencyByUser):
    userIdWithMaxCompletedTasks = []
    maxAmountOfCompletedTasks = max(completedTasksFrequencyByUser.values())
    for userId, numberOfCompletedTasks in completedTasksFrequencyByUser.items():
        if(numberOfCompletedTasks == maxAmountOfCompletedTasks):
            userIdWithMaxCompletedTasks.append(userId)

    return userIdWithMaxCompletedTasks

r = requests.get("https://jsonplaceholder.typicode.com/todos")

#tasks = json.loads(r.text)

try:
    tasks = r.json()
except json.decoder.JSONDecodeError:
    print("Niepoprawny format")
else:
    completedTasksFrequencyByUser = count_task_frequency(tasks)
    usersWithTopCompletedTasks = get_users_with_top_completed_tasks(completedTasksFrequencyByUser)

# #sposób 1
# r = requests.get("https://jsonplaceholder.typicode.com/users")

# users = r.json()

# for user in users:
#     if(user["id"] in usersWithTopCompletedTasks):
#         print("Wręczamy ciasteczko mistrza dyscypliny do użytkowników od imieniu: ", user["name"])

# #sposób 2

# for userId in usersWithTopCompletedTasks:
#     # r = requests.get("https://jsonplaceholder.typicode.com/users/"+str(userId))
#     r = requests.get("https://jsonplaceholder.typicode.com/users/", params="id=" +str(userId))
#     user = r.json()
#     print("Wręczamy ciasteczko mistrza dyscypliny do użytkowników od imieniu: ", user[0]["name"])

#sposób 3 NAJLEPSZY
def change_list_into_conj_of_param(my_list,key="id"):
    conj_param = "id="

    lastIterationNumber = len(my_list)
    i = 0
    for item in my_list:
        i+=1
        if (i == lastIterationNumber):
            conj_param += str(item)
        else:
            conj_param += str(item) + "&"+key+"="

    return conj_param

conj_param = change_list_into_conj_of_param(usersWithTopCompletedTasks,"id")
r = requests.get("https://jsonplaceholder.typicode.com/users/", params=conj_param)

users = r.json()

for user in users:
    print("Wręczamy ciasteczko mistrza dyscypliny do użytkowników od imieniu: ", user["name"])
    