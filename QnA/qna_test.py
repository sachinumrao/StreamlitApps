from transformers import pipeline

nlp = pipeline('question-answering')

context = """
The cost impact may also spread beyond shipping, according to the energy analyst firm Wood Mackenzie. “Knock-on effects from the cap on sulphur emissions in marine bunker fuel could even wind up giving you a more expensive plane ticket in 2020,” the company said.
"""

question = """
What is the name of anergy analyst firm?
"""

answer = nlp({'question' : question,
            'context' : context
            })['answer']

print(answer)