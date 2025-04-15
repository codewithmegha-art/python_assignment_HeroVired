import configparser 
import json 
import sqlite3 
from flask import Flask, jsonify 

app = Flask(__name__)
DATABASE = 'config_data.db'


# Function to parse INI file and convert to a dictionary
def parse_config_file(file_path):
    config = configparser.ConfigParser()
    try: 
        config.read(file_path)  # <-- fixed: use read() instead of read_file()
        result = {} 
        
        for section in config.sections(): 
            result[section] = dict(config.items(section))
            
        return result 
    
    except configparser.Error as e:
        print(f"Error reading configuration file: {e}")
        return None 
    

# Save parsed config data to SQLite DB
def save_to_db(data): 
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor() 
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS config_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            data TEXT NOT NULL
        )
    ''') 
    
    cursor.execute('DELETE FROM config_data')  # Overwrite previous data
    json_data = json.dumps(data)
    cursor.execute('INSERT INTO config_data (data) VALUES (?)', (json_data,))
    conn.commit()
    conn.close() 
    

# Fetch config data from DB
def fetch_from_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT data FROM config_data')
    row = cursor.fetchone()
    conn.close()
    return json.loads(row[0]) if row else {} 


# Flask route to return config data
@app.route('/get-config', methods=['GET'])
def get_config():
    data = fetch_from_db()
    return jsonify({"Configuration File Parser Results": data})  


# Run the app
if __name__ == '__main__': 
    config_data = parse_config_file('config.ini')  # <-- make sure the file name is correct
    if config_data: 
        print("Parsed config:", config_data)
        save_to_db(config_data) 
        print("Data saved to database successfully")
        
    app.run(debug=True)
