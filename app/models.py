import pyodbc
from flask import current_app


def get_connection():
    conn_str = (
        "DRIVER={ODBC Driver 17 for SQL Server};"
        f"SERVER={current_app.config['SQL_SERVER']};"
        f"DATABASE={current_app.config['SQL_DATABASE']};"
        f"UID={current_app.config['SQL_USER_NAME']};"
        f"PWD={current_app.config['SQL_PASSWORD']};"
        "Encrypt=yes;TrustServerCertificate=no;Connection Timeout=30;"
    )
    return pyodbc.connect(conn_str)


def get_all_articles():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, body, image_url FROM articles ORDER BY id DESC")
    rows = cursor.fetchall()
    conn.close()
    return rows


def get_article(article_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT id, title, author, body, image_url FROM articles WHERE id = ?", article_id)
    row = cursor.fetchone()
    conn.close()
    return row


def insert_article(title, author, body, image_url):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO articles (title, author, body, image_url) VALUES (?, ?, ?, ?)",
        title, author, body, image_url
    )
    conn.commit()
    conn.close()


def update_article(article_id, title, author, body, image_url):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE articles SET title=?, author=?, body=?, image_url=? WHERE id=?",
        title, author, body, image_url, article_id
    )
    conn.commit()
    conn.close()


def delete_article(article_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM articles WHERE id=?", article_id)
    conn.commit()
    conn.close()


def get_user(username, password):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id, username FROM users WHERE username=? AND password=?",
        username, password
    )
    row = cursor.fetchone()
    conn.close()
    return row
