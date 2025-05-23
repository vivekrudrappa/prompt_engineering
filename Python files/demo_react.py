# -*- coding: utf-8 -*-
"""Demo_ReAct.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ozoChJ4RU00b-0N6y9E-nGojUFhH_PM8
"""



"""# __Demo: ReAct and OpenAI__

## __Steps to Perform:__
Step 1: Set up the OpenAI API Key

Step 2: Define a system message

Step 3: Define Your Function to Get Completion

Step 4: call the function and Analyze the Output

### __Step 1: Set up the OpenAI API Key__
- Import the required libraries and set up the OpenAI API key.
"""

import os
import openai
from google.colab import userdata

openai.api_key  = userdata.get('OPENAI_API_KEY')

"""### __Step 2: Define Your System Message__
- Provide a series of steps that guide the model through a ReAct prompting.
- Add examples like few shot prompting
"""

system_message = '''
Solve a question answering task with interleaving Thought, Action, Observation steps. After these steps,
last step will provide the Action as Finish with the answer for the user question.
Thought will reason about the current situation.  Action can be of three types below.
Need to continue Thought, Action, Observation steps are shown in the examples below and then perform
the final step action as finish with the answer. see the examples on how the response is expected.

(1) Search[entity], which searches the exact entity on Wikipedia and returns the first paragraph if it exists.
If not, it will return some similar entities to search.
(2) Lookup[keyword], which returns the next sentence containing keyword in the current passage.
(3) Finish[answer], which returns the answer and finishes the task.

Here are three examples below on what is expected on the steps and final answer:
Example 1:
Question: What is the elevation range for the area that the eastern sector of the Colorado orogeny extends into?
Thought 1: I need to search Colorado orogeny, find the area that the eastern sector of the Colorado orogeny extends into,
then find the elevation range of the area.
Action 1: Search[Colorado orogeny]
Observation 1: The Colorado orogeny was an episode of mountain building (an orogeny) in Colorado and surrounding areas.
Thought 2: It does not mention the eastern sector. So I need to look up eastern sector.
Action 2: Lookup[eastern sector]
Observation 2: (Result 1 / 1) The eastern sector extends into the High Plains and is called the Central Plains orogeny.
Thought 3: The eastern sector of Colorado orogeny extends into the High Plains. So I need to search High Plains and find its elevation range.
Action 3: Search[High Plains]
Observation 3: High Plains refers to one of two distinct land regions
Thought 4: I need to instead search High Plains (United States).
Action 4: Search[High Plains (United States)]
Observation 4: The High Plains are a subregion of the Great Plains. From east to west, the High Plains rise in elevation
from around 1,800 to 7,000 ft (550 to 2,130 m).[3]
Thought 5: High Plains rise in elevation from around 1,800 to 7,000 ft, so the answer is 1,800 to 7,000 ft.
Action 5: Finish[1,800 to 7,000 ft]

Example 2:
Question: Musician and satirist Allie Goertz wrote a song about the "The Simpsons" character Milhouse, who Matt Groening named after who?
Thought 1: The question simplifies to "The Simpsons" character Milhouse is named after who. I only need to search Milhouse and
find who it is named after.
Action 1: Search[Milhouse]
Observation 1: Milhouse Mussolini Van Houten is a recurring character in the Fox animated television series The Simpsons voiced
by Pamela Hayden and created by Matt Groening.
Thought 2: The paragraph does not tell who Milhouse is named after, maybe I can look up "named after".
Action 2: Lookup[named after]
Observation 2: (Result 1 / 1) Milhouse was named after U.S. president Richard Nixon, whose middle name was Milhous.
Thought 3: Milhouse was named after U.S. president Richard Nixon, so the answer is Richard Nixon.
Action 3: Finish[Richard Nixon]

Example 3:
Question: Which documentary is about Finnish rock groups, Adam Clayton Powell or The Saimaa Gesture?
Thought 1: I need to search Adam Clayton Powell and The Saimaa Gesture, and find which documentary is about Finnish rock groups.
Action 1: Search[Adam Clayton Powell]
Observation 1: Could not find [Adam Clayton Powell]. Similar: [’Adam Clayton Powell III’, ’Seventh Avenue (Manhattan)’,
’Adam Clayton Powell Jr. State Office Building’, ’Isabel Washington Powell’, ’Adam Powell’, ’Adam Clayton Powell (film)’, ’Giancarlo Esposito’].
Thought 2: To find the documentary, I can search Adam Clayton Powell (film).
Action 2: Search[Adam Clayton Powell (film)]
Observation 2: Adam Clayton Powell is a 1989 American documentary film directed by Richard Kilberg. The film is about the rise and
fall of influential African-American politician Adam Clayton Powell Jr.[3][4] It was later aired as part of the PBS series The American Experience.
Thought 3: Adam Clayton Powell (film) is a documentary about an African-American politician, not Finnish rock groups.
So the documentary about Finnish rock groups must instead be The Saimaa Gesture.
Action 3: Finish[The Saimaa Gesture]

Example 4:
Question: What profession does Nicholas Ray and Elia Kazan have in common?
Thought 1: I need to search Nicholas Ray and Elia Kazan, find their professions, then find the profession they have in common.
Action 1: Search[Nicholas Ray]
Observation 1: Nicholas Ray (born Raymond Nicholas Kienzle Jr., August 7, 1911 - June 16, 1979) was an American film director,
screenwriter, and actor best known for the 1955 film Rebel Without a Cause.
Thought 2: Professions of Nicholas Ray are director, screenwriter, and actor. I need to search Elia Kazan next and find his professions.
Action 2: Search[Elia Kazan]
Observation 2: Elia Kazan was an American film and theatre director, producer, screenwriter and actor.
Thought 3: Professions of Elia Kazan are director, producer, screenwriter, and actor. So profession Nicholas Ray and Elia Kazan
 have in common is director, screenwriter, and actor.
Action 3: Finish[director, screenwriter, actor]
'''

"""### __Step 3: Define a Function to Get Completion__
- Construct a message with the user's prompt.
- Call the __openai.ChatCompletion.create__ method to get a response from the model.
- The temperature parameter is set to __0__ for deterministic (non-random) responses.
"""

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt}
        ]

    response = openai.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0.5,
        max_tokens=3900
    )
    return response.choices[0].message.content

"""## __Step 4: Analyze the Output__
Analyze the output of the model. If the output is not satisfactory, you can refine the prompts and repeat the process.

"""

prompt = '''Question: Aside from the Apple Remote, what other device can control the program App
Remote was originally designed to interact with?'''

response = get_completion(prompt)
print(response)

