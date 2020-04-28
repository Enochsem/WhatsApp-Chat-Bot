import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "jokes-icnuxo-d8c9b613987b.json"

import dialogflow_v2 as dialogflow 
dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "jokes-icnuxo"

def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input =dialogflow.types.TextInput(text=text, language_code = language_code)
    query_input = dialogflow,type.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(session=session, query_input=query_input)
    return response.query_result

def dialog_reply(query, session_id):
    df_response = detect_intent_from_text(query, session_id)
    return df_response.fulfillment_text