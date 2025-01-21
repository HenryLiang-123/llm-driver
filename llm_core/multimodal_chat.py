from pydantic import BaseModel
from typing import List, Dict
from llm_core.chat_utils import completion_with_backoff
from timeout import timeout

class FunctionCall(BaseModel):
    Detections: bool
    Predictions: bool
    Maps: bool
    Occupancy: bool

@timeout(15)
def run_one_round_multimodal_conversation(
        message: str,
        temperature: float = 0.0,
        model_name: str = "gpt-4o-mini", # "gpt-3.5-turbo-16k-0613",
        base64_image=None,
        response_format: BaseModel=FunctionCall
    ):
    """
    Perform one round of multimodal chat using OpenAI API
    """
    user_content = [
        {
            "type": "text",
            "text": message,
        },
        {
            "type": "image_url",
            "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
        },
    ]

    messages = [
        {
            "role": "system",
            "content": "Role: You are the brain of an autonomous vehicle (a.k.a. ego-vehicle). In this step, you need to extract necessary information from the driving scenario presented in the image. The information you extract must be useful for the next-step motion planning, and should be converted to fit into the given structure.",
        },
        {
            "role": "user",
            "content": user_content,
        }
    ]
    
    response = completion_with_backoff(
        model=model_name,
        messages=messages,
        temperature=temperature,
        response_format=response_format
    )

    response_message = response["choices"][0]["message"]
        
    return response_message

# def run_one_round_conversation_with_functional_call(
#         full_messages: List[Dict], 
#         system_message: str, 
#         user_message: str, 
#         functional_calls_info: List[Dict],
#         temperature: float = 0.0,
#         model_name: str = "gpt-3.5-turbo-0613" # "gpt-3.5-turbo-16k-0613"
#     ):
#     """
#     Perform one round of conversation with functional call using OpenAI API
#     """
#     message_for_this_round = [
#             {"role": "system", "content": system_message},
#             {"role": "user", "content": user_message},
#         ] if system_message else [{"role": "user", "content": user_message}]
    
#     full_messages.extend(message_for_this_round)
    
#     response = completion_with_backoff(
#         model=model_name,
#         messages=full_messages,
#         temperature=temperature,
#         functions=functional_calls_info,
#         function_call="auto",
#     )

#     response_message = response["choices"][0]["message"]
    
#     # Append assistant's reply to conversation
#     full_messages.append(response_message)
    
#     return full_messages, response_message