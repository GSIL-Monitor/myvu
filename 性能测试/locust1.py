from locust import HttpLocust, TaskSet, task

class UserBehavior(TaskSet):

    @task(1)
    def baidu(self):
        self.client.get("/")



class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 3000
    max_wait = 6000