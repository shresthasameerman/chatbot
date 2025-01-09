import random
from typing import Dict, List, Tuple
import re

def get_random_agent_name() -> str:
    """Return a random agent name from a predefined list."""
    return random.choice(["Alex", "Charlie", "Jordan", "Taylor", "Casey"])

def generate_response(user_input: str) -> str:
    """Generate an appropriate response based on user input."""
    # Convert input to lowercase for easier matching
    user_input = user_input.lower()

    # Patterns and responses for greetings
    greetings = {
        r'\b(hi|hello|hey|howdy)\b': [
            "Hi there! How can I help you today?",
            "Hello! Nice to meet you!",
            "Hey! How are you doing?",
            "Hi! What can I do for you today?"
        ],
        r'\b(good morning)\b': [
            "Good morning! Hope you're having a great start to your day!",
            "Good morning! What can I help you with?",
            "Morning! How are you today?"
        ],
        r'\b(good afternoon)\b': [
            "Good afternoon! How can I assist you?",
            "Good afternoon! What brings you here today?",
            "Afternoon! How can I help?"
        ],
        r'\b(good evening)\b': [
            "Good evening! How may I assist you?",
            "Good evening! What can I do for you?",
            "Evening! How can I help?"
        ]
    }

    # Patterns and responses for "how are you" type questions
    how_are_you = {
        r'\b(how are you|how you doing|how\'s it going|what\'s up)\b': [
            "I'm doing great, thanks for asking! How about you?",
            "I'm excellent! How are you doing today?",
            "All good here! How's your day going?",
            "I'm wonderful! How about yourself?"
        ]
    }

    # Patterns and responses for feelings
    feelings = {
        r'\b(i\'m good|i\'m great|i\'m excellent|doing good|doing great)\b': [
            "That's wonderful to hear! What can I help you with?",
            "I'm glad you're doing well! How can I assist you today?",
            "That's great! What brings you here today?"
        ],
        r'\b(i\'m tired|i\'m exhausted|i\'m sleepy)\b': [
            "I hope you can get some rest soon! Meanwhile, how can I help you?",
            "Make sure to take care of yourself! What do you need assistance with?",
            "Remember to take breaks when needed! What can I help you with?"
        ],
        r'\b(i\'m sad|i\'m upset|i\'m unhappy)\b': [
            "I'm sorry to hear that. Is there anything I can do to help?",
            "I hope things get better soon. How can I assist you today?",
            "That must be difficult. What can I do to help?"
        ]
    }

    # Information about facilities
    facilities_info: Dict[str, Dict[str, str]] = {
        "library": {
            "location": "Building A, first floor",
            "hours": "9:00 AM to 6:00 PM",
            "details": "It's right across from the student center. Would you like directions?"
        },
        "cafeteria": {
            "location": "Student Center, ground floor",
            "hours": "7:30 AM to 8:00 PM",
            "details": "It offers multiple food stations. Need today's menu?"
        },
        "coffee": {
            "location": "Student Center, next to the cafeteria",
            "hours": "8:00 AM to 5:00 PM",
            "details": "They make amazing lattes! Want to know about their specials?"
        },
        "gym": {
            "location": "Athletics Building, behind the Student Center",
            "hours": "6:00 AM to 10:00 PM",
            "details": "It's equipped with modern facilities. Would you like to know about membership?"
        },
        "parking": {
            "location": "Lots A, B, and C",
            "hours": "Open 24/7",
            "details": "Lot A is closest to the main building, while B and C are near the Athletics Building. Need a parking map?"
        },
        "bookstore": {
            "location": "Building B, ground floor",
            "hours": "9:00 AM to 5:00 PM",
            "details": "They have all your textbook needs plus university merchandise!"
        },
        "administration": {
            "location": "Building C, second floor",
            "hours": "9:00 AM to 5:00 PM",
            "details": "This includes Admissions, Financial Aid, and the Registrar's office. Need specific directions?"
        }
    }

    # Check for "where is" questions and opening hours queries
    where_pattern = r'where(?:\s+is)?(?:\s+the)?\s+(\w+)'
    hours_pattern = r'when(?:\s+does)?(?:\s+the)?\s+(\w+)\s+(open|close|open\s+and\s+close)'

    where_match = re.search(where_pattern, user_input)
    hours_match = re.search(hours_pattern, user_input)

    if where_match:
        facility_key = where_match.group(1).lower()
        if facility_key in facilities_info:
            info = facilities_info[facility_key]
            return f"The {facility_key} is located in {info['location']}. It's open from {info['hours']}. {info['details']}"
    
    if hours_match:
        facility_key = hours_match.group(1).lower()
        if facility_key in facilities_info:
            info = facilities_info[facility_key]
            return f"The {facility_key} is open from {info['hours']}."

    # Check for keywords in facilities info
    for keyword, info in facilities_info.items():
        if keyword.lower() in user_input:
            return f"The {keyword} is located in {info['location']}. It's open from {info['hours']}. {info['details']}"

    # Check for greetings
    for pattern, responses in greetings.items():
        if re.search(pattern, user_input):
            return random.choice(responses)

    # Check for "how are you" type questions
    for pattern, responses in how_are_you.items():
        if re.search(pattern, user_input):
            return random.choice(responses)

    # Check for feelings
    for pattern, responses in feelings.items():
        if re.search(pattern, user_input):
            return random.choice(responses)

    # Check for gratitude
    if re.search(r'\b(thanks|thank you|thx|tysm)\b', user_input):
        return random.choice([
            "You're welcome! Is there anything else you'd like to know?",
            "My pleasure! Let me know if you need anything else.",
            "Happy to help! What else can I do for you?",
            "Anytime! Don't hesitate to ask if you need more help."
        ])

    # Default responses for unknown inputs
    return random.choice([
        "I'm not quite sure about that. Could you please rephrase your question?",
        "Interesting! Could you tell me more about what you're looking for?",
        "I want to help, but I'm not sure I understood. Could you explain a bit more?",
        "Hmm, I'm not quite following. Could you try asking that in a different way?",
        "I'm here to help! Could you provide more details about what you need?"
    ])

# Example usage:
user_input = "Where is the library?"
print(generate_response(user_input))

user_input = "When does the coffee shop open?"
print(generate_response(user_input))