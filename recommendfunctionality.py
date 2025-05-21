# rule-based recommendation system
def get_suggestion(weather_desc, temp):
    """Helper function to generate weather-appropriate suggestions"""
    suggestions = []
    
    # Temperature based suggestions
    if temp >= 20:
        suggestions.append("It's quite warm - don't forget sunscreen and stay hydrated!")
    elif temp <= 10:
        suggestions.append("It's cold - remember to dress warmly!")
        
    # Weather condition based suggestions
    if any(word in weather_desc.lower() for word in ['rain', 'shower', 'drizzle', 'thunderstorm']):
        suggestions.append("Take an umbrella with you!")
    elif any(word in weather_desc.lower() for word in ['clear', 'sunny', 'sun']):
        suggestions.append("Don't forget your sunglasses!")
    elif 'cloud' in weather_desc.lower():
        suggestions.append("It might be changeable weather - be prepared!")
        
    return " ".join(suggestions) if suggestions else ""
