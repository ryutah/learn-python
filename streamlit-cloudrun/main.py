import streamlit as st
import random
import time

import logging
from logging import getLogger, StreamHandler
from google.cloud.logging.handlers import StructuredLogHandler
from google.cloud.logging_v2.handlers import setup_logging

from streamlit.web.server.websocket_headers import _get_websocket_headers

import requests


@st.cache_resource
def on_google_cloud():
    try:
        requests.get(
            "http://metadata/computeMetadata/v1/instance/id",
            headers={"Metadata-Flavor": "Google"},
            timeout=0.1,
        ).text
        return True
    except:
        return False


@st.cache_resource
def initialize_logging():
    if on_google_cloud():
        print("Initializing in Google Cloud")
        handler = StructuredLogHandler()
        setup_logging(handler, log_level=logging.DEBUG)
    else:
        print("Initializing in Local")
        handler = StreamHandler()
        handler.setLevel(logging.DEBUG)
        logging.basicConfig(level=logging.DEBUG, handlers=[handler])


def response_generator():
    response = random.choice(
        (
            [
                "Hello ther! How can I assist you today?",
                "Hi, human! Is there anything I can help you with?",
                "Do you need any help?",
            ]
        )
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.2)


st.title("Simple chat")
initialize_logging()

headers = _get_websocket_headers()

logger = getLogger(__name__)

if headers is not None:
    logger.debug("=======================", extra={"foo": "bar"})
    for key, value in headers.items():
        logger.debug(f"{key}: {value}")
    logger.debug("=======================")


if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt,
        }
    )

    response = f"Echo: {prompt}"
    with st.chat_message("assistant"):
        response = st.write_stream(response_generator())
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response,
        }
    )
