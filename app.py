import streamlit as st

st.title("Midori")           # big heading
st.header("Section")         # smaller heading
st.write("some text")        # general purpose — works for text, dataframes, anything
st.markdown("**bold**")      # markdown formatting

col1, col2 = st.columns(2)   # side by side columns
with col1:
    st.write("left side")



"""st.dataframe(df)             # interactive table
st.json(some_dict)           # formatted JSON"""

st.spinner("Loading...")     # loading indicator
st.success("Done!")          # green message
st.error("Something broke")  # red message

"""query = st.text_input("Ask a question")
if st.button("Search"):
    with st.spinner("Thinking..."):
        #result = your_function(query)
        #st.write(result)"""