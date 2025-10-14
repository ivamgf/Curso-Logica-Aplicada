import praw

# Crie um app no Reddit para obter essas credenciais:
# https://www.reddit.com/prefs/apps
client_id = "SEU_CLIENT_ID"
client_secret = "SEU_CLIENT_SECRET"
user_agent = "webcrawler_reddit:v1.0 (by u/SEU_USUARIO)"

# Autenticação
reddit = praw.Reddit(client_id=client_id,
                     client_secret=client_secret,
                     user_agent=user_agent)

# Escolher o subreddit
subreddit = reddit.subreddit("python")

# Buscar os 10 posts mais populares
print("Posts do r/python (Top 10):\n")
for post in subreddit.hot(limit=10):
    print(f"Título: {post.title}")
    print(f"Autor: {post.author}")
    print(f"Upvotes: {post.score}")
    print(f"Link: {post.url}")
    print("-" * 50)
