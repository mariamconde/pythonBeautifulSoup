# import beautifulsoup and request here
import requests
import json


# function to get job list from url 'https://www.monster.com/jobs/search?q={role}&where={location}'
def getJobList(role, location):
    url = 'https://www.monster.com/jobs/search?q={role}&where={location}'
    # Complete the missing part of this function here

# save data in JSON file


def saveDataInJSON(jobDetails):
    # Complete the missing part of this function here
    print("Saving data to JSON")

# main function


def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter location: ")
    location = input()
    print("Job role: ", role)
    print("location: ", location)
    print("\n\nResults:\n\n")
    jobs = getJobList(role, location)

    # print jobs and details
    for job in jobs:
        for detail in job:
            print(detail)
        print("\n\n")

    data = {"Title": "test"}
    saveDataInJSON(data)


if __name__ == '__main__':
    main()
