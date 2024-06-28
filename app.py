from flask import Flask, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/read-excel', methods=['GET'])
def read_excel():
    # Replace 'your_file.xlsx' with the path to your Excel file
    df = pd.read_excel('your_file.xlsx')
    # Convert the dataframe to a dictionary
    data = df.to_dict(orient='records')
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
