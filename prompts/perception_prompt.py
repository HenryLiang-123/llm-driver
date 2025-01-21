def get_perception_prompt(ego_state):
    perception_prompt = f'''
    **A Language Agent for Autonomous Driving**
    Role: You are the brain of an autonomous vehicle (a.k.a. ego-vehicle). In this step, you need to extract necessary information from the driving scenario presented in the image. The information you extract must be useful for the next-step motion planning, and should be converted to fit into the given structure.

    Your task:
    1. Analyze the driving scenario in the provided image.
    2. Identify which of the following types of information are needed for motion planning:
    - **Detections**: Objects in the scene that require attention.
    - **Predictions**: Estimated future trajectories of the detected objects.
    - **Maps**: Information about traffic lanes, road shoulders, and boundaries, particularly in relation to the ego-vehicle's position.
    - **Occupancy**: Areas occupied by other objects or vehicles.

    **Ego States:**
    {ego_state}

    **Instructions**:
    - For each category (**Detections, Predictions, Maps, Occupancy**), specify True it is required and False if it is not. Do not give explanations.
    '''

    return perception_prompt


# # Collecting necessary information from driving scenarios by chatting with function call
# # Written by Jiageng Mao

# init_system_message = """
# **A Language Agent for Autonomous Driving**
# Role: You are the brain of an autonomous vehicle (a.k.a. ego-vehicle). In this step, you need to extract necessary information from the driving scenario. The information you extracted must be useful to the next-step motion planning. 

# Necessary information might include the following:
# - Detections: The detected objects that you need to pay attention to.
# - Predictions: The estimated future motions of the detected objects. 
# - Maps: Map information includes traffic lanes and road boundaries.
# - Occunpancy: Occupancy implies whether a location has been occupied by other objects.

# Task
# - You should think about what types of information (Detections, Predictions, Maps, Occupancy) you need to extract from the driving scenario.
# - Detections and Predictions are quite important for motion planning. You should call at least one of them if necessary.
# - Maps information are also important. You should pay more attention to road shoulder and lane divider information to your current ego-vehicle location.
# - I will guide you through the thinking process step by step.
# """

# detection_prompt = """
# Do you need to perform detections from the driving scenario?
# Please answer YES or NO.
# """

# prediction_prompt = """
# Do you need to perform future trajectory predictions for the detected objects?
# Please answer YES or NO.
# """

# occupancy_prompt = """
# Do you need to get occupancy information for this driving scenario?
# Please answer YES or NO.
# """

# map_prompt = """
# Do you need to get map information for this driving scenario?
# Please answer YES or NO.
# """