import json
import pandas as pd

with open('comments.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

comments_flattened = []


def flatten_comments(comments):
    for comment in comments:
        comment_info = {
            'author_and_id': f"{comment['author'][1:]}@{comment['author_id'][:5]}",
            'comment_id': comment['id'],
            'text': comment['text'],
            'likes': comment.get('likes', 0),
            'time_text': comment.get('time_text', ''),
            'is_reply': False
        }
        comments_flattened.append(comment_info)

        # replies
        if 'replies' in comment and comment['replies']:
            for reply in comment['replies']:
                reply_info = {
                    'author_id': f"{reply['author']}@{reply['author_id']}",
                    'comment_id': reply['id'],
                    'text': reply['text'],
                    'likes': reply.get('likes', 0),
                    'time_text': reply.get('time_text', ''),
                    'is_reply': True
                }
                comments_flattened.append(reply_info)


flatten_comments(data)
df = pd.DataFrame(comments_flattened)

df.to_csv('flattened_comments.csv', index=False, encoding='utf-8-sig')

print("flattened_comments.csv created")
