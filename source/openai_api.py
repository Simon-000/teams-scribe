# LLM API
from openai import OpenAI

# Define a function calling the API for `gpt-3.5-turbo-0125` model with prompt as a parameter 
# to enable different tasks, and context being a document that we want to perform the task on
def extract_ur_artifact(
    input_data,
    ur_prompt,
    model = "gpt-3.5-turbo-0125",
    debug = False,
    max_tokens = 150,
    stop_sequence = None
):
    """
    TODO: Google Docstring
    """
    
    # Instatiate OpenAI client
    openai_client = OpenAI()
    
    # Assign `input_data` to `context` variable
    context = input_data
    
    # If debug, print the raw model response
    if debug:
        print("Context:\n" + context)
        print("\n\n")

    try:
        # Create a chat completion using the `ur_prompt` and `context` returning the output of the UR prompt
        model_response = openai_client.chat.completions.create(
            model = model,
            messages = [
                {"role": "system", "content": "%s\n\n" % ur_prompt},
                {"role": "user", "content": "Context: %s\n\n---\n\n\nAnswer:" % context}
            ],
            temperature = 0,
            max_tokens = max_tokens,
            top_p = 1,
            frequency_penalty = 0,
            presence_penalty = 0,
            stop = stop_sequence,
        )
        
        return model_response.choices[0].message

    # Return exception if our try block failed
    except Exception as e:
        print(e)
        return ""