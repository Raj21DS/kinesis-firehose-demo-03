import streamlit as st
import streamlink

st.set_page_config(layout = "wide")
st.title("Live Youtube Multi stream Dashboard")

youtube_urls =[
  "https://www.youtube.com/watch?v=j2knrqAzYVY",
  "https://www.youtube.com/watch?v=LPZh9BOjkQs",
  "https://www.youtube.com/watch?v=X8F9JfCUWrs",
  "https://www.youtube.com/watch?v=D1eL1EnxXXQ"
]

# Define a new function
def get_stream_url(youtube_urls):
  try:
  # return the array of video quality of streams
    streams = streamlink.streams(youtube_urls)

    # check for best video quality
    if 'best' in streams:
      return streams['best'].url
    return None
  except Exception as e:
    st.error(f"Error loading stram: {e}")
    return None

# Grid setup
col1,col2 = st.columns(2)

# stream 1
with col1:
  st.subheader("Live stream 1")
  stream_url = get_stream_url(youtube_urls[0])
  if stream_url:
    st.video(stream_url)
  else:
    st.warning("Unable to load Stream")

# stream 2
with col2:
  st.subheader("Live stream 1")
  stream_url = get_stream_url(youtube_urls[1])
  if stream_url:
    st.video(stream_url)
  else:
    st.warning("Unable to load Stream")

# Grid setup
col3,col4 = st.columns(2)

# stream 3
with col3:
  st.subheader("Live stream 3")
  stream_url = get_stream_url(youtube_urls[2])
  if stream_url:
    st.video(stream_url)
  else:
    st.warning("Unable to load Stream")

# stream 4
with col4:
  st.subheader("Live stream 4")
  stream_url = get_stream_url(youtube_urls[3])
  if stream_url:
    st.video(stream_url)
  else:
    st.warning("Unable to load Stream")
      
  
  
