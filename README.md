# interview-schedule

## Build and start 
You need to have python and pip installed on your computer.

Install dependencies:

`pip install -r requirements.txt`

Switch into project folder:

`cd interview_schedule`

Run tests: 

`python manage.py test`

Database migration : 

`python manage.py migrate`

Start the development server: 

`python manage.py runserver`

## Api

After starting the development server you have a browseable api under: 
`http://127.0.0.1:8000/api/`

### /api/candidates/
Lists all candidates and creating new candidates.

### /api/candidates/<id: Int>
Show candidate with given id and interact with it.

### /api/interviewers/
Lists all interviewers and creating new interviewers.

### /api/interviewers/<id: Int>
Show interviewer with given id and interact with it.

## /api/candidate/appointmentslots
List all candidate appointmentslots. You can filter with the query parameter `candidateId=<id: Int>`.

## /api/candidate/appointmentslots/<id: Int>
Show appointmentslot with given id and interact with it.

## /api/interviewer/appointmentslots
List all interviewer appointmentslots. You can filter with the query parameter `interviewerId=<id: Int>`.

## /api/interviewer/appointmentslots/<id: Int>
Show appointmentslot with given id and interact with it.

## /api/appointments/overlap/?candidateId=<id: Int>&interviewerIds=<id: Int>,<id: Int>
Calculates appointment overlaps for an interviewer and candidate. 
Both query parameter are mandatory!

For each candidate slot exists a list of interviewer slots which lies within the candidate slot. 

Example response: 

```
[
    {
        "candidate-slot": {
            "id": 1,
            "begin": "2018-06-28T08:00:00Z",
            "end": "2018-06-29T08:00:00Z",
            "candidate": 1
        },
        "interviewer-slots": [
            {
                "id": 3,
                "begin": "2018-06-28T08:00:00Z",
                "end": "2018-06-29T08:00:00Z",
                "interviewer": 2
            }
        ]
    },
    {
        "candidate-slot": {
            "id": 6,
            "begin": "2018-06-25T08:00:00Z",
            "end": "2018-06-26T08:00:00Z",
            "candidate": 1
        },
        "interviewer-slots": []
    }
]
```

