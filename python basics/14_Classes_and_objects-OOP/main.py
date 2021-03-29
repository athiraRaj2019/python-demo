#use name of module and not that of class
from user import User
from post import Post
# create an object
app_user_one = User("ak@ak.com", "Athira K", "pwd1", "Devops Engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("Senior Systems Engineer")
app_user_one.get_user_info()

app_user_two = User("jj@jj.com", "Jhon", "pwd2", "consultant")
app_user_two.get_user_info()

new_post = Post("On a secret mission", app_user_one.name)
new_post.get_post_info()