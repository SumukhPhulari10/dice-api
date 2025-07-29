# dice_api.py

from flask import Flask, jsonify, request
import random
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access this backend

@app.route('/roll', methods=['GET'])
def roll_dice():
    try:
        result = random.randint(1, 6)
        return jsonify({"dice": result, "success": True})
    except Exception as e:
        return jsonify({"error": str(e), "success": False}), 500

@app.route('/roll-multiple', methods=['POST'])
def roll_multiple_dice():
    try:
        data = request.get_json()
        num_dice = data.get('count', 1)
        
        if num_dice <= 0 or num_dice > 10:  # Limit to 10 dice
            return jsonify({"error": "Invalid number of dice", "success": False}), 400
            
        results = [random.randint(1, 6) for _ in range(num_dice)]
        return jsonify({
            "dice": results,
            "total": sum(results),
            "average": round(sum(results) / len(results), 2),
            "success": True
        })
    except Exception as e:
        return jsonify({"error": str(e), "success": False}), 500

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "message": "Dice API is running"})

if __name__ == '__main__':
    print("🎲 Starting Dice Simulator API...")
    print("📡 API will be available at: http://localhost:5000")
    print("🔗 Frontend should connect to: http://localhost:3000")
    app.run(debug=True, host='0.0.0.0', port=5000)
