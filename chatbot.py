def get_response(user_input):
    user_input = user_input.lower()

    if "course" in user_input:
        return "We offer B.Sc, B.Com, B.A and Msc courses."

    elif "fee" in user_input or "fees" in user_input:
        return "The fee structure depends on the course. Please contact the office."

    elif "average fees" in user_input:
        return "The average fees for most courses is around ₹7000 to ₹10000 for 3 years."
    
    elif "admission" in user_input:
        return "Admissions are based on online application and merit."

    elif "contact" in user_input:
        return "You can contact us at +91-04255-251144 or email principalpalladam@gmail.com."
    
    elif "hostel" in user_input:
        return "Yes, we have separate hostel facilities available for boys and girls."

    elif "location" in user_input:
        return " college is located on Mangalam road, palladam"

    elif "timing" in user_input or "time" in user_input:
        return "College timing is 10:00 AM to 3:00 PM."
    
    elif "scholarship" in user_input:
        return "We provide various scholarships primarily through government schemes."
    
    elif "library" in user_input:
        return "Our library has over 2475+ books and journals."
    
    elif "labs" in user_input:
        return "We have well-equipped computer and science labs."
    
    elif "sports" in user_input:
        return "We offer facilities for cricket, football, volleyball, and athletics."
    
    elif "events" in user_input:
        return "We host annual cultural and sports events."
    
    elif "affiliation" in user_input:
        return "We are affiliated with Bharathiar University."
    
    elif "accreditation" in user_input:
        return "Our college is accredited by NAAC with a B+ grade."
    
    elif "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! If you have any more questions, feel free to ask."
    elif"full form" in user_input:
        return "Puratchi Thalaivi Amma Government Arts And Science College"

    elif "hello" in user_input or "hi" in user_input:
        return "Hello! How can I help you?"

    else:
        return "Sorry, I didn't understand that. Please ask about courses, fees, admission, contact, or timings."
