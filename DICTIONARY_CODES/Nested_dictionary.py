courses={
    "python":{"instructor":"priya","duration":45},
    "sql":{"instructor":"kunal","duration":35},
    "java":{"instructor":"shivansh","duration":65},
    "php":{"instructor":"akhilesh","duration":60}
}
for course,details in courses.items():
    if course=="python":
        print("ins_name:",details["instructor"])
        print("duration:",details["duration"])
        
