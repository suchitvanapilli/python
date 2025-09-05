def quiz():
    score = 0
 
    question = "Guess the capital city of Maharashtra"
    print("\n", question)
    options = ['a) chennai  b) kolkata  c) new delhi  d) mumbai']
    print("\n", options )
    correct_answer = "d"
    user_answer = input("Enter your answer: ").strip().lower()
    if user_answer == correct_answer.lower():
        print("✅ Correct answer!")
        score += 1
    else:
        print("❌ Your answer is incorrect.")


    question = "Guess the capital city of Karnataka "
    print("\n", question)
    options = ['a) bengaluru  b) coorg  c) Mangaluru d) mumbai']
    print("\n", options )
    correct_answer = "a"
    user_answer = input("Enter your answer: ").strip().lower()
    if user_answer == correct_answer.lower():
        print("✅ Correct answer!")
        score += 1
    else:
        print("❌ Your answer is incorrect.")



    question = "Guess the capital city of kerala "
    print("\n", question)
    options = ['a) chennai  b) thiruvanantha puram c) new delhi  d) mumbai']
    print("\n", options )
    correct_answer = "b"
    user_answer = input("Enter your answer: ").strip().lower()
    if user_answer == correct_answer.lower():
        print("✅ Correct answer!")
        score += 1
    else:
        print("❌ Your answer is incorrect.")



    question = "Guess the capital city of Goa"
    print("\n", question)
    options = ['a) imphal  b) Bombay  c) panaji  d) none of the above']
    print("\n", options )
    correct_answer = "c"
    user_answer = input("Enter your answer: ").strip().lower()
    if user_answer == correct_answer.lower():
        print("✅ Correct answer!")
        score += 1
    else:
        print("❌ Your answer is incorrect.")



    question = "Guess the capital city of Bihar"
    print("\n", question)
    options = ['a) patna b) jharkhand  c) chattishgarh d) rajasthan']
    print("\n", options )
    correct_answer = "a"
    user_answer = input("Enter your answer: ").strip().lower()
    if user_answer == correct_answer.lower():
        print("✅ Correct answer!")
        score += 1
    else:
        print("❌ Your answer is incorrect.")
    

    question = "guess the capital city of jharkhand "
    print("\n", question)
    options = ['a) madhya pradesh b) chattisgarh c) bihar d) ranchi ']
    print("\n", options)
    correct_answer = "d"
    user_answer = input("Enter your answer: ").strip().lower()
    if user_answer == correct_answer.lower():
        print("✅ Correct answer")
        score += 1
    else:
        print("❌ Your answer is incorrect")
   

    question = "guess the capital city of Odisha "
    print("\n", question)
    options = ['a) Bhubaneshwar b) puri c) cuttack d) calcutta ']
    print("\n", options)
    correct_answer = "a"
    user_answer = input("Enter your answer: ").strip().lower()
    if user_answer == correct_answer.lower():
        print("✅ Correct answer")
        score += 1
    else:
        print("❌ Your answer is incorrect")
    

    question = "guess the capital city of Uttar Pradesh "
    print("\n", question)
    options = ['a) Lucknow b) Prayagraj c) Kanpur d) Indore ']
    print("\n", options)
    correct_answer = "a"
    user_answer = input("Enter your answer: ").strip().lower()
    if user_answer == correct_answer.lower():
        print("✅ Correct answer")
        score += 1
    else:
        print("❌ Your answer is incorrect")
  

    question = "guess the capital city of Meghalaya"
    print("\n", question)
    options = ['a) Shillong b) Aizawl c) Agartala d) Kohima ']
    print("\n", options)
    correct_answer = "a"
    user_answer = input("Enter your answer: ").strip().lower()
    if user_answer == correct_answer.lower():
        print("✅ Correct answer")
        score += 1
    else:
        print("❌ Your answer is incorrect")
    

    question = "guess the capital city of Gujarat "
    print("\n", question)
    options = ['a) Ahmedabad b) Gandhinagar c) Surat d) Rajkot ']
    print("\n", options)
    correct_answer = "b"
    user_answer = input("Enter your answer: ").strip().lower()
    if user_answer == correct_answer.lower():
        print("✅ Correct answer")
        score += 1
    else:
        print("❌ Your answer is incorrect")
    
   
   
    print("Your score is:", score)
    percentage = (score / 10 ) * 100
    print("\n", percentage)

    if percentage >= 90:
        print("excellent")
    elif percentage >= 60:
        print("good")
    elif percentage >= 30:
        print("average")
    else :
        print("fail")
# Run the quiz
quiz()