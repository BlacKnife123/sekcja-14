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

    print("Wręczamy ciasteczko mistrza dyscypliny do użytkowników od id: ", usersWithTopCompletedTasks)
    




