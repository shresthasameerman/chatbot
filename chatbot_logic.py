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

    # Greetings patterns remain the same
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

    # How are you patterns remain the same
    how_are_you = {
        r'\b(how are you|how you doing|how\'s it going|what\'s up)\b': [
            "I'm doing great, thanks for asking! How about you?",
            "I'm excellent! How are you doing today?",
            "All good here! How's your day going?",
            "I'm wonderful! How about yourself?"
        ]
    }

    # Feelings patterns remain the same
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

    # Location and facility information
    location_queries: Dict[str, List[str]] = {
        "library": [
            "The main library is located in Building A, first floor. It's right across from the student center. It's open from 9:00 AM to 6:00 PM. Would you like directions?",
            "You'll find our library in Building A. Just enter through the main doors and you can't miss it! Need help finding it?",
            "The library is in Building A, with study rooms on both floors. The quiet study area is on the second floor. Would you like to know more about our facilities?"
        ],
        "cafeteria": [
            "The main cafeteria is in the Student Center, ground floor. It's open from 7:30 AM to 8:00 PM and offers multiple food stations. Need today's menu?",
            "Our cafeteria is located in the Student Center. Just follow the signs from the main entrance. They're serving some great options today!",
            "You can find the cafeteria in the Student Center. There's also a coffee shop nearby. Would you like to know about our meal plans?"
        ],
        "coffee": [
            "The coffee shop is right next to the cafeteria in the Student Center. They make amazing lattes! It's open from 8:00 AM to 5:00 PM.",
            "Looking for coffee? Head to the Student Center - the coffee shop is right by the main entrance. Their cold brew is fantastic!",
            "Our coffee shop is in the Student Center, near the study area. They have student discounts too! Want to know about their specials?"
        ],
        "gym": [
            "The gym is located in the Athletics Building, which is behind the Student Center. It's equipped with modern facilities and open from 6:00 AM to 10:00 PM.",
            "Our fitness center is in the Athletics Building. You can't miss it - it's the big building with the blue roof! Would you like to know about membership?",
            "The gym facilities are in the Athletics Building. We have a weight room, cardio area, and group fitness classes. Need more details?"
        ],
        "parking": [
            "Student parking is available in Lots A, B, and C. Lot A is closest to the main building, while B and C are near the Athletics Building. Need a parking map?",
            "We have three main parking lots: A (near main building), B and C (near Athletics). Parking permits are required. Would you like permit information?",
            "Parking lots A, B, and C are available for students. The closest one to your current location would be Lot A. Need directions?"
        ],
        "bookstore": [
            "The campus bookstore is on the ground floor of Building B, next to the Student Center. They have all your textbook needs plus university merchandise!",
            "You'll find our bookstore in Building B. They're open Monday to Friday, 9:00 AM to 5:00 PM. Need to know what textbooks you need?",
            "The bookstore is located in Building B, ground floor. They offer new, used, and rental options for textbooks. Want to know about their return policy?"
        ],
        "administration": [
            "The administration offices are in Building C, second floor. This includes Admissions, Financial Aid, and the Registrar's office. Need specific directions?",
            "All administrative services are centralized in Building C, second floor. The elevators are right by the main entrance. What services do you need?",
            "Building C houses our administration offices. You can handle most administrative tasks there. Would you like to know about their office hours?"
        ]
    }

    # First check for "where is" questions
    where_pattern = r'where(?:\s+is)?(?:\s+the)?\s+(\w+)'
    where_match = re.search(where_pattern, user_input)
    if where_match:
        location_key = where_match.group(1).lower()
        # Check if we have location information for this query
        for key, responses in location_queries.items():
            if location_key in key or key in location_key:
                return random.choice(responses)

    # Check for keywords in location queries
    for keyword, responses in location_queries.items():
        if keyword.lower() in user_input:
            return random.choice(responses)

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