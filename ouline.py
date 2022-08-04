# import beautifulsoup and request here
import requests
from bs4 import BeautifulSoup
import json

url = "https://www.indeed.com/jobs?q=SoftwareDeveloper&l=Charlotte"
payload = {}
headers = {
    'Cookie': 'CSRF=ojIJVoKITjWihgD00Wsw8og5Hc1D9jjy; CTK=1g9ittdkais2a802; __cf_bm=3d_3hEaWqjebPYFH1ZB06COXFyW1h_t1qMxR6wPYVdg-1659566470-0-ATYe9fdCDReSZ5kyzgvbicC+JDlKwhgvFvGSbDDdko6JkHClfUeUHJ1EFMuOs16qJbo4Dv9qQTMbCUystHtrkYY=; _cfuvid=8bi6jLjOgpRdvOI8aEyezfmaUd9mO0LufOGoH05eHQU-1659566470830-0-604800000; CTK=1g9ittdkais2a802; INDEED_CSRF_TOKEN=V52DfhCraHkJ3bBxqz5X2GaEbJSI4o9L; JSESSIONID=5665C2F454B693F196A77CE7BAE6B2FE; LV="LA=1659566470:CV=1659566470:TS=1659566470"; PREF="TM=1659566529355:L=Charlotte"; RQ="q=Software+Developer&l=Charlotte&ts=1659566529385"; UD="LA=1659566529:CV=1659566529:TS=1659566529:SG=81eb9022bb235584be7202b852ab2d2c"; indeed_rcc="LV:CTK:UD"; jaSerpCount=1'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)


# function to get job list from url 'https://www.monster.com/jobs/search?q={role}&where={location}'
def getJobList(role, location):
    url = 'https://www.monster.com/jobs/search?q={role}&where={location}'
    # Complete the missing part of this function here


def getJobList(role, location):
    # Complete the missing part of this function here
    response = requests.request("GET", url)  # Complete this part
    # print the status code here!
    print(response.status_code)
    soup = BeautifulSoup(response.content, "html.parser")  # Complete this part
    JobDetails = soup.find_all('div', class_='card card__job')
    # Create an array Here
    jobs = []
    for job in JobDetails:
        jobTitle = job.find('h2', class_='card__job-title').text.strip()
        company = job.find(
            'div', class_='card__job-empname-label').text.strip()
        description = job.find(
            'p', class_='card__job-snippet').text.replace('\n', '').replace("'", "").strip()
        jobDetailsjson = {
            "Title": jobTitle,
            "Company": company,
            "Description": description
        }
        # Add jobDetailsjson to that array
        jobs.append(job)
    return jobs  # defined array


# save data in JSON file
def saveDataInJSON(jobDetails):
    # Complete the missing part of this function here
    with open('jobDetails.json') as file:
        json.dump(file)
    print("Saving data to JSON")

# main function
def main():
    # Write a code here to get job location and role from user e.g. role = input()
    print("Enter role you want to search")
    role = input()
    # Complete the missing part of this function here
    print("Enter role you want to search")
    role = input()
    location = input("Enter location you want to search\n")
    print("My role is: " + "'" + role + "'" + ' ' +
          "my location is " + "'" + location + "'")


if __name__ == '__main__':
    main()
