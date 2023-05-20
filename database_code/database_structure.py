create_table_jobs = """
CREATE TABLE IF NOT EXISTS jobs (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    description VARCHAR(255),
    salary VARCHAR(255),
    company VARCHAR(255),
    email VARCHAR(255)
)
"""

