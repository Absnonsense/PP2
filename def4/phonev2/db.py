import psycopg2
from config import load_config
def connect():
    return psycopg2.connect(**load_config())
def create_user(username):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("INSERT INTO users (username) VALUES (%s) RETURNING id;", (username,))
            user_id = cur.fetchone()[0]
        conn.commit()
    return user_id
def get_user_id(username):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT id FROM users WHERE username = %s;", (username,))
            result = cur.fetchone()
            return result[0] if result else None
def get_user_score(user_id):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("SELECT level, score FROM user_scores WHERE user_id = %s;", (user_id,))
            result = cur.fetchone()
            return result if result else (1, 0)
def update_user_score(user_id, level, score):
    with connect() as conn:
        with conn.cursor() as cur:
            cur.execute("""
                INSERT INTO user_scores (user_id, level, score)
                VALUES (%s, %s, %s)
                ON CONFLICT (user_id) 
                DO UPDATE SET level = EXCLUDED.level, score = EXCLUDED.score;
            """, (user_id, level, score))
        conn.commit()