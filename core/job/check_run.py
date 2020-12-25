import json


class CheckRun:

    def __init__(self) -> None:
        self.uncheck = {}
        self.checked = {}

    def add_run_job_in_json(self, new_done_job):
        ''' move element from uncheck.json to check.json'''
        checked_path = r"example_dir\ex1\ta\job\job.json"
        new_done_job_json = new_done_job

        with open(checked_path) as job:
            self.checked = json.load(job)

        self.checked["run_job"].append(new_done_job_json)

        with open(checked_path,"w") as k:
            k.write(json.dumps(self.checked))

cr = CheckRun()
checked = { "filename": "123456.zip", "student_id": "12345678", "name": "test", "ex": "ex1", "score1": 500 }
cr.add_run_job_in_json(checked)
