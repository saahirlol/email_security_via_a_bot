# Import the required libraries
import base64
import email
import openai
import os
# Set the OpenAI API key
openai.api_key = "get ur own @ https://platform.openai.com/account/api-keys"

# Specify the OpenAI model to use
model_engine = "gpt-3.5-turbo" 

# Define an empty list to store email headers
headerxxxx = []

# Define an empty string to store the email body
yex_message = ""

# Define an empty string to store the email headers and body
emxil = ""
# Define an empty string to store the email path
file = ""
# Define a function to generate a delimiter string
def delim(times=1):
    return "★★★★★★★★★★★★★★★★★★★★★★★ \n" * times

# Define a function to parse the email file and extract the headers and body
def check(h="example.eml"):
    global headerxxxx
    global yex_message
    global emxil
    
    # Open the EML Headers
    with open(h, 'rb') as eml_file:
        
        # Parse the EML file using the email library
        eml_message = email.message_from_bytes(eml_file.read())
        
        # Access the headers of the email message
        headers = eml_message.items()
        
        # Iterate through each header
        for header, value in headers:
            
            # Ignore the Microsoft's Antispam Message Info header
            if header != 'X-Microsoft-Antispam-Message-Info':
                # Add the header to the headerxxxx list
                headerxxxx.append(f'{header}: {value}')
    
    # Open the EML Headers again
    with open(h, 'rb') as eml_file:
        
        # Parse the EML file using the email library
        eml_message = email.message_from_bytes(eml_file.read())
        
        # Initialize an empty string to store the email body
        text_content = ''
        
        # Iterate through the message parts and extract text content
        for part in eml_message.walk():
            
            # Check if the part is a text/plain
            if part.get_content_type() == 'text/plain':
                # Add the text content to the text_content variable
                text_content += part.get_payload()
            
            # Check if the part is an attachment with Base64 encoding
            elif part.get_content_disposition() == 'attachment' and part.get('Content-Transfer-Encoding') == 'base64':
                # Decode the Base64-encoded data
                decoded_data = base64.b64decode(part.get_payload())
                # Replace the Base64-encoded string with a specified string
                part.set_payload(b'REPLACE_WITH_STRING')
        
        # Store the extracted text content in the yex_message variable
        yex_message = (text_content)
    
    # Combine the email headers and body and store it in the emxil variable
    emxil = ("Headers:\n "+ str(headerxxxx) +"\n\nBody:\n" + yex_message)
# print out loading in console
def loading(*thing):
    for ting in thing:
        return(ting)

# Define a function to initiate a conversation with the GPT-3 model
def botting(prompt="You are a cybersecuity expert rating how suspicous a email is. every message you will receive will be a email."):
    global emxil
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo-0301',
        n=1,
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": emxil},
        ])
    message = response.choices[0]['message']
    print("{}: {}".format(message['role'], message['content']))
def actual(tiem):
    global file
    print(delim(tiem))
    print(loading("Logging in to openai...", "loading..." "waiting..."))
    check(file)
    botting()
    print(delim(tiem))
def select():
    global file
    # get list of eml files in directory
    eml_files = [f for f in os.listdir(os.getcwd()) if f.endswith('.eml')]

    # select eml file
    if not eml_files:
        print("No .eml files found in directory")
        exit()
    elif len(eml_files) == 1:
        eml_file = eml_files[0]
    else:
        print("Select an .eml file:")
        for i, f in enumerate(eml_files):
            print(f"{i+1}. {f}")
        selection = input("> ")
        try:
            eml_file = eml_files[int(selection)-1]
        except:
            print("Invalid selection")
            exit()

    file = os.path.join(os.getcwd(), eml_file)

select()
actual(2)
