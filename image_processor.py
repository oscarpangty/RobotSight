import streamlit as st
from PIL import Image
import base64

base_url = 'https://api.rhymes.ai/v1'
api_key = st.secrets["aria_key"]  

from openai import OpenAI

client = OpenAI(
    base_url=base_url,
    api_key=api_key
)

def image_to_base64(image_path):
    """
    Converts an image to a base64-encoded string.

    Args:
        image_path (str): The path to the image file.

    Returns:
        str: The base64-encoded string of the image.
    """
    try:
        with open(image_path, "rb") as image_file:
            base64_string = base64.b64encode(image_file.read()).decode("utf-8")
        return base64_string
    except FileNotFoundError:
        return "Image file not found. Please check the path."
    except Exception as e:
        return f"An error occurred: {str(e)}"

dirty_items_response=""
def process_images(image1, image2):
    global dirty_items_response
    # Replace this with your actual processing logic
    # Example: performing some image processing and returning results as text
    
    # Just a placeholder for demonstration
    output_text = "Processed output text from the backend with two images."
    
    # Example of loading and performing an operation with PIL (optional)
    img1 = Image.open(image1)
    img2 = Image.open(image2)

    img1.save("image1.jpg", format="JPEG")
    img2.save("image2.jpg", format="JPEG")
    # Your image processing code here
    base64_image_1 = image_to_base64("image1.jpg")
    base64_image_2 = image_to_base64("image2.jpg")
    #base64_image_1 = image_to_base64('./room.jpg')
    #base64_image_2 = image_to_base64('./cleanroom.jpeg')
    
    response = client.chat.completions.create(
    model="aria",  # Model name updated
    messages=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image_1}"
                        }
                    },
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/jpeg;base64,{base64_image_2}"
                        }
                    },
                    {
                        "type": "text",
                        "text": '''<image><image>You are a cleaning robot. The first image is a used hotel room. What items are inside this room? The second image is the original condition of this hotel room. What items are inside this room? 
                        In comparison, what items belong to the hotel? 
                        Among items belonging to the hotel, summarize the dirty linens that appear needed to be cleaned '''  # Added <image> symbols for each image
                    }
                ]
            }
        ],
        stream=False,
        temperature=0.6,
        max_tokens=1024,
        top_p=1,
        stop=["<|im_end|>"]
    )
    
    dirty_items_response=response.choices[0].message.content
    print(response.choices[0].message.content)
    return response.choices[0].message.content


def garbage_items(image1, image2):
    global dirty_items_response
    # Replace this with your actual processing logic
    # Example: performing some image processing and returning results as text
    
    # Just a placeholder for demonstration
    output_text = "Processed output text from the backend with two images."
    
    # Example of loading and performing an operation with PIL (optional)
    img1 = Image.open(image1)
    img2 = Image.open(image2)

    img1.save("image1.jpg", format="JPEG")
    img2.save("image2.jpg", format="JPEG")
    # Your image processing code here
    base64_image_1 = image_to_base64("image1.jpg")
    base64_image_2 = image_to_base64("image2.jpg")
    #base64_image_1 = image_to_base64('./room.jpg')
    #base64_image_2 = image_to_base64('./cleanroom.jpeg')
    
    response = client.chat.completions.create(
    model="aria",  # Model name updated
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image_1}"
                    }
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/jpeg;base64,{base64_image_2}"
                    }
                },
                {
                    "type": "text",
                    "text": '''<image><image>You are a cleaning robot. The first image is a used hotel room. What items are inside this room? The second image is the original condition of this hotel room. What items are inside this room? 
                        In comparison, what items belong to the hotel? 
                        Among items belonging to the hotel, summarize the dirty linens that appear needed to be cleaned '''  # Added <image> symbols for each image
                }
            ]
        },{
            "role": "aria",
            "content": [
                {
                    "type": "text",
                    "text": f"{dirty_items_response}"
                }
            ]
        },
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": '''Except for the items to be cleaned, Summarize the plastic or paper garbage useless to either hotel or customer that needs to be thrown away.
        '''
            }
        ]
            }
            ],
        stream=False,
        temperature=0.6,
        max_tokens=1024,
        top_p=1,
        stop=["<|im_end|>"]
    )
    
    print(response.choices[0].message.content)
    return response.choices[0].message.content
    
