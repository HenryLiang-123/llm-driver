# llm-driver

# Initial planning
- Multimodal gpt4o mini for tool calling
  - Use JSON mode
  - For a single call to the multimodal API, we want a json that contains yes or no for all of the functions
            {Detections: YES / NO
            Predictions: YES / NO
            Maps: YES / NO
            Occupancy: YES / NO}
- Receive info from tools
- Lidar for perception