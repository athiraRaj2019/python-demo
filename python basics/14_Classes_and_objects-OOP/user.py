# user class
# below is the user class, anything inside a class is called class body
class User:
    # init function is called constructor
    # to ensure these variables belongs to user class we use self.<parameter>

    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.current_job_title = current_job_title

    # functions that belongs to a class are called methods
    def change_password(self, new_password):
        self.password = new_password

    def change_job_title(self, new_job_title):
        self.current_job_title = new_job_title

    def get_user_info(self):
        print(f"user {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email}")


