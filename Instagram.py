from instapy import InstaPy
from instapy import smart_run

my_username = "carlosveigafilho"
my_password = "patamares42"

session = InstaPy(username = my_username, password = my_password, headless_browser = False)

with smart_run(session):
    session.set_relationship_bounds(enabled=True, delimit_by_numbers=True, max_followers=150000, min_followers=10, min_following=50)
    session.set_do_follow(True,percentage=100)
    session.like_by_tags(["music"], amount=80)
