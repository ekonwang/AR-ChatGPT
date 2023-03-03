import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

class Refinement():
    def __init__(self, api_key=None):
        if api_key is None:
            openai.api_key
        else:
            openai.api_key = os.getenv("OPENAI_API_KEY")
    
    def __call__(self, raw_str:str):
        return Refinement.refine(raw_str)
        
    @staticmethod
    def refine(raw_str:str):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Give me a better prompt to generate an amazing painting in stable diffusion based on the input basic prompt: "
                    f"'{raw_str}'.\n\n"
                    f"1. Do not change the meaning of the basic prompt, but refine it with more realistic words to describe.\n\n2. Prompt should not exceed 50 words.\n\n3. warp prompt with \"\"",
            temperature=0.7,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0
        )
        return response["choices"][0]['text']

if __name__ == '__main__':
    print(Refinement.refine('an astronaut riding a horse'))

"""
Give me a better prompt to generate an amazing painting in stable diffusion based on the input basic prompt: 'an astronaut riding a horse'.

1. Do not change the meaning of the basic prompt, but refine it with more realistic words to describe.

2. Prompt should not exceed 50 words.

3. warp prompt with ""
 """