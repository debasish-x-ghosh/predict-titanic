def fake_predict(user_age):
    if user_age>10:
        prediction = "Survive (Over 10)"
    else:
        prediction ="Rescue (Under 10)"
    return prediction
