from survey import AnonymousSurvey
#define a question , make a survey
question = "what language did you first learn to speak? "
my_survey = AnonymousSurvey(question)

#show the question , and store response to the question.
my_survey.show_question()
print("enter 'q' at any time to quit \n")
while True:
    response = input("language: ")
    if response == 'q':
        break
    my_survey.store_response(response)

    #show the survey result.
    print("\n thank you to everyone who participated in the survey! ")
    my_survey.show_result()