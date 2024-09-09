# from dotenv import load_dotenv
# import openai
# import os
# import base64

# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode('utf-8')

# def generate_caption(base64_image):
#     response = openai.chat.completions.create(
#     model="gpt-4o-mini",  # Make sure to use a vision-capable model
#     messages=[
#         {"role": "system", "content": "You are a helpful assistant."},
#         {
#             "role": "user",
#             "content": [
#                 {"type": "text", "text": """Please analyze the image provided. Return a list of all the functionalities which a tester would need to test.(functionalities which have some input to be given)
#                  Output type : comma separated values of clear names of the functionalities (Give new name to functionality in context of the page if the functionality name is vague) (don't need explanation)"""},
#                 {
#                     "type": "image_url",
#                     "image_url": {
#                         "url": f"data:image/jpeg;base64,{base64_image}"
#                     }
#                 }
#             ]
#         }
#     ],
#     max_tokens=1000
#     )
#     return response.choices[0].message.content

# base64_image = encode_image("C:/Users/KrtrimaIQ/Downloads/1.png")
# image_caption = generate_caption(base64_image)

# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI

# model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# system_rewrite = """
# You are an software tester that generates test instructions based on descriptions.
# Provide detailed testing instructions based on the description you get.
# Make sure to include cover all testcases for the given functionality.
# Each test case should include:
# -	Description: What the test case is about.
# -	Pre-conditions: What needs to be set up or ensured before testing.
# -	Testing Steps: Clear, step-by-step instructions on how to perform the test.
# -	Expected Result: What should happen if the feature works correctly.
# """

# prompt = ChatPromptTemplate.from_messages(
#     [
#         ("system", system_rewrite),
#         ("human", "{question}"),
#     ]
# )

# chain = prompt | model

# with open("file.txt","w") as f:
#     for i in image_caption.split(","):
#         response = chain.invoke({"question": i.strip()})
#         chain_resp = response.content
#         f.write(chain_resp+"\n")


# import streamlit as st
# from dotenv import load_dotenv
# import openai
# import os
# import base64
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_openai import ChatOpenAI

# # Load environment variables
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")

# # Function to encode the image to base64
# def encode_image(image_path):
#     with open(image_path, "rb") as image_file:
#         return base64.b64encode(image_file.read()).decode("utf-8")

# # Function to generate caption from OpenAI
# def generate_caption(base64_image):
#     response = openai.chat.completions.create(
#         model="gpt-4o-mini",  # Make sure to use a vision-capable model
#         messages=[
#             {"role": "system", "content": "You are a helpful assistant."},
#             {
#                 "role": "user",
#                 "content": [
#                     {
#                         "type": "text",
#                         "text": """Please analyze the image provided. Return a list of all the functionalities which a tester would need to test.(functionalities which have some input to be given)
#                                     Output type : comma separated values of clear names of the functionalities (Give new name to functionality in context of the page if the functionality name is vague) (don't need explanation)""",
#                     },
#                     {
#                         "type": "image_url",
#                         "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
#                     },
#                 ],
#             },
#         ],
#         max_tokens=1000,
#     )
#     return response.choices[0].message.content

# # Set up the prompt and model for generating test instructions
# model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# system_rewrite = """
# You are an software tester that generates test instructions based on descriptions.
# Provide detailed testing instructions based on the description you get.
# Make sure to include cover all testcases for the given functionality.
# Each test case should include:
# -	Description: What the test case is about.
# -	Pre-conditions: What needs to be set up or ensured before testing.
# -	Testing Steps: Clear, step-by-step instructions on how to perform the test.
# -	Expected Result: What should happen if the feature works correctly.
# """

# prompt = ChatPromptTemplate.from_messages(
#     [("system", system_rewrite), ("human", "{question}")]
# )

# chain = prompt | model

# # Streamlit App Layout
# st.title("Image Functionality Tester")
# st.write("Upload an image to analyze its functionalities and generate test cases.")

# # File uploader in Streamlit
# uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

# if uploaded_file is not None:
#     # Save the uploaded file temporarily
#     temp_image_path = f"temp_image.{uploaded_file.type.split('/')[-1]}"
#     with open(temp_image_path, "wb") as f:
#         f.write(uploaded_file.read())
    
#     # Encode the image to base64
#     base64_image = encode_image(temp_image_path)
    
#     # Generate caption from the image
#     st.write("Analyzing the image...")
#     image_caption = generate_caption(base64_image)
#     st.write("Functionalities detected:", image_caption)
    
#     # Generate and display test cases
#     st.write("Generating test cases...")
#     for functionality in image_caption.split(","):
#         response = chain.invoke({"question": functionality.strip()})
#         chain_resp = response.content
#         st.text_area(f"Test Cases for {functionality.strip()}", chain_resp, height=200)

#     # Optionally save results to a file (disabled since file operations are not preferred in Streamlit)
#     # with open("file.txt", "w") as f:
#     #     for functionality in image_caption.split(","):
#     #         response = chain.invoke({"question": functionality.strip()})
#     #         f.write(response.content + "\n")

#     st.success("Test cases generated successfully!")


import streamlit as st
from dotenv import load_dotenv
import openai
import os
import base64
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Function to encode the image to base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

# Function to generate caption from OpenAI
def generate_caption(base64_image, context=""):
    response = openai.chat.completions.create(
        model="gpt-4o-mini",  # Make sure to use a vision-capable model
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"""Please analyze the image provided. {context} Return a list of all the functionalities which a tester would need to test (functionalities which have some input to be given).
                                    Output type: comma-separated values of clear names of the functionalities (Give a new name to functionality in context of the page if the functionality name is vague) (don't need explanation)""",
                    },
                    {
                        "type": "image_url",
                        "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                    },
                ],
            },
        ],
        max_tokens=1000,
    )
    return response.choices[0].message.content

# Set up the prompt and model for generating test instructions
model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

system_rewrite = """
You are a software tester that generates test instructions based on descriptions.
Provide detailed testing instructions based on the description you get.
Make sure to include all test cases for the given functionality.
Each test case should include:
- Description: What the test case is about.
- Pre-conditions: What needs to be set up or ensured before testing.
- Testing Steps: Clear, step-by-step instructions on how to perform the test.
- Expected Result: What should happen if the feature works correctly.
"""

prompt = ChatPromptTemplate.from_messages(
    [("system", system_rewrite), ("human", "{question}")]
)

chain = prompt | model

# Streamlit App Layout
st.title("Image Functionality Tester")
st.write("Upload an image to analyze its functionalities and generate test cases.")

# File uploader in Streamlit
uploaded_file = st.file_uploader("Upload an Image", type=["png", "jpg", "jpeg"])

# Optional context input
user_context = st.text_area("Optional Context")

# Submit button
if st.button("Submit"):
    if uploaded_file is not None:
        # Save the uploaded file temporarily
        temp_image_path = f"temp_image.{uploaded_file.type.split('/')[-1]}"
        with open(temp_image_path, "wb") as f:
            f.write(uploaded_file.read())
        
        # Encode the image to base64
        base64_image = encode_image(temp_image_path)
        
        # Generate caption from the image
        st.write("Analyzing the image...")
        image_caption = generate_caption(base64_image, context=user_context)
        st.write("Functionalities detected:", image_caption)
        
        # Generate and display test cases
        st.write("Generating test cases...")
        for functionality in image_caption.split(","):
            response = chain.invoke({"question": functionality.strip()})
            chain_resp = response.content
            st.text_area(f"Test Cases for {functionality.strip()}", chain_resp, height=200)

        st.success("Test cases generated successfully!")
    else:
        st.error("Please upload an image before submitting.")
